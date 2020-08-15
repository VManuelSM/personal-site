from django.contrib import admin
from .models import Project, Technology

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


class TechnologyAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology, ProjectAdmin)
