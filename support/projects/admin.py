from __future__ import unicode_literals

from django.contrib import admin
from projects.models import Project ,Category ,Comments ,Donation,Rating,CommentReport,ProjectReport,ProjectPicture

# Register your models here.
<<<<<<< HEAD
from .models import  Users,ProjectTag, Project, Comments, CommentReply, Donation, Rating

admin.site.register(ProjectTag)
admin.site.register(Project)
admin.site.register(Comments)
admin.site.register(CommentReply)
admin.site.register(Donation)
admin.site.register(Rating)
admin.site.register(Users)


=======

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Comments)

admin.site.register(Donation)
admin.site.register(Rating)
admin.site.register(CommentReport)
admin.site.register(ProjectReport)
admin.site.register(ProjectPicture)
>>>>>>> 16794e705e0f12119669828544ad2794632db66e
