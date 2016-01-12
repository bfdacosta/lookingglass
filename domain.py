#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import content

from sys import exit
from sys import argv
import os
import subprocess

class dig(object):
    ''' Get information about DNS resolution

        Attributes:
        domain      string with domain name
        query_type  (optional) with query type eg. A, MX, etc
        dns         (optional) DNS Server
    '''

    def __init__ (self, domain, query_type = "A", dns = "8.8.8.8"):
        self.domain = domain
        self.dns = dns
        self.query_type = query_type

    def query (self):
        ''' Returns the DNS query '''

        if self.query_type.lower() == 'ptr':
            p = subprocess.Popen(["dig", '-x', self.domain, "@"+self.dns], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            out = p.communicate()[0]
            return out
        else:
            p = subprocess.Popen(["dig", self.domain, "@"+self.dns, self.query_type], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            out = p.communicate()[0]
            return out

class ping(object):
    ''' Get information about the ping (icmp) '''

    def __init__ (self, address):
        self.address = address

    def do (self):
        '''  Executes the ping to the address '''

        import subprocess
        p = subprocess.Popen(["ping", "-c", "4", self.address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = p.communicate()[0]
        return out

class traceroute(object):
    ''' Get information about trace route to the address '''

    def __init__ (self, address):
        self.address = address

    def trace (self):
        ''' Executes the trace route to address '''

        p = subprocess.Popen(["/usr/sbin/traceroute", "-n", "-A", self.address], stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        out = p.communicate()[0]
        return out

class nmap(object):
    ''' Get information network mapper to the address '''

    def __init__ (self, address):
        self.address = address

    def run (self):
        ''' Executes the nmap to the host '''

        p = subprocess.Popen(["nmap", self.address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = p.communicate()[0]
        return out

class whois(object):
    ''' Get informations about the domain (whois) '''

    def __init__ (self, domain):
        self.domain = domain

    def query (self):
        ''' Executes the whois on the domain '''
        return subprocess.call (["whois", self.domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = p.communicate()[0]
        return out

