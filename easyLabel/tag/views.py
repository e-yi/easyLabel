from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
    pictures = Picture.objects.filter(label1=request.data['label1']).order_by('updated')[:CACHE_NUM]
    serializer = PictureSerializer(pictures, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
def picture_review(request):
    """
    返回一组打过标签的图片
    :param request:
    :return:
    """
    CACHE_NUM = 3
    pictures = Picture.objects.filter(label1__isnull=True).order_by('-updated')[:CACHE_NUM]
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

