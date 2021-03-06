from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import StreamingHttpResponse

from .models import Picture, Label1
from .serializers import PictureSerializer, Label1Serializer, InfoSerializer


@api_view(['GET'])
def picture_info(request):
    """
    查询图片库信息 如总数，id分别为等
    :param request:
    :return:
    """
    if request.method == 'GET':
        ImageCount = Picture.objects.count()
        serializer = InfoSerializer(data={'count': ImageCount})
        if serializer.is_valid():
            return Response(data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def picture_list(request):
    """
    列出所有图片
    :param request:
    :return:
    """
    if request.method == 'GET':
        pictures = Picture.objects.all()
        serializer = PictureSerializer(pictures, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PATCH'])
def picture_detail(request, pk):
    """
    获取或更新一个picture实例
    :param request:
    :param pk:
    :return:
    """
    try:
        picture = Picture.objects.get(pk=pk)
    except Picture.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PictureSerializer(picture)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = PictureSerializer(picture, data={'label1': request.data['label1']}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def picture_random(request):
    """
    返回一组没打过标签的图片
    :param request:
    :return:
    """
    CACHE_NUM = 3
    # order_by('?')是一个低效的解决方案，鉴于目前数据量较少，故使用
    pictures = Picture.objects.filter(label1__isnull=True).order_by('?')[:CACHE_NUM]
    serializer = PictureSerializer(pictures, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
def picture_review(request, label1, step=0):
    """
    返回一组打过标签的图片
    :param step:
    :param label1:
    :param request:
    :return:
    """
    CACHE_NUM = 5
    pictures = Picture.objects.filter(label1=label1) \
                   .order_by('-updated')[step * CACHE_NUM:(step + 1) * CACHE_NUM]
    serializer = PictureSerializer(pictures, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def label1_list(request):
    """
    得到所有标签列表或添加一个新的标签
    :param request:
    :return: （更新后）所有标签列表
    """
    if request.method == 'GET':
        labels = Label1.objects.all()
        serializer_labels = Label1Serializer(labels, many=True)
        return Response(serializer_labels.data)
    elif request.method == 'POST':
        serializer = Label1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            labels = Label1.objects.all()
            serializer_labels = Label1Serializer(labels, many=True)
            return Response(serializer_labels.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def output_download(request):
    import sqlite3
    import csv

    file = open('output.csv', 'w', newline='')
    db = sqlite3.connect('./db.sqlite3')
    sql3_cursor = db.cursor()
    sql3_cursor.execute('SELECT * FROM tag_picture WHERE label1_id is not NULL and label1_id is not "这是侧脸！"')
    # print(sql3_cursor.fetchall())
    csv_out = csv.writer(file)
    # write header
    csv_out.writerow([d[0] for d in sql3_cursor.description])
    # write data
    for result in sql3_cursor:
        csv_out.writerow(result)
    db.close()

    file.close()
    file = open('output.csv', 'r', newline='')

    def file_iterator(f, chunk_size=512):
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break

    the_file_name = "output.csv"
    response = StreamingHttpResponse(file_iterator(file))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

    return response
