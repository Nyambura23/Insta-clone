from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('',views.index,name = 'index'),
    # path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html')),
    path('post/',views.post, name = 'post'),
    path('user-profile/',views.userprofile, name = 'userprofile'),
    path('update-profile/',views.updateprofile, name = 'updateprofile'),
    path('search/',views.search_results, name='search_results'),
    path('like/<image_id>', views.like, name='like'),
    path('comments/<image_id>', views.comments,name='comments'),
    path('profile/<pk>',views.profile, name = 'profile'),

]