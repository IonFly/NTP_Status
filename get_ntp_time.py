#!/usr/bin/env python3
#
# file: get_ntp_time.py
# abstract: get latest time from ntp server
#
# credit is to be given to this StackOverflow post:
# https://stackoverflow.com/questions/36500197/python-get-time-from-ntp-server#49255977

import ntplib
from datetime import datetime, timezone

c = ntplib.NTPClient()
# Provide the respective ntp server ip in below function
response = c.request('uk.pool.ntp.org', version=3)
response.offset
# UTC timezone used here, for working with different timezones you can use [pytz library][1]
print (datetime.fromtimestamp(response.tx_time, timezone.utc))
