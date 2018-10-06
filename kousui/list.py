#!/usr/bin/env python

import sys
import time

from pytz import timezone
from datetime import datetime

if len(sys.argv) != 6:
    print(sys.argv[0],"[x_min] [x_max] [y_min] [y_max] [zoom]",)
    sys.exit(1)

d = datetime.datetime.now() - datetime.timedelta(minutes=10)
m = int(d.strftime("%M"))
m = m - (m%10)
now = d.strftime("%Y%m%d%H") + str(m)

path = "https://www.jma.go.jp/jp/kaikotan/kaikotan_tile/KAIKOTAN10M/%s/%s/zoom%i/%i_%i.png"

for i in range(int(sys.argv[1]), int(sys.argv[2])):
    for j in range(int(sys.argv[3]), int(sys.argv[4])):
        print(path%(now, now, int(sys.argv[5]), i,j))
