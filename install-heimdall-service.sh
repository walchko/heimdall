#!/bin/bash

set -e

# check if we are root
if [ "$EUID" -ne 0 ]; then
  echo "*** Please run as root ***"
  exit 1
fi

OS=`uname`
if [[ ! "${OS}" =~ Linux ]]; then
  echo "*** ERROR: You must run this on Linux ***"
  echo "***        ${OS} is not supported     ***"
  exit 1
fi

# setup the service
HEIMDALL_SRVC="heimdall.service"

# if the file exists, remove it ... going to dynamically create it
if [[ -f "${HEIMDALL_SRVC}" ]]; then
	rm ${HEIMDALL_SRVC}
fi

# I probably should rethink this ... want to package it on pypi
# find script, most likely in /usr/local/bin or /usr/bin
HEIMDALL=`pwd`/heimdall.py

SERVICE="                          \
[Service] \n                       \
ExecStart=${HEIMDALL} \n           \
Restart=always \n                  \
StandardOutput=syslog\n            \
StandardError=syslog\n             \
SyslogIdentifier=heimdall\n        \
User=pi\n                          \
Group=pi\n                         \
Environment=NODE_ENV=production\n  \
\n                                 \
[Install]\n                        \
WantedBy=multi-user.target\n"

# The -e makes echo respect the \n properly
echo -e ${SERVICE} > ${HEIMDALL_SRVC}

# copy
if [ ! -f "/etc/systemd/system/heimdall.service" ]; then
  cp heimdall.service /etc/systemd/system/
else
  echo "*** removing old file ***"
  rm -f /etc/systemd/system/heimdall.service
  cp heimdall.service /etc/systemd/system/
fi

# update and start
systemctl enable heimdall
service heimdall start
service heimdall status
