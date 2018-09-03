from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Picture
from .serializers import PictureSerializer


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


@api_view(['GET', 'PUT'])
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

    elif request.method == 'PUT':
        serializer = PictureSerializer(picture, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
