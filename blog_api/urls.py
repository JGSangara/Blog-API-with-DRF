from django.urls import path

from .views import CustomUserCreate, LoginView, PostDetail, PostList

app_name = "blog_api"

urlpatterns = [
    path("posts/", PostList.as_view(), name="listcreate"),
    path("posts/<int:pk>/", PostDetail.as_view(), name="detailcreate"),
    path("users/register/", CustomUserCreate.as_view(), name="register"),
    path("users/login/", LoginView.as_view(), name="login"),
]
