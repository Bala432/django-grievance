from django.urls import path
from app import views

appname = "app"

urlpatterns = [

    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='logout'),
    path('post/new/',views.CreatePostView.as_view(),name='post_new'),
    path('post_list/',views.PostListView.as_view(),name='post_list'),
    path('post_list/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('thankyou/',views.thankYou,name='thankyou'),
    path('home/',views.home,name='home'),
    path('publish/new/',views.CreatePublishView.as_view(),name='publish_new'),
    path('publish_list/',views.PublishListView.as_view(),name='publish_list'),
    path('publish_list/<int:pk>/',views.PublishDetailView.as_view(),name='publish_detail'),
    path('thanks/',views.thanks,name='thanks'),

    path('super_post_list/',views.SuperPostListView.as_view(),name='super_post_list'),
    path('super_post_list/<int:pk>/',views.SuperPostDetailView.as_view(),name='super_post_detail'),

    path('user_post_list/',views.UserPostListView.as_view(),name="user_post_list"),
    path('user_post_list/<int:pk>/',views.UserPostDetailView.as_view(),name="user_post_detail"),
    #path('post_list/<int:pk>/post_delete/', views.PostDeleteView.as_view(), name="post_delete"),
    #path('post_list/<int:pk>/posts_delete/',views.posts_delete_view,name="post_delete")
]