'''
Created on Jun 26, 2016

@author: smhaus
'''

from PIL import Image, ImageFont, ImageDraw
import os

imagesdir = "D:\\MyWork\\myworkspace-e45\\mypython\\data\\images\\"
dataimagesdir = "D:\\data\\images"


allfontsA = ["arial.ttf", "arialbd.ttf", "arialbi.ttf", "ariali.ttf", "ARIALN.TTF", "ARIALNB.TTF", "ARIALNBI.TTF", "ARIALNI.TTF", 
            "ARIALUNI.TTF", "ariblk.ttf", "ARLRDBD.TTF", 
            "cour", "calibri.ttf", "calibrib.ttf", "calibrii.ttf", "calibril.ttf", "calibrili.ttf", "calibriz.ttf", "comic.ttf", "comicbd.ttf", 
            "GARA.TTF", "GARABD.TTF", "GARAIT.TTF", "georgia.ttf", "georgiab.ttf", "georgiai.ttf", "georgiaz.ttf", 
            "OCRA2_P.TTF", "OCRAEXT.TTF", "OCRAStd.otf", "OCRBMT.TTF", "OLDENGL.TTF", 
            "QT2C_B.TTF", "QT2C_I.TTF", "QT2C_P.TTF", "QT2M_P.TTF",  "QT2_B.TTF", "QT2_I.TTF", "QT2_P.TTF", 
            "STENCIL.TTF", "tahoma.ttf", "tahomabd.ttf", "times.ttf", "timesbd.ttf", "timesbi.ttf", "timesi.ttf", 
            "verdana.ttf", "verdanab.ttf", "verdanai.ttf", "verdanaz.ttf"]

allfonts = ["arial", "arialbd", "arialbi", "ariali", "ARIALN", "ARIALNB", "ARIALNBI", "ARIALNI", 
            "ARIALUNI", "ariblk", "ARLRDBD", 
            "cour", "courbd", "courbi", "couri", "calibri", "calibrib", "calibrii", "calibril", "calibrili", "calibriz", "comic", "comicbd", 
            "GARA", "GARABD", "GARAIT", "georgia", "georgiab", "georgiai", "georgiaz", 
            "OCRA2_P", "OCRAEXT", "OCRAStd.otf", "OCRBMT", "OLDENGL", 
            "QT2C_B", "QT2C_I", "QT2C_P", "QT2M_P",  "QT2_B", "QT2_I", "QT2_P", 
            "STENCIL", "tahoma", "tahomabd", "times", "timesbd", "timesbi", "timesi", 
            "verdana", "verdanab", "verdanai", "verdanaz"]

symbolfonts = ["symbol.ttf", "webdings.ttf", "wingding.ttf", "WINGDNG2.TTF", "WINGDNG3.TTF" ]

#"QT2PI_P.TTF",

def basicPillow():
    imgfile = imagesdir + "lena2.png"
    im = Image.open(imgfile)

    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=128, width=5)
    draw.line((0, im.size[1], im.size[0], 0), fill=128, width=5)
    del draw
    # write to stdout #im.save(os.sys.stdout, "PNG")
    im.show()
    
def fontPillow():
    imgfile = imagesdir + "white_1000.png"
    textex = " - AaBbGg1234"
    im = Image.open(imgfile)
    draw = ImageDraw.Draw(im)
    # use a truetype font
    colorW = (255,255,255,255)
    colorB = (0,0,0,255)
    x = 10
    y = 5
    for fontname in allfonts:
        print fontname
        font = ImageFont.truetype(fontname, 28)
        if x<1000 and y<1000:
            draw.text((x, y), fontname.lower() + textex, font=font, fill=colorB)
            y = y + 38
            if y > 990:
                y = 5
                x = x + 500
    
    
    #font = ImageFont.truetype("cour.ttf", 50)"arial.ttf"
    #draw.text((10, 50), "world", font=font)

    del draw

    # write to stdout
    #im.save(os.sys.stdout, "PNG")
    
    im.show()

if __name__ == '__main__':
    #basicPillow()
    fontPillow()
    
    