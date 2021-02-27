from  django.urls import path, include
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('accounts/', include('allauth.urls')),

    path('list/',  PostList.as_view(), name='post-list' ),
    path('<slug:slug>/', PostDetail.as_view(), name='post-detail'),
    path('post/new/', PostCreate.as_view(), name='post_new'),
    path('<slug:slug>/edit', PostUpdate.as_view(), name='post-up'),
    path('<slug:slug>/delete', PostDelete.as_view(), name='post-delete'),

]