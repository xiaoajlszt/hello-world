# requires python 2.7 or later
"""
simpleflock
===========

Provides file lock related functions.

FileLockNB
----------

A non-blocking file lock which works with context manager. Supports both
shared and exclusive operations.

To obtain a file lock:
```
    with FileLockNB(lock_file, shared=True) as _flck:
        if _flck.locked():
            ...  # locked code here
        else:
            ...  # not locked
```

check_file_locked
-----------------

A function to non-invasively check the given file lock.
Return value is a list of processes which are currently holding the lock.

Example:
    >>> check_file_locked(lock_file)
    [(65418, 'READ'), (2461, 'READ')]  # two processes are holding the lock
    [(28418, 'WRITE')]  # a process is holding the lock exclusively
    []  # no process is holding the lock

"""

from __future__ import print_function

import os
import fcntl
from subprocess import Popen, PIPE

class FileLockNB:
    def __init__(self, lockfile, shared=None):
        self._lockfile = lockfile
        self._locked_fd = None
        self._mode = fcntl.LOCK_EX if not shared else fcntl.LOCK_SH

    def __enter__(self):
        self._try_lock()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.locked():
            self._unlock()

    def _try_lock(self):
        open_mode = os.O_RDWR | os.O_CREAT | os.O_TRUNC
        fd = os.open(self._lockfile, open_mode)

        try:
            fcntl.flock(fd, self._mode | fcntl.LOCK_NB)
        except (IOError, OSError):
            os.close(fd)
        else:
            self._locked_fd = fd

    def _unlock(self):
        fcntl.flock(self._locked_fd, fcntl.LOCK_UN)
        os.close(self._locked_fd)
        self._locked_fd = None

    def locked(self):
        return self._locked_fd is not None

def check_file_locked(lockfile):
    ret = []
    full_path = os.path.abspath(lockfile)
    try:
        proc = Popen(['lslocks', '-o', 'PID,MODE,PATH'], stdout=PIPE, universal_newlines=True)
        out, _ = proc.communicate()
        for line in out.splitlines():
            try:
                pid, mode, path = line.split(None, 2)
                pid = int(pid)
            except:
                continue
            if path == full_path:
                ret.append((pid, mode))
    except:
        raise RuntimeError('Cannot check file: {}'.format(full_path))
    return ret

if __name__ == '__main__':
    # for python 2
    try:
        input = raw_input
    except NameError:
        pass

    # unit test
    print('test file lock')

    with FileLockNB('./test_file.lck') as lock:
        if lock.locked():
            print('locked')
            print('\npress enter to leave...')
            try:
                input()
            except:
                print('\nabort...')
                os.abort()
        else:
            print('not locked')
