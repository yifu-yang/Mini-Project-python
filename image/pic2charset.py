#!/usr/bin/env python3

''' transform a picture to a char set'''

import sys
from PIL import Image

charset = list(
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. 123456789")


class Pic2CharProcessor(object):
    ''' the processor of a pic to char set'''

    def __init__(self):
        pass

    def ProcessPictureToCharFile(self, filepath, scale):
        img = Image.open(filepath)
        (width, height) = img.size
        img = img.convert("L")
        img.thumbnail((width // scale, height // scale))
        matrix = self.__convert(img, width // scale, height // scale)
        with open('test.txt', 'w') as f:
            for index in range(len(matrix)):
                f.write(matrix[index] + "\n")

    def __convert(self, img, width, height):
        matrix = []
        for y in range(height):
            tmpstr = ""
            for x in range(width):
                tmpstr += charset[img.getpixel((x, y)) // len(charset)]
            #tmpstr += "\n"
            matrix.append(tmpstr)
        return matrix


if __name__ == "__main__":
    processor = Pic2CharProcessor()
    sourcepath = sys.argv[1]
    scale = int(sys.argv[2])
    processor.ProcessPictureToCharFile(sourcepath, scale)
