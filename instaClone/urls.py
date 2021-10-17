from django.urls import path, include
from . import views
from .views import PostLikeToggle, PostLikeAPIToggle
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    path('follow/<to_follow>', views.follow, name='follow'),
    path('like', views.like_post, name='like_post'),
    path('search/', views.search_profile, name='search'),
    path('post/<id>/like', PostLikeToggle.as_view(), name='liked'),
    path('api/post/<id>/like', PostLikeAPIToggle.as_view(), name='liked-api'),
    path('post/<id>', views.post_comment, name='comment'),
    path('post/<id>', views.post_comment, name='comment'),

]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)