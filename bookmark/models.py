from django.db import models
from django.urls import reverse

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        #객체 출력 시 나타날 값, bookmark 목록에서 화면에 보여지는 목록 info
        return "이름 : " + self.site_name + ", 주소 : " + self.url

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
