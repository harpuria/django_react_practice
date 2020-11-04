from django.db import models
from django.conf import settings

# 1(auth.USER):N(Profile) 관계
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6) # , validators = [] 이 옵션으로 유효성 검사 처리 가능