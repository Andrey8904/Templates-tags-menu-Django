from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main_app import views

app_name = 'main_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('<path:url>?<str:selected>', views.show_selected, name='select'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)