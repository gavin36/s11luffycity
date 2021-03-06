from django.conf.urls import url
from api.views import course,degree_course
urlpatterns = [
    url(r'course/$', course.CoursesView.as_view()),
    url(r'degree/$', degree_course.DegreeView.as_view()),
    url(r'course/(?P<pk>\d+)/$', course.CourseDetailView.as_view()),
    url(r'degree/(?P<pk>\d+)/$', degree_course.CourseDetailView.as_view()),

]

# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'CourseCategory', views.CourseCategoryViewSet)
# router.register(r'Course', views.CourseViewSet)
# router.register(r'CourseDetail', views.CourseDetailViewSet)
# urlpatterns += router.urls