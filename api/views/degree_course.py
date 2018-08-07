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
from api.serializers.course import DegreeCourseModelSerializer
from api.utils.response import BaseResponse


class DegreeView(APIView):
    '''
    DegreeView：学位课

    # response = {'code':1000,'data':None,'error':None}
    '''

    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            # 从数据库取数据
            queryset = models.DegreeCourse.objects.all()
            ser = DegreeCourseModelSerializer(instance=queryset, many=True)
            ret.data = ser.data
            print('_____________')
            print(ret.data)
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'

        return Response(ret.dict)
class CourseDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            course = models.DegreeCourse.objects.get(id=pk)
            ser = DegreeCourseModelSerializer(instance=course)
            response['data'] = ser.data
        except Exception as e:
            response['code'] = 500
            response['error'] = '获取数据失败'
        return Response(response)