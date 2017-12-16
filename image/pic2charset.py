#!/usr/bin/env python3

''' transform a picture to a char set'''

import os
import sys
import time

from PIL import Image

charset = list(
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. 123456789")

# static play time : 3 seconds
gifPlayTime = 3

class Pic2CharProcessor(object):
    ''' the processor of a pic to char set'''

    def __init__(self):
        pass

    def ProcessPictureToCharFile(self, filepath, scale):
        img = Image.open(filepath)
        matrix = self.__convert(img, scale)
        self.__saveFile(filepath, matrix)

    def ProcessGifPictureToCharFile(self, filepath, scale):
        index = 1
        im = Image.open(filepath)
        matrixes = []
        matrixes.append(self.__convert(im, scale))
        # TODO I'm not sure how to save gif
        index += 1
        try:
            while 1:
                im.seek(im.tell() + 1)
                matrixes.append(self.__convert(im, scale))
                index += 1
        except EOFError:
            print("finish process frame")
        self.__displayGifCharset(matrixes)

    def __displayGifCharset(self, gifCharset):
        frameCount = len(gifCharset)
        frameSleepTime = gifPlayTime/frameCount
        time.sleep(2)
        os.system("clear")
        for frameIndex in range(frameCount):
            print(gifCharset[frameIndex])
            # clear screen
            time.sleep(frameSleepTime/2)
            i = os.system('clear')
            time.sleep(frameSleepTime)
        # TODO smooth play a gif picture 


    def __convert(self, img, scale):
        (width, height) = img.size
        img = img.convert("L")
        img.thumbnail((width // scale, height // scale))
        (width, height) = (width // scale, height // scale)
        matrix = ""  # define an empty string
        for y in range(height):
            tmpstr = ""
            for x in range(width):
                tmpstr += charset[img.getpixel((x, y)) // len(charset)]
            matrix += tmpstr + "\n"
        return matrix

    def __saveFile(self, filename, charset):
        with open(filename + '.txt', 'w') as f:
            f.write(charset)


if __name__ == "__main__":
    processor = Pic2CharProcessor()
    sourcepath = sys.argv[1]
    scale = int(sys.argv[2])
    transforType = int(sys.argv[3])
    if 1 == transforType:
        processor.ProcessPictureToCharFile(sourcepath, scale)
    else:
        processor.ProcessGifPictureToCharFile(sourcepath, scale)
