#!/usr/bin/python
import dns.resolver
import os, sys
#r = dns.resolver.Resolver()
#r.namerservers = ['127.0.0.1']

r = dns.resolver.Resolver()
r.namerservers =  ['38.99.188.10']
answers = r.query('tekyhost.com', 'A')

#answers = dns.resolver.query('tekyhost.com', 'A')
for rdata in answers:
#    print 'Host', rdata.exchange, 'has preference', rdata.preference
#       print rdata.exchange

        if rdata != '38.99.188.10':
                sys.exit(2)       # CRITICAL
        else:
                sys.exit(0)       # OK
~                                      
