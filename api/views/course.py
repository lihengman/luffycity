from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from api import models
from api.serializers import course, degree
from api.utils.response import BaseResponse
from rest_framework.viewsets import ViewSetMixin
from rest_framework.pagination import PageNumberPagination
from api.serializers.course import CourseModelSerializer, CourseSeriallizer
import redis
conn = redis.Redis(host='192.168.11.61', port=6379)

# class DegreeCourseView(APIView):
#
#     """
#     学位课
#     """
#     def get(self, request, *args, **kwargs):
#         ret = BaseResponse()
#         try:
#             # 从数据库获取数据
#             # a.查看所有学位课并打印学位课名称以及授课老师
#             queryset = models.DegreeCourse.objects.all()
#             print(queryset)
#             # b.查看所有学位课并打印学位课名称以及学位课的奖学金
#             # 见序列化类
#             ser = degree.DegreeCourseSeriallizer(instance=queryset, many=True)
#             ret.data = ser.data
#             print(ret.data)
#         except Exception as e:
#             ret.code = 500
#             ret.error = "获取数据失败"
#             print(e)
#         return Response(ret.dict)
#
#     def post(self, request, *args, **kwargs):
#         return HttpResponse("OK")


# class DegreeCourseDetailView(APIView):
#     """
#     学位课详情
#     """
#
#     def get(self, request, pk, *args, **kwargs):
#         ret = BaseResponse()
#         try:
#             # d.查看id=1的学位课对应的所有模块名称
#             queryset = models.DegreeCourse.objects.filter(id=pk)
#             ser = degree.DegreeCourseSeriallizer(instance=course)
#             ret.data = ser.data
#             print(ret.data)
#         except Exception as e:
#             ret.code = 500
#             ret.error = "获取数据失败"
#         return Response(ret.dict)
#
#     def put(self, request, pk, *args, **kwargs):
#         return HttpResponse("ok")
#
#     def delete(self, request, pk, *args, **kwargs):
#         return HttpResponse("ok")


# class CourseView(APIView):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse("ok")
#
#     def post(self, request, *args, **kwargs):
#         return HttpResponse("ok")


# class CourseDetailView(APIView):
#
#     def get(self, request, pk, *args, **kwargs):
#         ret = BaseResponse()
#         try:
#             # e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
#             #
#             # f.获取id = 1的专题课，并打印该课程相关的所有常见问题
#             #
#             # g.获取id = 1的专题课，并打印该课程相关的课程大纲
#             #
#             # h.获取id = 1的专题课，并打印该课程相关的所有章节
#
#             queryset = models.Course.objects.filter(id=pk, degree_course__isnull=True)
#             ser = course.CourseSeriallizer(instance=queryset, many=True)
#             ret.data = ser.data
#         except Exception as e:
#             ret.code = 500
#             ret.error = "获取数据失败"
#         return Response(ret.dict)
#
#     def put(self, request, *args, **kwargs):
#         return HttpResponse("ok")
#
#     def delete(self, request, *args, **kwargs):
#         return HttpResponse("ok")


class CourseView(ViewSetMixin, APIView):

    def list(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            # 从数据库获取数据
            queryset = models.Course.objects.all()

            # 分页
            # page = PageNumberPagination()
            # course_list = page.paginate_queryset(queryset, request, self)
            # 分页之后的结果执行序列化
            # print("345354",course_list)
            ser = CourseModelSerializer(instance=queryset, many=True)
            print("45646")
            ret.data = ser.data
            print("%%%%%%")
        except Exception as e:
            ret.code = 500
            ret.error = "获取数据失败"
            print("qqqqqqqqq",e)
        return Response(ret.dict)

    def create(self):
        pass

class ShoppingCarView(ViewSetMixin, APIView):

    def list(self, request, *args, **kwargs):
        conn.hset('lh','k1','豆豆')
        conn.hset('lh','k2','果果')
        n1 = conn.hget('lh', 'k1').decode('utf-8')
        n2= conn.hget('lh', 'k2').decode('utf-8')
        print(n1, n2)
        return Response('OK')

    def create(self, request, *args, **kwargs):
        return Response('OK')