#!/usr/bin/env python

from twisted.internet import protocol,reactor
from time import ctime

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print ("...connected from:%s", clnt)

    def dataReceived(self, data):
        self.transport.write(('[%s] %s' % (ctime(), data)).encode())

factory = protocol.Factory()
factory.protocol = TSServProtocol
print("waiting for connection...")
reactor.listenTCP(PORT,factory)
reactor.run()

