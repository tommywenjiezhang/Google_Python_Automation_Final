#!/usr/bin/env python3
from PIL import Image

import glob, os

size = 600, 400

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
        im = Image.open(infile)
            im.thumbnail(size)
                im.save(file + ".thumbnail", "JPEG")
