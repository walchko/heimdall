#!/usr/bin/env python

from __future__ import print_function
import requests
import time
from file_storage import FileStorage
import simplejson as json
from pprint import pprint
import sys


def getTimeStamp():
    return time.time()


def formatTimeStamp(ts):
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

rpis = {}

print("Starting scan")

# for n in range(140, 150):
for n in range(1, 254):
    try:
        url = "http://192.168.86.{}:8080/json".format(n)
        r = requests.get(url=url, timeout=1)
        # print(r.status_code)
        if r.status_code == 200:
            info = r.json()
            print('+', end='')
            # pprint(data)
            # print("Found:", data["hostname"], data["network"]["IPv4"]["address"])
            key = info["network"]["IPv4"]["mac"]
            data = {
                'timestamp': getTimeStamp(),
                'changed': False,
                'json': info
            }
            if key in rpis:
                if rpis[key]["json"]["hostname"] != data["json"]["hostname"]:
                    data["changed"] = True
            rpis[key] = data
    except KeyboardInterrupt:
        break
    except requests.ConnectTimeout:
        # print("Invalid:", url)
        print('.', end='')
    except requests.ConnectionError as e:
        # print("Strange:", url, e)
        print('/', end='')
    # time.sleep(0.1)
    sys.stdout.flush()

print("\nFinished scan")

if len(rpis) > 0:
    fs = FileStorage()
    fs.writeJson('network.json', rpis)
