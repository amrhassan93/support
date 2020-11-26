from django.contrib import admin
from django.urls import path
from my_profile.views import all_project, detail_view,all_donation
# from .views import 
#     PostListView,
#     PostDetailView,
#     PostCreateView,
#     PostUpdateView,
#     PostDeleteView
# 
 
urlpatterns = [
    path('',all_project,name='all_project'),
    #path('', PostListView.as_view(), name='blog-home'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('',all_donation, name="all_donation")
]