from api import models

from rest_framework import serializers

# 课程大类
class CourseCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CourseCategory
        fields = "__all__"

# 课程子类
class CourseSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseSubCategory
        fields = "__all__"


# 学位课
class DegreeCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DegreeCourse
        fields = "__all__"


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
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = "__all__"

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
