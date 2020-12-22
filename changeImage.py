#!/usr/bin/env python3
from PIL import Image

import glob, os

size = 600, 400

for infile in glob.glob("./supplier-data/images/*.tiff"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im = im.convert('RGB')
    im.thumbnail(size)
    im.save(file + ".jpeg", "JPEG", quality=100)
