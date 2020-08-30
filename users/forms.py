from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='密码', max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=16, min_length=4,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='密码', max_length=16, min_length=6,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='确认密码', max_length=16, min_length=6,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='邮箱地址', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # captcha = CaptchaField(label='验证码')


class ChangePwdForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=16,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    old_password = forms.CharField(label='原密码', max_length=16,
                                   widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password = forms.CharField(label='新密码', max_length=16,
                                   widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # captcha = CaptchaField(label='验证码')


class ResetPwdForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    register_code = forms.CharField(label="注册码", max_length=8, widget=forms.TextInput(attrs={'class': 'form-control'}))
    new_password = forms.CharField(label='设置新密码', max_length=16,
                                   widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # captcha = CaptchaField(label='验证码')
