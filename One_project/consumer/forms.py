import re
from django import forms

class UserForm(forms.Form):
        username = forms.CharField(max_length=30, min_length=4, required=True,
                                   error_messages={'max_length': '用户名最大长度超出30个字符',
                                                   'min_length': '用户名最小长度至少为4个字符', })
        password = forms.CharField(max_length=30, min_length=5, required=True,
                                   error_messages={'max_length': '密码最大长度超出10个字符',
                                                   'min_length': '密码最小长度至少为5个字符'})
        def clean_username(self):
            regex=r'\w{4,8}'
            if re.findall(regex,self.cleaned_data["username"]) is None:
                raise forms.ValidationError('输入格式不正确')
            return self.cleaned_data["username"]


class RegForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=30)
    userPassword1 = forms.CharField(label='密码',max_length=20,min_length=5)
    userPassword2 = forms.CharField(label='重复密码',max_length=20,min_length=5)
    userphone=forms.CharField(label='手机号',max_length=13)
    userEmail = forms.EmailField(label='邮箱')


