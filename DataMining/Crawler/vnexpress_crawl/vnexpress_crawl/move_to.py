import glob
import shutil
import os

for filename in glob.glob('*.txt'):
    # print(filename)
    src = ''
    des = ''
    with open(filename, 'r', encoding='utf-8') as post:
        title = post.readline()
        if ':' in title:
            category = title[title.index(':') + 2:].strip('\n').strip()
            if category not in os.listdir():
                os.mkdir(category)
                # print('make')
            src = os.getcwd() + '\\' + filename
            des = os.getcwd() + '\\' + category + '\\' + filename
    print('from: ' + src)
    print('to: ' + des)
    os.rename(src, des)
    # shutil.move(src, des)
    # os.replace(src, des)