from api import models
from rest_framework import serializers


# class CourseSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()




# 学位课# a.查看所有学位课并打印学位课名称以及授课老师
class DegreeCourseModelSerializer(serializers.ModelSerializer):
    teachers = serializers.SerializerMethodField()

    # b.查看所有学位课并打印学位课名称以及学位课的奖学金
    scholarship = serializers.SerializerMethodField()

    # d. 查看id=1的学位课对应的所有模块名称
    coursename = serializers.SerializerMethodField()
    class Meta:
        model = models.DegreeCourse
        fields = ['id','name','teachers','scholarship', 'coursename']

    def get_teachers(self, row):
        #教师
        teachers_list = row.teachers.all()
        return [{'id': item.id, 'name': item.name} for item in teachers_list]

    def get_scholarship(self,ro):
        #奖学金
        scholarship_list = ro.scholarship_set.all()
        return [{'time_percent': item.time_percent, 'value': item.value} for item in scholarship_list]

    def get_coursename(self, row):
        ret_obj = row.course_set.all()

        return [{'id': item.id, 'name': item.name} for item in ret_obj]





# 老师
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = "__all__"

# 学位奖学金
class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Scholarship
        fields = "__all__"

# 专题课
# c.展示所有的专题课
class CourseModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = ['id', 'name']

# 课程详情页
class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseDetail
        fields = "__all__"

# 常见问题
class OftenAskedQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OftenAskedQuestion
        fields = "__all__"

# 课程大纲
class CourseOutlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseOutline
        fields = "__all__"

# 课程章节
class CourseChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseChapter
        fields = "__all__"

#课时
class CourseSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseSection
        fields = "__all__"

#课时
class PricePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PricePolicy
        fields = "__all__"
