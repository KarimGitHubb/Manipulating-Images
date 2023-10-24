#!/usr/bin/env python3
import glob
from PIL import Image



# get the path/directory
src_dir = '/home/karim/images'
dst_dir = '/home/karim/Newimgs'



# iterate over files in
# that directory
for images in glob.iglob(f'{src_dir}/*'):
    img = Image.open(images)
    filename = img.filename[19:-1]
    img.rotate(90).resize((128,128)).convert('RGB').save('/home/karim/Newimgs/'+str(filename),'JPEG')


