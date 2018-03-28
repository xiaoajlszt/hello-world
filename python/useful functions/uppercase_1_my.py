#!/usr/bin/env python
# -*- coding:utf-8 -*-

def main():
	log = '2018-02-28 03:17:47 syslog.py[line:760] DEBUG : Data(len=438) for sending to socket : <156>Wed 28 03:17:47 internalbeta CEF:0|Trend Micro|Deep Discovery Email Inspector|3.0.0.1189|200120|Deny List updated|3|rt=Feb 28 2018 03:17:47 GMT+00:00 dvc=10.64.1.131 dvchost=internalbeta.bcc.ddei dvcmac=ec:f4:bb:de:e5:30 deviceExternalId=67067637-acbf-46de-a22d-be8d0d976cd5 cs1Label=type cs1=Deny List File SHA1 end=Mar 30 2018 03:17:03 GMT+00:00 act=Add fileHash=D2B045A85EEBCC8D70984C5F11613C94640D6448 cs2Label=RiskLevel cs2=High'
	log = transform_to_uppercase(log, 'dvcmac')
	print log

# 将字符串中的某一属性的值(key=value格式)转为大写，返回转换后的字符串
def transform_to_uppercase(log, key):
    value = ''
    pos1 = 0
    pos2 = 0

    pos1 = log.find(key)
    if pos1 == -1:
        LOGGER.error("%s is not in log." % key)
        return log
    else:
        pos1 = pos1 + len(key)
        while log[pos1] == '=' or log[pos1] == ' ':
            pos1 = pos1 + 1

        pos2 = pos1
        while log[pos2] != ' ':
            value = value + log[pos2]
            pos2 = pos2 + 1

        value = value.upper()
        
        return log[:pos1] + value + log[pos2:]  
		
if __name__ == '__main__':
	main()