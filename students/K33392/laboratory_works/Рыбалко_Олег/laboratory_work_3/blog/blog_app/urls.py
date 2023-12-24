from blog_app.views import PostViewSet, UserViewSet, CommentViewSet, FollowViewSet, UsernameViewSet, PostCommentsViewSet
from rest_framework.routers import DefaultRouter
from djoser.views import UserViewSet

r = DefaultRouter()
r.register('users', UserViewSet)
r.register('posts', PostViewSet)
r.register('comments', CommentViewSet)
r.register('follows', FollowViewSet)
r.register('username', UsernameViewSet, basename="username")
r.register('post_comments', PostCommentsViewSet, basename="post_comments")
urlpatterns = r.urls