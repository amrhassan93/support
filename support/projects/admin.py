from django.contrib import admin

# Register your models here.
from .models import  Users,ProjectTag, Project, Comments, CommentReply, Donation, Rating

admin.site.register(ProjectTag)
admin.site.register(Project)
admin.site.register(Comments)
admin.site.register(CommentReply)
admin.site.register(Donation)
admin.site.register(Rating)
admin.site.register(Users)


