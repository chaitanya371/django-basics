# urls.py
from django.urls import path
from . import views
urlpatterns = [
	path('',views.home,name="home"),
	path('register',views.register,name="register")
]


# urls.py
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
	path('admin/', admin.site.urls),
	path('',include('prob1.urls')),
]


# urls.py
from django.conf.urls import url 
from . import views 
urlpatterns = [ 
	url(r'^connection/',views.formView, name = 'formView'), 
	url(r'^login/', views.login, name = 'login'), 
	url(r'^logout/', views.logout, name = 'logout'), 
]

