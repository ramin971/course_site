from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('meetups/',views.index,name='home'),
    path('meetups/<slug:slug>',views.meetup_details,name='detail'),
    path('meetups/<slug:slug>/success', views.register_success, name='register_success'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)