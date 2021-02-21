import hashlib
import random
import string
import markdown
from django.shortcuts import render, redirect
from .forms import UserForm, RegisterForm, ChangePwdForm, ResetPwdForm
from .models import User, Notice


# Create your views here.

def user(request):
    user_name = None
    if request.session.get('is_login', None):
        user_name = request.session['user_name']
        info = User.objects.get(username=user_name)
    # 返回最后创建，而非最后日期
    notice = Notice.objects.last()
    if notice:
        notice.content = markdown.markdown(notice.content,
                                           extensions=[
                                               'markdown.extensions.extra',
                                               'markdown.extensions.codehilite',
                                               'markdown.extensions.toc',
                                           ])
    else:
        not_notice = '暂时没有通知!'
    return render(request, 'user/user.html', locals())


def login(request):
    if request.session.get('is_login', None):  # 如果用户在线，不能重复登录
        return redirect('users:user')

    if request.method == 'POST':
        login_form = UserForm(request.POST)
        # error_message = '请检查填写的内容！'
        error_message = '验证码错误！'
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            captcha = login_form.cleaned_data['captcha']
            try:
                user_info = User.objects.get(username=username)
                if user_info.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user_info.id
                    request.session['user_name'] = user_info.username
                    request.session['email'] = user_info.email
                    return redirect('users:user')
                else:
                    error_message = '密码不正确！'
            except:
                error_message = '用户不存在！'
        return render(request, 'user/login.html', locals())
    login_form = UserForm()
    return render(request, 'user/login.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('users:user')
    # flush()方法是比较安全的一种做法,一次性将session中的所有内容全部清空
    request.session.flush()
    return redirect('users:user')


def generate_register_code(length):
    for_select = string.ascii_letters + string.digits
    register_code = ''
    for j in range(length):
        register_code += random.choice(for_select)
    return register_code


def register(request):
    if request.session.get('is_login', None):  # 已登录则不能注册
        # 登录状态不允许注册,可以修改这条原则！
        return redirect("users:user")
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        error_message = '验证码错误！'
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            if password1 != password2:
                error_message = '两次输入的密码不同！'
                return render(request, 'user/register.html', locals())
            else:
                same_name_user = User.objects.filter(username=username)
                if same_name_user:
                    error_message = '用户已经存在，请修改用户名！'
                    return render(request, 'user/register.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:
                    error_message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'user/register.html', locals())
                new_user = User.objects.create()
                new_user.username = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.register_code = '#' + generate_register_code(8)
                new_user.save()
                success_message = '注册成功！去登录？'
                return render(request, 'user/register.html', locals())
        return render(request, 'user/register.html', locals())
    register_form = RegisterForm()
    return render(request, "user/register.html", locals())


def hash_code(s, salt='site_login'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update 方法只接收 bytes 类型
    return h.hexdigest()


def change_pwd(request):
    if request.method == 'POST':
        change_pwd_form = ChangePwdForm(request.POST)
        error_message = '验证码错误！'
        if change_pwd_form.is_valid():
            username = change_pwd_form.cleaned_data['username']
            old_password = change_pwd_form.cleaned_data['old_password']
            new_password = change_pwd_form.cleaned_data['new_password']
            user_info = User.objects.filter(username=username).values('username', 'password')
            if user_info:
                if hash_code(old_password) == user_info[0]['password']:
                    User.objects.filter(username=username,
                                        password=hash_code(old_password)).update(password=hash_code(new_password))
                    success_message = '密码修改成功！'
                else:
                    error_message = '请检查原密码是否正确！'
            elif len(user_info) == 0:
                error_message = '请检查用户名是否正确！'
        return render(request, 'user/change_pwd.html', locals())
    change_pwd_form = ChangePwdForm()
    return render(request, 'user/change_pwd.html', locals())


def reset_pwd(request):
    if request.method == 'POST':
        reset_pwd_form = ResetPwdForm(request.POST)
        error_message = '验证码错误！'
        if reset_pwd_form.is_valid():
            username = reset_pwd_form.cleaned_data['username']
            email = reset_pwd_form.cleaned_data['email']
            register_code = reset_pwd_form.cleaned_data['register_code']
            new_password = reset_pwd_form.cleaned_data['new_password']
            user_info = User.objects.filter(username=username).values('username', 'email', 'register_code')
            if user_info:
                if email == user_info[0]['email']:
                    if register_code == user_info[0]['register_code']:
                        User.objects.filter(username=username).update(password=hash_code(new_password))
                        success_message = '密码重置成功！'
                    else:
                        error_message = '注册码错误！'
                else:
                    error_message = '请检查邮箱是否正确！'
            elif len(user_info) == 0:
                error_message = '请检查用户名是否正确！'
        return render(request, 'user/reset_pwd.html', locals())
    reset_pwd_form = ResetPwdForm()
    return render(request, 'user/reset_pwd.html', locals())


def get_user_info(request):
    user_name = None
    if request.session.get('is_login', None):
        user_name = request.session['user_name']
        info = User.objects.get(username=user_name)
    return render(request, 'user/user_info.html', locals())
