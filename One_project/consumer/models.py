from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
from hypermarket.models import Cmmodity


class MyUserManager(BaseUserManager):
    def create_user(self, username,  password=None):
        # 验证是否有用户名
        if not username:
            raise username

        user = self.model(
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,  password):
        # 设置超级用户
        user = self.create_user(
            username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    headimage = models.FileField('头像', upload_to='tmp/',null=True)
    usernickname=models.CharField('昵称',max_length=30,default='')
    username = models.CharField('用户名',max_length=30,unique=True)
    usersex=models.CharField('性别',max_length=5,default='')
    userage=models.CharField('年龄',max_length=3,default='')
    userphone=models.CharField('手机号',max_length=13)
    userEmail = models.EmailField('邮箱')

    create_time = models.DateTimeField('注册时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []  # 创建超级用户时使用

    #
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    class Meta:
        db_table = 'user'
        verbose_name='用户列表'
        verbose_name_plural=verbose_name

class UserCmmodity(models.Model):
    cmmoditynumber=models.IntegerField('订单号',unique=True,null=True)
    cmmodityname=models.CharField('商品名称',max_length=100,null=True)
    cmmodityimg = models.FileField('商品图片', upload_to='tmp/', null=True)
    price=models.DecimalField('单价',max_digits=10,decimal_places=2,null=True)
    type1=models.CharField('规格1',max_length=20)
    type2=models.CharField('规格2',max_length=20)
    pay_number=models.IntegerField('购买数量')
    address=models.CharField('送货地址',max_length=100,null=True)
    settime=models.DateField('购买时间',auto_now=True)
    pay_state=models.BooleanField('付款状态',default=False)
    evaluate_state=models.BooleanField('评价状态',default=False)
    pay_id=models.ForeignKey(Cmmodity,default='',on_delete=models.SET_DEFAULT)
    pay_userid=models.ForeignKey(MyUser,default='',on_delete=models.SET_DEFAULT)
    class Meta:
        verbose_name='用户商品列表'
        verbose_name_plural=verbose_name

class UserPin(models.Model):
    userid=models.ForeignKey(MyUser,default='',on_delete=models.SET_DEFAULT)
    cmmodityid=models.ForeignKey(Cmmodity,default='',on_delete=models.SET_DEFAULT)
    enevaluation=models.TextField('评论',null=True)
    enevaluationnumber=models.CharField('单号',max_length=50,null=True)
    pintime=models.DateField('时间',auto_now_add=True)
    class Meta:
        verbose_name='用户评论'
        verbose_name_plural=verbose_name





















