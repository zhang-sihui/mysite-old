import hashlib
import random
import string
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import UserForm, RegisterForm, ChangePwdForm, ResetPwdForm
from .models import User


# Create your views here.
def user(request):
    user_name = None
    if request.session.get('is_login', None):
        user_name = request.session['user_name']
        info = User.objects.get(username=user_name)
    return render(request, 'user/user.html', locals())


# 登录
def login(request):
    if request.session.get('is_login', None):  # 如果用户在线，不能重复登录
        return redirect('users:user')

    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user_info = User.objects.get(username=username)  # 查询用户名
                if user_info.password == hash_code(password):  # 判断密码
                    request.session['is_login'] = True
                    request.session['user_id'] = user_info.id
                    request.session['user_name'] = user_info.username
                    request.session['email'] = user_info.email
                    return redirect('users:user')
                else:
                    message = '密码不正确！'
            except:
                message = '用户不存在！'
        return render(request, 'user/login.html', locals())
    login_form = UserForm()
    return render(request, 'user/login.html', locals())


# 登出
def logout(request):
    if not request.session.get('is_login', None):  # 判断用户是否登录
        return redirect('users:user')
    # flush()方法是比较安全的一种做法,一次性将session中的所有内容全部清空
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect('users:user')


# 生成8位注册码
def generate_code(length):
    for_select = string.ascii_letters + string.digits
    register_code = ""
    for j in range(length):
        register_code += random.choice(for_select)
    print(register_code)
    return register_code


# 注册用户
def register(request):
    if request.session.get('is_login', None):  # 已登录则不能注册
        # 登录状态不允许注册,可以修改这条原则！
        return redirect("users:user")

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'user/register.html', locals())
            else:
                same_name_user = User.objects.filter(username=username)
                if same_name_user:  # 检测用户名是否已存在
                    message = '用户已经存在，请修改用户名！'
                    return render(request, 'user/register.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:  # 检测邮箱地址石否已存在
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'user/register.html', locals())

                new_user = User.objects.create()
                new_user.username = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.register_code = generate_code(8)
                new_user.save()
                success_message = '注册成功！去登录？'
                return render(request, 'user/register.html', locals())

    register_form = RegisterForm()
    return render(request, "user/register.html", locals())


# 密码加密
def hash_code(s, salt='site_login'):  # 添加一个字符串
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


# 修改密码
def change_pwd(request):
    if request.method == 'POST':
        change_pwd_form = ChangePwdForm(request.POST)
        if change_pwd_form.is_valid():
            username = change_pwd_form.cleaned_data['username']
            old_password = change_pwd_form.cleaned_data['old_password']
            new_password = change_pwd_form.cleaned_data['new_password']
            # 判断
            user_info = User.objects.filter(username=username)
            if user_info:
                pwd = User.objects.filter(username=username, password=hash_code(old_password))
                if pwd:
                    User.objects.filter(username=username,
                                        password=hash_code(old_password)).update(password=hash_code(new_password))
                    success_message = '密码修改成功！'
                else:
                    message = '请检查原密码是否正确！'
            elif len(user_info) == 0:
                message = '请检查用户名是否正确！'
        return render(request, 'user/change_pwd.html', locals())

    change_pwd_form = ChangePwdForm()
    return render(request, 'user/change_pwd.html', locals())


# 重置密码
def reset_pwd(request):
    if request.method == 'POST':
        reset_pwd_form = ResetPwdForm(request.POST)
        if reset_pwd_form.is_valid():
            username = reset_pwd_form.cleaned_data['username']
            email = reset_pwd_form.cleaned_data['email']
            register_code = reset_pwd_form.cleaned_data['register_code']
            new_password = reset_pwd_form.cleaned_data['new_password']
            # 判断用户是否存在
            user_info = User.objects.filter(username=username)
            if user_info:
                email = User.objects.filter(username=username, email=email)
                if email:
                    User.objects.filter(username=username).update(password=hash_code(new_password))
                    success_message = '密码重置成功！'
                else:
                    message = '请检查邮箱是否正确！'
            elif len(user_info) == 0:
                message = '请检查用户名是否正确！'
        return render(request, 'user/reset_pwd.html', locals())

    reset_pwd_form = ResetPwdForm()
    return render(request, 'user/reset_pwd.html', locals())


# 个人信息
def personal_info(request):
    user_name = None
    if request.session.get('is_login', None):
        user_name = request.session['user_name']
        info = User.objects.get(username=user_name)
    return render(request, 'user/personal_info.html', locals())
