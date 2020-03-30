from django.urls import path


from user.views import RegisterView

from user.views import Login

from user.views import ProfileUpdate

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth-register'),
    path('login/', Login.as_view(), name='auth-login'),
    path('profile/', ProfileUpdate.as_view(), name='login-profile'),
]
