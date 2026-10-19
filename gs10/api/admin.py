from django.contrib import admin

from .models import Student
# Register your models here.
# @admin.register(Singer)
# class SingerAdmin(admin.ModelAdmin):
#     list_display = ['id' , 'name' , 'gender']

# @admin.register(Song)
# class SongAdmin(admin.ModelAdmin):
#     list_display = ['id' , 'title' , 'singer' , 'duration']
@admin.register(Student)
class studentadmin(admin.ModelAdmin):
    list_diaply = ('id' , 'name' , 'roll' , 'city')


    