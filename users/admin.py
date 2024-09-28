from django.contrib import admin

from .models import StudentProfile, TeacherProfile, StaffProfile

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'enrollment_date', 'phone')
    search_fields = ('user_username', 'level', 'phone')
    list_filter = ('level',)
    ordering = ('enrollment_date',)

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'years_of_experience', 'phone')
    search_fields = ('user_username', 'subjects', 'phone')
    list_filter = ('years_of_experience',)
    ordering = ('years_of_experience',)

@admin.register(StaffProfile)
class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'domain', 'phone')
    search_fields = ('user_username', 'domain', 'phone')
    list_filter = ('domain',)
    ordering = ('domain',)
    

