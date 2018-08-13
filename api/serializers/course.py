from rest_framework import serializers
from api import models


class CourseSeriallizer(serializers.Serializer):
    #     pass
    #     """
    #     只有在下面写出要显示的字段才能正确的显示,不写下面的字段只是写fiekds不会显示
    #     """
    id = serializers.IntegerField()
    name = serializers.CharField()


#     level = serializers.CharField(source='get_level_display')
#     why_study = serializers.CharField(source='coursedetail.why_study')
#     what_to_study_brief = serializers.CharField(source='coursedetail.what_to_study_brief')
#     recommend_courses = serializers.CharField(source='course.recommend_course.all')
#     asked_question = serializers.CharField(source='asked_question.all')
#     CourseOutline = serializers.CharField(source='coursedetail.courseoutline_set.all')
#     CourseChapter = serializers.CharField(source='coursechapters.all')
#     demo = serializers.SerializerMethodField()
#
#     def get_demo(self, obj):
#         data = obj.coursedetail.why_study
#         return data


class CourseModelSerializer(serializers.Serializer):
    level_name = serializers.CharField(source='get_level_display')
    hours = serializers.CharField(source='coursedetail.hours')
    course_slogan = serializers.CharField(source='coursedetail.course_slogan')
    # recommend_courses = serializers.CharField(source='coursedetail.recommend_courses.all')

    # recommend_courses = serializers.SerializerMethodField()
    # def get_recommend_courses(self,obj):
    #     li = []
    #     for item in obj.coursedetail.recommend_courses.all():
    #         li.append(item.name)
    #     return li

    #
    # class Meta:
    #     model = models.Course
    #     fields = ['id', 'name', 'level_name', 'hours', 'course_slogan','recommend_courses123']

    # def get_recommend_courses123(self, row):
    #     recommend_list = row.coursedetail.hours
    #     print("**********", recommend_list)
    #     # return [{'id':item.id, 'name':item.name} for item in recommend_list]
    #     return 123

    # recommend_courses = serializers.SerializerMethodField()
    #
    # class Meta:
    #     model = models.Course
    #     fields = ['id','name','level_name','hours','course_slogan','recommend_courses']
    #
    # def get_recommend_courses(self,row):
    #     recommend_list = row.coursedetail.recommend_courses.all()
    #     return [ {'id':item.id,'name':item.name} for item in recommend_list]
