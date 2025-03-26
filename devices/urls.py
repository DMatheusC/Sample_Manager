from django.urls import path
from devices.views import login_view, logout_view, device_list, register_device, register_user

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("device_list/", device_list, name="device_list"),
    path("register_device/", register_device, name="register_device"),
    path("register_user/", register_user, name="register_user"),
    path("", login_view, name="login"),
]



