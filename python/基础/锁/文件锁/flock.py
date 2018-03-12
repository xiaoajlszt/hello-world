# -*- coding: utf-8 -*-
"""Flock module.

No descriptions.
"""

import fcntl
import os
import struct
import traceback
import subprocess
#from trend.ddi.constant.constant import Constant
from ConfigParser import ConfigParser
from StringIO import StringIO


class Flock(object):
    """Flock class.

    Flock call fcntl.flock to maintain a flock on the given file name.
    This class is also a Context Manager, user should use it with ```with'''
    statement.

    For example,
    with Flock('file_ZZZZ') as lock:
        YOUR CODE HERE

    The lock will be kept within the with-block. After leaving the with-block,
    the file lock will be released automatically.

    Attributes:
        No attributes.
    """

    def __init__(self, file_name, file_mode='a', is_shared=False, is_block=True):
        """
        This constructor need a file_name for the target file.

        Args:
            file_name: string
        """
        self._file_name = file_name
        self._file_mode = file_mode
        self._lock_op = self._get_lock_op(is_shared, is_block)

        self._fd = None

    def __enter__(self):
        self._fd = open(self._file_name, self._file_mode)

        try:
            fcntl.flock(self._fd, self._lock_op)
            self.is_locked = True
        except IOError:
            self.is_locked = False

        return self

    def __exit__(self, exc_type, exc_msg, traceback):
        if self.is_locked:
            fcntl.flock(self._fd, fcntl.LOCK_UN)
        self._fd.close()

    def _get_lock_op(self, is_shared, is_block):
        op = fcntl.LOCK_SH if is_shared else fcntl.LOCK_EX
        if not is_block:
            op |= fcntl.LOCK_NB

        return op

    def read_lock_info(self):
        '''
        [Purpose]
            To read related information which stored with lock
        [Return]
            A key-value dict
        '''
        parser = ConfigParser()
        fake_section = 'default'  # Need a fake section to match ConfigParser's requirement

        with open(self._file_name) as stream:
            fake_section_str = '[' + fake_section + ']\n'
            stream = StringIO(fake_section_str + stream.read())
            parser.readfp(stream)

        result_dict = {}
        options = parser.options(fake_section)
        for option in options:
            result_dict[option] = parser.get(fake_section, option)
        return result_dict


class FcntlFileLock:
    def __init__(self, lock_file_path, is_shared=True, timeout=-1):
        """
        [Purpose]
            Constructor
        [Parameters]
            lock_file_path: Path to lock file
            is_shared: 
                True: Shared/read lock
                False: Exclusive/write lock
            timeout: timeout in seconds                
        """
        self.lock_acquired = False
        self.lock_file_path = lock_file_path
        self.is_shared = is_shared

        calc_timeout = lambda t: t if t > 0 else 1
        self.timeout = calc_timeout(timeout)

        self.fp = None

        self.timeout_set = False
        if timeout > 0:
            self.timeout_set = True

        if is_shared:
            if not os.path.exists(lock_file_path):
                subprocess.call(['/bin/touch', lock_file_path])
            self.fp = open(lock_file_path, 'r')
        else:
            self.fp = open(lock_file_path, 'w')

    def acquire(self):
        """
        [Purpose]
            To acquire the lock
        [Parameters]
            N/A              
        """
        ret = True

        for i in xrange(self.timeout):
            try:
                if self.is_shared:
                    lockdata = struct.pack('hhllhh', fcntl.F_RDLCK, 0, 0, 0, 0, 0)
                else:
                    lockdata = struct.pack('hhllhh', fcntl.F_WRLCK, 0, 0, 0, 0, 0)
                fcntl.fcntl(self.fp, fcntl.F_SETLK, lockdata)
                ret = True
                self.lock_acquired = True
                break
            except IOError, e:
                if self.timeout_set:
                    #dprint(1, LOG_DEBUG, "%s - [%s] Failed to acquire the lock, wait..." % (i, e))
                    time.sleep(1)
                else:
                    #dprint(1, LOG_DEBUG, "[%s] Failed to acquire the lock" % e)
                    None
                ret = False
                continue
            except:
                print traceback.format_exc()
                ret = False
                break

        return ret

    def release(self):
        """
        [Purpose]
            To release the lock
        [Parameters]
            N/A              
        """
        try:
            if self.fp and self.lock_acquired:
                fcntl.fcntl(self.fp, fcntl.LOCK_UN)
                self.fp.close()

            self.lock_acquired = False
        except:
            None
