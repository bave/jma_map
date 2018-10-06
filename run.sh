base=`pwd`
echo ${base}

xs=20
xe=45

ys=15
ye=45

zoom=6

cd ./river
python list.py ${xs} ${xe} ${ys} ${ye} ${zoom} > list
wget -i list
cd ${base}

cd ./road
python list.py ${xs} ${xe} ${ys} ${ye} ${zoom} > list
wget -i list
cd ${base}

cd ./base_white
python list.py ${xs} ${xe} ${ys} ${ye} ${zoom} > list
wget -i list
cd ${base}

cd ./mask
python list.py ${xs} ${xe} ${ys} ${ye} ${zoom} > list
wget -i list
cd ${base}

cd ./rail
python list.py ${xs} ${xe} ${ys} ${ye} ${zoom} > list
wget -i list
cd ${base}

cd ./base_color
python list.py ${xs} ${xe} ${ys} ${ye} ${zoom} > list
wget -i list
cd ${base}

cd ./kousui
sh ./del_png.sh
python list.py ${xs} ${xe} ${ys} ${ye} ${zoom} > list
wget -i list
cd ${base}

cd ./suigai
sh ./del_png.sh
#python list.py ${xs} ${xe} ${ys} ${ye} ${zoom} > list
#wget -i list
cd ${base}
