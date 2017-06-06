#! /usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio

@asyncio.coroutine

def hello():
    print('Hello World!')
    r = yield from asyncio.sleep(1)
    print("Hello Again!")

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello())
    loop.close()

if __name__ == '__main__':
    main()
