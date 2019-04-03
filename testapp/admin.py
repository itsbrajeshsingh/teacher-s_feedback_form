from django.contrib import admin
from .models import reporter, subjectcode, subjectname, branchh
# Register your models here.
class reporterAdmin(admin.ModelAdmin):
    list_display = ['s_username','branch_name','f_username','subject_name','semester','subject_knowledge','pratical_knowledge','class_maintainance']

admin.site.register(reporter,reporterAdmin)

admin.site.register(subjectname)
admin.site.register(subjectcode)
admin.site.register(branchh)
admin.site.site_header = "Teacher's feedback admin"
admin.site.site_title = 'teachers feedback form'