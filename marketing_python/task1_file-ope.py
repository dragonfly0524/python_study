import os

path = './task1/data'
tmp = os.listdir(path)
#空のリスト作成
files = []
for filename in tmp:
    p = path + '/' + filename
    if os.path.isfile(p):
        files.append(filename)

for filename in files:
    ext = filename.split('.')[-1]
    p = path + '/' + ext
    if not os.path.exists(p):
        os.mkdir(p)

import shutil

for filename in files:
    from_path = path + '/' +filename
    ext = filename.split('.')[-1]
    to_path = path + '/' + ext
    shutil.move(from_path, to_path)
    
#効率化すると以下
import os
import shutil

path = './task1/data'
files = os.listdir(path)

for filename in files:
    from_path = path + '/' + filename
    if os.path.isfile(filename):
        ext = filename.split('.')[-1]
        to_path = path + '/' + ext
        if not os.path.exists(to_path):
            os.mkdir(to_path)
        shutil.move(from_path, to_path)



for filename in files:

    ext = filename.split('.')[-1]


    
