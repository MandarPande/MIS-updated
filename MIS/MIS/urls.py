from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login),
    path('home/',views.menu),
    path('achievements/',views.home),
    path('student_details/',views.details)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

