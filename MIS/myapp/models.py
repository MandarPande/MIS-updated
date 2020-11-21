from django.db import models

# Create your models here.
class SessionYearModel(models.Model):
    id = models.AutoField(primary_key=True)
    session_start_year = models.DateField()
    session_end_year = models.DateField()

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    contact = models.IntegerField()

class Subject(models.Model):
    id =models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, default=1) #need to give default course
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Student(models.Model):
    name = models.CharField(max_length=20, null=True)
    USN = models.CharField(max_length=10, primary_key=True)
    gender = models.CharField(max_length=50)
    profile_pic = models.FileField(upload_to="Profile_pic")
    address = models.TextField()
    contact = models.IntegerField()
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Image(models.Model):
    id =models.AutoField(primary_key=True)
    Ename = models.CharField(max_length=20, null=True)
    Edate = models.CharField(max_length=15, null=True)
    photo = models.FileField(upload_to="achievements", null=True)
    s_usn = models.ForeignKey(Student, on_delete=models.CASCADE, default=1)
    date = models.DateTimeField(auto_now_add=True)
    branch = models.CharField(max_length=30,null=True)
    filetype = models.CharField(max_length=30,null=True)
    description = models.CharField(max_length=250,null=True)

class FeedBackStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class FeedBackStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Result(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    subject_exam_marks = models.FloatField(default=0)
    subject_assignment_marks = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
