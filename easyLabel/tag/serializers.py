from rest_framework import serializers

from .models import Picture, Label1


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'name', 'origin', 'height',
                  'width', 'imageRelativeUrl', 'label1')


class Label1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Label1
        fields = ('id', 'label')


class Info:
    def __init__(self, count):
        self.count = count


class InfoSerializer(serializers.Serializer):
    """
    统计信息
    """
    count = serializers.IntegerField()
