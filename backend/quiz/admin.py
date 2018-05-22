from django.contrib import admin
from .models import Group, UserToGroup, Course, GroupToCourse, QuizPassing, QuizToCourse

#admin.site.register(GroupOfUsers)
#admin.site.register(UserToGroup)
admin.site.register(QuizPassing)

admin.site.register(QuizToCourse)

@admin.register(Group)
class GroupOfUsersAdmin(admin.ModelAdmin):
    pass

@admin.register(UserToGroup)
class UserToGroupAdmin(admin.ModelAdmin):
    list_display = ('user', 'group')
    list_filter = ('user', 'group')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(GroupToCourse)
class GroupToCourseAdmin(admin.ModelAdmin):
    list_display = ('group', 'course')
    list_filter = ('group', 'course')