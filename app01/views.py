from django.shortcuts import render,HttpResponse

# Create your views here.
from api import models
from rest_framework.views import APIView
from rest_framework.versioning import URLPathVersioning

class DegreeCourseView(APIView):

    def get(self, request, *args, **kwargs):
        """

        :param request: 请求相关的数据
        :param args: 给浏览器相应的内容
        :param kwargs:
        :return:
        """
        # print("cvbcvcb",request.version)
        # a. 查看所有学位课并打印学位课名称以及授课老师
        # degree_list = models.DegreeCourse.objects.all().values("name", "teachers__name")
        # print("course_list", degree_list)

        # b.查看所有学位课并打印学位课名称以及学位课的奖学金
        # value_list = models.DegreeCourse.objects.all().values("name", "scholarship__value")
        # print("value_list", value_list)
        return HttpResponse("OK")

    def post(self, request, *args, **kwargs):
        return HttpResponse("OK")

#
# class Course(APIView):
#
#     def get(self, request, *args, **kwargs):
#         # c. 展示所有的专题课
#         # course_list = models.Course.objects.filter(course__degree_course__isnull=True)
#         # print(course_list)
#
#         # e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
#         # obj = models.Course.objects.get(id=1)
#         # print(obj.name)
#         # print(obj.brief)
#         # print(obj.get_level_display() )
#         # print(obj.coursedetail.hours )
#         # print(obj.coursedetail.why_study )
#         # print(obj.coursedetail.recommend_courses.all()
#
#         # f.获取id = 1的专题课，并打印该课程相关的所有常见问题
#         # course_obj = models.Course.objects.filter(id=2, degree_course__isnull=True).first()
#         # aks_list = course_obj.asked_question.all()
#         # print(aks_list)
#
#         # c_obj = Course.objects.filter(id=1).first()
#         # print(c_obj.asked_question.all().values('question'))
#
#         # obj = Course.objects.get(id=1)
#         # ask_list = obj.asked_question.all()
#         # for item in ask_list:
#         #     print(item.question,item.answer)
#
#         # g.获取id = 1的专题课，并打印该课程相关的课程大纲
#         # c_obj = Course.objects.filter(id=1)
#         # print(c_obj.values('coursedetail__courseoutline__title'))
#
#         # obj = Course.objects.get(id=1)
#         # outline_list = obj.coursedetail.courseoutline_set.all()
#         # for item in outline_list:
#         #     print(item.title,item.content)
#
#         # h.获取id = 1的专题课，并打印该课程相关的所有章节
#         # c_obj = Course.objects.filter(id=1)
#         # print(c_obj.values('coursechapters__name'))
#
#         # obj = Course.objects.get(id=1)
#         # chapter_list = obj.xxxxx.all() # 默认obj.表名_set.all()
#         # for item in chapter_list:
#         #     print(item.name)
#
#         # i.获取id = 1的专题课，并打印该课程相关的所有课时
#         # 第1章·Python 介绍、基础语法、流程控制
#             # 01 - 课程介绍（一）
#             # 01 - 课程介绍（一）
#             # 01 - 课程介绍（一）
#             # 01 - 课程介绍（一）
#             # 01 - 课程介绍（一）
#         # 第1章·Python介绍、基础语法、流程控制
#             # 01 - 课程介绍（一）
#             # 01 - 课程介绍（一）
#             # 01 - 课程介绍（一）
#             # 01 - 课程介绍（一）
#             # 01 - 课程介绍（一）
#         # c_obj = Course.objects.filter(id=1)
#         # for i in c_obj.values('coursechapters__chapter','coursechapters__name'):
#         #     print(i.get('coursechapters__chapter'),i.get('coursechapters__name'))
#         #     a_obj=CourseChapter.objects.filter(name=i.get('coursechapters__name'))
#         #     for j in a_obj.values('coursesections__name'):
#         #         print(j.get('coursesections__name'))
#
#         return HttpResponse("OK")
#
#     def post(self, request, *args, **kwargs):
#         return HttpResponse("OK")


class DegreeCourseDetail(APIView):

    def get(self, request, *args, **kwargs):
        # d.查看id = 1的学位课对应的所有模块名称
        course = models.DegreeCourse.objects.filter(id=1, course__degree_course__isnull=False).values("course__name")
        print(course)
        return HttpResponse("OK")

    def post(self, request, *args, **kwargs):
        return HttpResponse("OK")


class OftenAskedQuestion(APIView):
    def get(self, request, *args, **kwargs):
        # f.获取id = 1的专题课，并打印该课程相关的所有常见问题
        course_obj = models.DegreeCourse.objects.filter(id=1, degree_course__isnull=True).first()
        aks_list = course_obj.asked_question.all()
        print(aks_list)
        return HttpResponse("OK")

    def post(self, request, *args, **kwargs):
        return HttpResponse("OK")
