from django.contrib import admin
from .models import News,Comments,Images,Teachers,Teachers_situation,subjects,ACCEPTANCE,Achievements,Boss
# Register your models here.



admin.site.register(ACCEPTANCE)


@admin.register(Boss)
class BossAdmin(admin.ModelAdmin):
    list_display = ('fullname','slug')
    prepopulated_fields = {"slug": ("fullname",)}

@admin.register(Achievements)
class AchievementsAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {"slug": ("name",)}

@admin.register(subjects)
class subjectsAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Comments)
admin.site.register(Images)
admin.site.register(Teachers_situation)
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    '''Admin View for News'''

    list_display = ('title','slug')
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    '''Admin View for News'''

    list_display = ('fullname','slug')
    prepopulated_fields = {"slug": ("fullname",)}