from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from app02 import models

def login(request):
    """
    用户登录
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'login.html')
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')

    obj = models.UserInfo.objects.filter(name=user, pwd=pwd).first()
    if obj:
        request.session['user_info'] = {'id': obj.id, 'name': obj.name}
        return  redirect('/index')
    return render(request, 'login.html', {'msg': '用户名或密码错误'})

def index(request):
    """
    首页
    :param request:
    :return:
    """
    corrent_user_id = request.session['user_info']['id']
    return render(request, 'index.html')
def get_qrcodee(request):
    ret = {'status': True, 'data': None}
    access_url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid={appid}&redirect_uri={redirect_uri}&response_type=code&scope=snsapi_userinfo&state={state}#wechat_redirect"
    url = access_url.format(
        appid='wx13328dfbb0585940',
        redirect_uri="http://132.232.137.34:8805/get_wx_id",  # 跳转到我的网站
        state=request.session['user_info']['id']  # 用户ID
    )
    ret['data'] = url
    return JsonResponse(ret)