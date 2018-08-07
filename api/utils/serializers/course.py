from rest_framework import serializers


class CourseSeriallizer(serializers.Serializer):
    """
    只有在下面写出要显示的字段才能正确的显示,不写下面的字段只是写fiekds不会显示
    """
    name = serializers.CharField(source="name")
    level = serializers.CharField(source='get_level_display')
    why_study = serializers.CharField(source='coursedetail.why_study')
    what_to_study_brief = serializers.CharField(source='coursedetail.what_to_study_brief')
    recommend_courses = serializers.CharField(source='course.recommend_course.all')
    asked_question = serializers.CharField(source='asked_question.all')
    CourseOutline = serializers.CharField(source='coursedetail.courseoutline_set.all')
    CourseChapter = serializers.CharField(source='coursechapters.all')
    demo = serializers.SerializerMethodField()

    def get_demo(self, obj):
        data = obj.coursedetail.why_study
        return data



