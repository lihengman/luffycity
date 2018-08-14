import json
import uuid
from django.shortcuts import HttpResponse
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin

from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning
from rest_framework.pagination import PageNumberPagination

from api import models
from api.serializers.course import CourseModelSerializer, CourseSeriallizer
from api.utils.response import BaseResponse


class AuthView(ViewSetMixin, APIView):

    def login(self, request, *args, **kwargs):
        """
        用户登录认证
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        response = BaseResponse()
        try:
            user = request.data.get("username")
            pwd = request.data.get('password')
            obj = models.Account.objects.filter(username=user, password=pwd).first()
            if not obj:
                response.code = 10002
                response.error = '用户名或密码错误'
            else:
                uid = str(uuid.uuid4())
                models.UserToken.objects.update_or_create(user=obj, defaults={'token': uid})

                response.code = 99999
                response.data = uid
        except Exception as e:
            response.code = 10005
            response.error = '操作异常'
        return Response(request.dict)

