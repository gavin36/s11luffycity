from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from api import models

from django import views


from rest_framework.response import Response

from api import serializers as api_serializers

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.versioning import URLPathVersioning
#(URLPathVersioning: 这个方案要求客户端指定版本作为URL路径的一部分。)
from rest_framework.pagination import PageNumberPagination
from api.serializers.course import CourseModleSerialzer,DegreeCourseModelSerializer
from api.utils.response import BaseResponse
# Create your views here.



#专题课(版本一)
'''
class CoursesView(APIView):
    # def get(self,request, *args, **kwargs):
    #     result=''
    #     if request.version == "v1":
    #         result = 'v1'
    #     else:
    #         result = '其他'
    #     return HttpResponse(result)
    def get(self,request,*args,**kwargs):
        """
            获取所有专题课信息
            :param request:
            :param args:
            :param kwargs:
            :return:
        """
        # 方式一：
        # course_list = list(models.Course.objects.all().values('id','name'))
        # return HttpResponse(json.dumps(course_list,ensure_ascii=False))

        # 方式二：
        course_list = models.Course.objects.all()
        ser = CourseSerializer(instance=course_list, many=True)
        return Response(ser.data)

class CourseDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        course = models.Course.objects.get(id=pk)
        ser = CourseSerializer(instance=course)
        return Response(ser.data)
'''
#专题课(版本二)

class CoursesView(APIView):
    '''
    CoursesView：专题课
    PageNumberPagination：分页
    # response = {'code':1000,'data':None,'error':None}
    '''

    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            # 从数据库取数据
            queryset=models.Course.objects.all()
            # 分页
            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset,request,self)
            # 分页之后的结果执行序列化
            ser = CourseModleSerialzer(instance=course_list, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'

        return Response(ret.dict)

class CourseDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            course = models.Course.objects.get(id=pk)
            ser = CourseModleSerialzer(instance=course)
            response['data'] = ser.data
        except Exception as e:
            response['code'] = 500
            response['error'] = '获取数据失败'
        return Response(response)
