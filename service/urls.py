from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('', views.index, name='index'),
	path('result/<int:pk>/', views.identification_result, name='identification_result'),
	path('delete/<int:pk>',views.delete,name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)