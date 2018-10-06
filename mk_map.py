#!/usr/bin/env python

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps

xs=20
xe=45

ys=15
ye=45

w=256*(xe-xs)
h=256*(ye-ys)

fsize=24
fname="../font_files/msgothic.ttc"


back = Image.new("RGBA", (w,h), (255,255,255))

#base = "./base_white/%i_%i.png"
base = "./base_color/%i_%i.png"
mask = "./mask/%i_%i.png"
rail = "./rail/%i_%i.png"
road = "./road/%i_%i.png"
river = "./river/%i_%i.png"
kousui = "./kousui/%i_%i.png"
suigai = "./suigai/%i_%i.png"

for iw in range(xs, xe):
    for ih in range(ys, ye):
        im1 = Image.open(base%(iw,ih)).convert("RGBA")
        im2 = Image.open(mask%(iw,ih)).convert("RGBA")
        im3 = Image.open(river%(iw,ih)).convert("RGBA")
        im4 = Image.open(road%(iw,ih)).convert("RGBA")
        im5 = Image.open(rail%(iw,ih)).convert("RGBA")
        im6 = Image.open(kousui%(iw,ih)).convert("RGBA")
        #im7 = Image.open(suigai%(iw,ih)).convert("RGBA")
        im1 = Image.alpha_composite(im1, im2)
        im1 = Image.alpha_composite(im1, im3)
        im1 = Image.alpha_composite(im1, im4)
        im1 = Image.alpha_composite(im1, im5)
        im1 = Image.alpha_composite(im1, im6)
        draw = ImageDraw.Draw(im1)
        font = ImageFont.truetype(fname, fsize)
        draw.text((0, 0), "%i_%i"%(iw,ih), font=font, fill=(0,255,0,128))
        back.paste(im1, ((iw-xs)*256, (ih-ys)*256))

back.save('map6.png')


