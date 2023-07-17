from django.contrib import admin
from .models import Teacher, Course, Curriculum, Category, Software, Event, Partner, Testimonial, Member
# Register your models here.

class CurriculumInLine(admin.TabularInline):
    model = Curriculum
    extra = 5

class CourseAdmin(admin.ModelAdmin):
    inlines = [CurriculumInLine]
    list_filter = ["category"]

admin.site.register(Curriculum)  
admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher)
admin.site.register(Category)
admin.site.register(Software)
admin.site.register(Event)
admin.site.register(Partner)
admin.site.register(Testimonial)
admin.site.register(Member)
    
