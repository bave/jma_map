#!/usr/bin/env python

import sys
import time

if len(sys.argv) != 6:
    print(sys.argv[0],"[x_min] [x_max] [y_min] [y_max] [zoom]",)
    sys.exit(1)

prefix=time.strftime("%Y%m%d%H", time.gmtime())+'%02i'
m = int(time.strftime("%M", time.gmtime()))
m = m - (m%10) - 10
now = prefix%(m)

path = "https://www.jma.go.jp/jp/suigaimesh/suigai_tile/INUND/%s/%s/zoom%i/%i_%i.png"

for i in range(int(sys.argv[1]), int(sys.argv[2])):
    for j in range(int(sys.argv[3]), int(sys.argv[4])):
        print(path%(now, now, int(sys.argv[5]), i,j))
