from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
# Create your models here.
class reporter(models.Model):
    s_username = models.CharField(max_length = 50)
    subject_name = models.CharField(max_length=50)
    subject_code = models.CharField(max_length = 10)
    subject_knowledge = models.IntegerField()
    pratical_knowledge = models.IntegerField()
    class_maintainance = models.IntegerField()
    f_username = models.CharField(max_length = 50)
    branch_name = models.CharField(max_length = 50)
    semester = models.IntegerField()
    update = models.DateTimeField(auto_now = True)
class subjectname(models.Model):
    s_name = models.CharField(max_length = 50, primary_key = True)
class subjectcode(models.Model):
    s_code = models.CharField(max_length = 8, primary_key = True)
class branchh(models.Model):
    s_branch = models.CharField(max_length = 30, primary_key = True)
