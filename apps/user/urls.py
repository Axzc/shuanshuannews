from apps.user.views import SignupView, ActiveView, LoginView, UserCenterView, LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', SignupView.as_view(), name='signup'),
    re_path('active/(?P<token>.*)', ActiveView.as_view(), name='active'),  # 用户激活
    # path('active', ActiveView.as_view(), name='active'),  # 用户激活

    path('homepage', login_required(UserCenterView.as_view()), name='usercenter')
]
