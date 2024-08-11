from django.urls import path

from users.views import Register, Login, home, logout_view

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('home/', home, name='userhome'),
    path('logout', logout_view, name='logout')
]

