#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
get the hosts from HOSTS_SOURCE, and write it in the hosts file of the system.
just use commond:sudo python fuckGFW.py or sudo ./fuckGFW.py
you can replace HOST_name by HOST_name.
This is to avoid "sudo" can not resolve the host problem. 
"""

import urllib2
import os
import sys
import time

HOSTS_PATH = "/etc/hosts"
HOST_NAME  = "127.0.0.1\ttux-PAF4\n"
# HOSTS_SOURCE = "https://raw.githubusercontent.com/txthinking/google-hosts/master/hosts"
# this hosts file is not longer maintained. just use the one in next line.  by tux ,20170413

HOSTS_SOURCE = "https://raw.githubusercontent.com/racaljk/hosts/master/hosts"
# HOSTS_SOURCE = "https://coding.net/u/scaffrey/p/hosts/git/raw/master/hosts"
# this is the mirror hosts

def GetRemoteHosts(url):
    f = urllib2.urlopen(url, timeout=5)
    hosts = [line for line in f]
    f.close()
    return hosts

def main():
    try:
        hosts = GetRemoteHosts(HOSTS_SOURCE)
    except IOError:
        print "Could't connect to %s. Try again." % HOSTS_SOURCE
        sys.exit(1)
    for i in range(len(hosts)):
        if hosts[i].startswith('127.0.0.1'):
            hosts.insert(i,HOST_NAME)
            break
    # for line in hosts[:40]:
    #     print line,
        # print repr(line)


    if os.path.isfile(HOSTS_PATH):
        os.rename(HOSTS_PATH, HOSTS_PATH + ".BAK")

    fp = open(HOSTS_PATH, "w")
    fp.writelines(hosts)
    fp.close()

    print "Update Hosts Success"
    print "The hosts infomation:"
    for line in hosts[:5]:
        print line,

if __name__ == "__main__":
    main()
