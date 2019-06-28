from django.db import models

# Create your models here.
class CmmodityType(models.Model):
    id=models.AutoField(primary_key=True)
    cmmodityname=models.CharField('类型名称',max_length=10,)
    cmmodity_parent_id=models.IntegerField('父类型id')
    cmmoditynumber=models.IntegerField('类型编号')

    def __str__(self):
        return self.cmmodityname

class Cmmodity(models.Model):
    cmmodityid = models.AutoField('商品id',primary_key=True)
    cmmodityname=models.CharField('商品名称',max_length=20,default='')
    cmmodityimg=models.FileField('商品图片',upload_to='tmp/',null=True)
    cmmodityprice=models.DecimalField('商品单价',max_digits=10, decimal_places=2,default='')
    cmmoditymess=models.CharField('商品信息',max_length=100,default='')
    cmmodityspecs1=models.CharField('商品规格1',max_length=60,default='')
    cmmodityspecs2=models.CharField("商品规格2",max_length=60,default='')
    cmmoditytype=models.ForeignKey(CmmodityType,on_delete=models.SET_DEFAULT,default='')

    def __str__(self):
        return self.cmmodityname


