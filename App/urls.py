from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.PostsListCreate.as_view(), name='post-view-create'),
    path("post/<int:pk>/", views.PostRetrieveUpdateDestroy.as_view(), name="update")
]
