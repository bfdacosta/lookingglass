from sys import exit
from sys import argv
import os
import subprocess

class dig(object):
    def __init__ (self, domain, query_type = "A", dns = "8.8.8.8"):
        self.domain = domain
        self.dns = dns
        self.query_type = query_type
    def query (self):
        import subprocess
        if self.query_type.lower() == 'ptr':
            p = subprocess.Popen(["dig", '-x', self.domain, "@"+self.dns], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out = p.communicate()[0]
            return out
        else:
            p = subprocess.Popen(["dig", self.domain, "@"+self.dns, self.query_type], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out = p.communicate()[0]
            return out
class ping(object):
    def __init__ (self, address):
        self.address = address
    def do (self):
        import subprocess
        p = subprocess.Popen(["ping", "-c", "4", self.address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = p.communicate()[0]
        return out
class traceroute(object):
    def __init__ (self, address):
        self.address = address
    def trace (self):
        import subprocess
        p = subprocess.Popen(["/usr/sbin/traceroute", "-n", "-A", self.address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = p.communicate()[0]
        return out
class nmap(object):
    def __init__ (self, address):
        self.address = address
    def run (self):
        import subprocess
        p = subprocess.Popen(["nmap", self.address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = p.communicate()[0]
        return out
class whois(object):
    def __init__ (self, domain):
        self.domain = domain
    def query (self):
        return subprocess.call (["whois", self.domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = p.communicate()[0]
        return out

