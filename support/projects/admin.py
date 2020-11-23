from __future__ import unicode_literals

from django.contrib import admin
from projects.models import Project ,Category ,Comments ,Donation,Rating,CommentReport,ProjectReport,ProjectPicture

# Register your models here.

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Comments)

admin.site.register(Donation)
admin.site.register(Rating)
admin.site.register(CommentReport)
admin.site.register(ProjectReport)
admin.site.register(ProjectPicture)
