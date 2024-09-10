from django.urls import path
from . import views

urlpatterns = [
    path('', UserCreateView, as_view()),
    path('login/', login, name='login'),
    path('<str:username>/', profile, name='profile'),
    path('signup/', signup, name='signup')
    path('<str:username>/', UserProfileView, as_view()),
]
