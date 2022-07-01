# urls.py
from django.urls import path
from . import views
urlpatterns = [
	path('',views.home,name="home"),
	path('category',views.category,name="category"),
	path('page',views.page,name = "page"),
	path('display',views.display,name="display") 
]


# urls.py:
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
	path('admin/', admin.site.urls),
	path('',include('prob1.urls'))
]

