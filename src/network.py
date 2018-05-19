from __future__ import print_function
from wifi import Cell, Scheme

def scan():
  nets = Cell.all('wlan0')
  for n in nets:
    print('-'*40)
    print('SSID:', n.ssid)
    print(' ', n.address)
    print(' Encryption:', n.encryption_type)
    print(' ', n.frequency, n.channel, n.signal,'dB')
    print('')
