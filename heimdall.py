#!/usr/bin/env python

from __future__ import print_function
from __future__ import division

from nxp_imu import IMU
from opencvutils import MJPEGServer





if __name__ == '__main__':
	print('Starting')
	
	# setup mjpeg  server
	
	# setup imu
	
	try:
		while True:
			time.sleep(1)  # FIXME
			
	except KeyboardInterrupt:
		print('Shutting down')
	
	print('bye ...')
