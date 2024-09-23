"""
URL configuration for social_network project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# social_network/urls.py
from django.urls import path
from users.views import SignupView, LoginView,UserSearchView
from django.urls import include
from users.views import BlockUserView,UserActivityView

urlpatterns = [
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/friends/', include('friends.urls')),
    path('api/users/search/', UserSearchView.as_view(), name='user-search'),
    path('api/users/block/', BlockUserView.as_view(), name='block-user'),
    path('api/users/activity/', UserActivityView.as_view(), name='user-activity'),
]

