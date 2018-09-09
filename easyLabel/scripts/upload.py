from tag.models import Picture
import os


def run():
    path = 'D:\_DATA\CASIA-FaceV5'
    rootUrl = 'http://pegn6g07j.bkt.clouddn.com/'
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

    def dfsFile(path):
        for file in os.listdir(path):
            fullPath = os.path.join(path, file)
            if os.path.isdir(fullPath):
                dfsFile(fullPath)
            else:
                picture = Picture(name=file, origin=origin, width=width,
                                  height=height, imageRelativeUrl=rootUrl + origin + '/' + file,
                                  label1=None)
                # print(picture)
                picture.save()

    dfsFile(path)
