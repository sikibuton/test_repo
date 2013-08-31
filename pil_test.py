#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      koki
#
# Created:     27/08/2013
# Copyright:   (c) koki 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
     from PIL import Image
     from PIL import ImageDraw
     img = Image.new("RGB",(256,256),(255,0,0))
     dr = ImageDraw.Draw(img)
     dr.ellipse(((96,96),(160,160)),outline=(0,0,0) ,fill= (0,0,255))
     img.save("on.jpg")

if __name__ == '__main__':
    main()
