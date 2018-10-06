#!/usr/bin/env python

import sys

path = "https://www.jma.go.jp/jp/commonmesh/map_tile/RAILROAD/none/none/zoom%i/%i_%i.png"

for i in range(int(sys.argv[1]), int(sys.argv[2])):
    for j in range(int(sys.argv[3]), int(sys.argv[4])):
        print(path%(int(sys.argv[5]), i,j))
