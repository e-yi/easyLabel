from django.db import models


class Label1(models.Model):
    """
    可能有多个标签类型，比如发型、脸型之类，所以此处标号为1
    """
    label = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.label


class Picture(models.Model):
    """
    存储图片基本信息
    """
    name = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)  # 图片从何而来
    width = models.IntegerField()
    height = models.IntegerField()
    imageRelativeUrl = models.URLField()
    label1 = models.ForeignKey(Label1, on_delete=models.SET(None), null=True,
                               blank=True, )
    updated = models.DateTimeField(auto_now=True)



    def __str__(self):
        return "picture {} '{}' size:{}*{} updated at {}".format(
            self.id, self.name, self.width, self.height, self.updated)

    def get_absolute_url(self):
        return 'picture_detail', None, {'object_id': self.id}
