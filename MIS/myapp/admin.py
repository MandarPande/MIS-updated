from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display = ['name','USN','gender','profile_pic','address','contact','course_id','created_at','updated_at' ]

@admin.register(Result)
class StudentResult(admin.ModelAdmin):
    list_display = ['id','student_id','subject_id','subject_exam_marks','subject_assignment_marks','created_at','updated_at']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','s_usn','Ename','Edate','branch','photo','date','filetype','description' ]

@admin.register(Staff)
class Staff(admin.ModelAdmin):
    list_display = ['id','name','created_at','updated_at','contact' ]

@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = ['id','course_name', 'created_at','updated_at']

@admin.register(Subject)
class Subject(admin.ModelAdmin):
    list_display = ['id','subject_name','course_id','staff_id', 'created_at','updated_at']

@admin.register(SessionYearModel)
class Session(admin.ModelAdmin):
    list_display = ['id','session_start_year','session_end_year' ]

@admin.register(FeedBackStudent)
class FeedBackStudent(admin.ModelAdmin):
    list_display = ['id','student_id','feedback','feedback_reply','created_at','updated_at']

@admin.register(FeedBackStaff)
class FeedBackStaff(admin.ModelAdmin):
    list_display = ['id','staff_id','feedback','feedback_reply','created_at','updated_at']
