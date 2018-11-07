from tag.models import Picture
import os


def run():
    path = './faceV5.txt'
    rootUrl = 'http://pic.puzzledsky.cn/'
    origin = 'CASIA-FaceV5'
    width = 640
    height = 480

    print(' image_path:{}\n rootUrl:{} \n origin:{} \n'
          ' width:{} height:{}\n continue? y/n'.format(
           path, rootUrl, origin, width, height))

    if input() == 'y':
        pass
    else:
        return

    with open(path, 'r') as f:
        for line in f:
            if not line:
                continue
            fileName = line.strip()
            picture = Picture(name=fileName, origin=origin, width=width, height=height,
                              imageRelativeUrl=rootUrl + origin + '/' + fileName,
                              label1=None)

    # print(picture)
    picture.save()
