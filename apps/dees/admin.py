from django.contrib import admin
from apps.dees.models import Project, Task, Skill, ResourceRequest

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Skill)
admin.site.register(ResourceRequest)
