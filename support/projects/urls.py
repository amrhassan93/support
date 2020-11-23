from django.contrib import admin
from django.urls import path
from . import views
 

urlpatterns = [
    path('' , views.all_project),
    path('create/', views.create),
    # path('projectDetails/<int:id>',views.showProject,name="show_proj"),
    # path('showCategory/<int:id>',views.showCategoryProjects ,name="show_cate"),
    # path('<int:id>/comment', views.create_comment, name = 'create_comment'),
    # path('<int:id>/report_pro', views.report_project, name = 'report_project'),
    # path('<int:id>/report_com', views.report_comment, name = 'report_comment'),
    # path('<int:id>/donate', views.donate, name = 'donate'),
    # path('tags/<slug:slug>', views.show_tag,name='show_tag'),
    # path('<int:id>/rate/<int:value>', views.rate_project, name='rate_project'),
    # path('<int:id>/delete', views.delete_project, name='delete_project')
]