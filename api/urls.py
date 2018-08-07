from django.conf.urls import url
from api.views import course


# urlpatterns = [
#     url(r'^DegreeCourseView/$', views.DegreeCourseView.as_view()),
#     url(r'Course/$', views.Course.as_view()),
# ]

urlpatterns = [
    url(r'degreecourse/$', course.DegreeCourseView.as_view()),
    url(r'degreecourse/(?P<pk>\d+)/$', course.DegreeCourseDetailView.as_view()),
    url(r'course/$', course.CourseView.as_view()),
    url(r'course/(?P<pk>\d+)/$', course.CourseDetailView.as_view()),
]