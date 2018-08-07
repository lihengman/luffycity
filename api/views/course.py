from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from api import models
from api.utils.serializers import course, degree
from api.utils.response import BaseResponse


class DegreeCourseView(APIView):

    """
    学位课
    """
    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            # 从数据库获取数据
            # a.查看所有学位课并打印学位课名称以及授课老师
            queryset = models.DegreeCourse.objects.all()
            # 查看所有学位课并打印学位课名称以及学位课的奖学金
            # 见序列化类
            ser = degree.DegreeCourseSeriallizer(instance=queryset, many=True)
            print(1111111111)
            ret.data = ser.data
            print(22222222222)
            print(ret.data)
        except Exception as e:
            ret.code = 500
            ret.error = "获取数据失败"
        return Response(ret.dict)

    def post(self, request, *args, **kwargs):
        return HttpResponse("OK")


class DegreeCourseDetailView(APIView):
    """
    学位课详情
    """

    def get(self, request, pk, *args, **kwargs):
        ret = BaseResponse()
        try:
            # d.查看id=1的学位课对应的所有模块名称
            queryset = models.DegreeCourse.objects.filter(id=pk)
            ser = degree.DegreeCourseSeriallizer(instance=course)
            ret.data = ser.data
            print(ret.data)
        except Exception as e:
            ret.code = 500
            ret.error = "获取数据失败"
        return Response(ret.dict)

    def put(self, request, pk, *args, **kwargs):
        return HttpResponse("ok")

    def delete(self, request, pk, *args, **kwargs):
        return HttpResponse("ok")


class CourseView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("ok")

    def post(self, request, *args, **kwargs):
        return HttpResponse("ok")


class CourseDetailView(APIView):

    def get(self, request, pk, *args, **kwargs):
        ret = BaseResponse()
        try:
            # e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
            #
            # f.获取id = 1的专题课，并打印该课程相关的所有常见问题
            #
            # g.获取id = 1的专题课，并打印该课程相关的课程大纲
            #
            # h.获取id = 1的专题课，并打印该课程相关的所有章节

            queryset = models.Course.objects.filter(id=pk, degree_course__isnull=True)
            ser = course.CourseSeriallizer(instance=queryset, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = "获取数据失败"
        return Response(ret.dict)

    def put(self, request, *args, **kwargs):
        return HttpResponse("ok")

    def delete(self, request, *args, **kwargs):
        return HttpResponse("ok")