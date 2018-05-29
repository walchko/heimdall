#!/usr/bin/env python

from __future__ import print_function
# from netscan import ActiveScan.ArpScan
import netscan


ascan = netscan.ActiveScan.ArpScan()
print(ascan.scan('en0'))
