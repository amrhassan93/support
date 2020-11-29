from django.contrib import admin
from django.urls import path
from . import views
 

urlpatterns = [
    path('' , views.all_project , name='projects'),
    path('create/', views.create),
    path('projectDetails/<int:id>',views.showProject, name="show_project"),
    path('deleteComment/<int:comment_id>/<int:project_id>', views.delete_comment, name="deleteComment"),
    path('editComment/<int:comment_id>/<int:project_id>', views.edit_comment, name="editComment"),
    path('updateComment/<int:comment_id>/<int:project_id>', views.update_comment, name="updateComment"),
    path('reportProject/<int:project_id>', views.report_project, name="reportProject"),
    path('reportComment/<int:comment_id>/<int:project_id>', views.report_comment, name="reportComment"),
    path('<int:id>/comment', views.create_comment, name = 'create_comment'),
    path('<int:id>/donate', views.donate, name = 'donate'),
    path('tags/<slug:slug>', views.show_tag,name='show_tag'),
    path('delete/<int:pk>', views.delete_project, name='project_delete'),



    ]