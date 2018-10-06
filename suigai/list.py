#!/usr/bin/env python

import sys
import time
import datetime

from pytz import timezone

if len(sys.argv) != 6:
    print(sys.argv[0],"[x_min] [x_max] [y_min] [y_max] [zoom]",)
    sys.exit(1)

d = datetime.datetime.now(timezone('GMT'))
d = d - datetime.timedelta(minutes=(d.minute%10+10), seconds=d.second, microseconds=d.microsecond)
now = d.strftime("%Y%m%d%H%M")

path = "https://www.jma.go.jp/jp/suigaimesh/suigai_tile/INUND/%s/%s/zoom%i/%i_%i.png"

for i in range(int(sys.argv[1]), int(sys.argv[2])):
    for j in range(int(sys.argv[3]), int(sys.argv[4])):
        print(path%(now, now, int(sys.argv[5]), i,j))
