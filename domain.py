#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import content
import runsub


class Dig(object):
    """ Get information about DNS resolution

        Attributes:
        domain      string with domain name
        query_type  (optional) with query type eg. A, MX, etc
        dns         (optional) DNS Server
    """

    def __init__(self, domain, query_type="A", dns="8.8.8.8"):
        self.domain = domain
        self.dns = dns
        self.query_type = query_type

    def query(self):
        """ Returns the DNS query """

        dig_cmd = 'dig {0} @{1} {2}'.format(self.domain, self.dns)
        dig_ptr_cmd = 'dig -x {0} @{1}'.format(self.domain, self.dns)

        if self.query_type.lower() == 'ptr':
            out = runsub.cmd(dig_ptr_cmd)
            return out[1]

        else:
            out = runsub.cmd(dig_cmd)

            return out[1]


class Ping(object):
    """ Get information about the ping (icmp) """

    def __init__(self, address):
        self.address = address

    def do(self):
        """  Executes the ping to the address """

        ping_cmd = 'ping -c 4 {0}'.format(self.address)
        out = runsub.cmd(ping_cmd)
        return out[1]


class Traceroute(object):
    """ Get information about trace route to the address """

    def __init__(self, address):
        self.address = address

    def trace(self):
        """ Executes the trace route to address """

        traceroute_cmd = '/usr/sbin/traceroute -n -A {0}'.format(self.address)
        out = runsub.cmd(traceroute_cmd)

        return out[1]


class NMap(object):
    """ Get information network mapper to the address """

    def __init__(self, address):
        self.address = address

    def run(self):
        """ Executes the nmap to the host """

        nmap_cmd = 'map {0}'.format(self.address)
        out = runsub.cmd(nmap_cmd)

        return out[1]


class Whois(object):
    """ Get informations about the domain (whois) """

    def __init__(self, domain):
        self.domain = domain

    def query(self):
        """ Executes the whois on the domain """

        whois_cmd = 'whois {0}'.format(self.domain)
        out = runsub.cmd(whois_cmd)

        return out[1]
