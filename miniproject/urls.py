from django.contrib import admin
from django.urls import path
from miniproject import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('hotel/', views.hotel, name='hotel'),
    path('product/', views.product, name='product')
]
