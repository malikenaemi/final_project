from django.conf.urls import url
from app1 import views

#TEMPLATE URLS!
app_name = 'app1'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]