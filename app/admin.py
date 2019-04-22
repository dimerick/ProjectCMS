from django.contrib import admin

from .models import Slider, Slide, Partner, TeamMember, Activity, Project, Group

# Register your models here.
class SliderAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

class SlideAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'is_active', 'position', 'slider')

	fieldsets = (
        ('Title', {
            'fields': ('title', ('top_title', 'left_title'), ('size_title', 'color_title'))
        }),
        ('Description', {
            'fields': ('text', ('top_text', 'left_text'), ('size_text', 'color_text'))
        }),
        ('Image', {
            'fields': (['image'])
        }),
        ('Button', {
            'fields': ('show_button', ('text_button', 'url_button', 'color_button'), ('top_button', 'left_button'))
        }),
        ('General Options', {
            'fields': ('slider', 'is_active', 'position')
        })
    )

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'position')
	# fields = ('slider', 'image', 'title', ('top_title', 'left_title', 'size_title'), 'text', 
	# 	('top_text', 'left_text', 'size_text'), ('show_button', 'text_button', 'url_button'), ('top_button', 
	# 		'left_button'), 'is_active', 'position')

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'date')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'position')

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'email')

admin.site.register(Slider, SliderAdmin)
admin.site.register(Slide, SlideAdmin)
admin.site.register(Partner)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Group, GroupAdmin)
