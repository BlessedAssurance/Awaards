from django.urls import path
from . import views
from .views import PostListView,PostDetailView,SignUpView
from django.conf import settings


urlpatterns = [

path('signup/', SignUpView.as_view(), name='signup'),

]