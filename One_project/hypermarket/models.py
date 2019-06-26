from django.db import models

# Create your models here.

class Cmmodity(models.Model):
    cmmodityname=models.CharField('商品名称',max_length=20,default='')
    cmmodityprice=models.DecimalField('商品单价',max_digits=10, decimal_places=2,default='')
    cmmoditymess=models.CharField('商品信息',max_length=100,default='')
    cmmodityspecs1=models.CharField('商品规格1',max_length=60,default='')
    cmmodityspecs2=models.CharField("商品规格2",max_length=60,default='')


