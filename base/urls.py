

from django.conf import settings

from django.views.static import serve
from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib import admin
from django.urls import path
admin.autodiscover()
urlpatterns = [
    path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('', views.home, name="home"),
    path('reserve_form/<int:pk>',views.reserve_form,name='reserve-form'),
    path('save_Bookings',views.save_Bookings,name='save-Bookings'),
    path('about/', views.about,name="about"),
    path('more/', views.more, name="more"),
    path('xwing/',views.xwing,name='xwing'),
    path('ships/',views.ships,name = 'ships'),
    path('goods/',views.goods,name = 'goods'),
    path('result1',views.result,name = 'result'),
    path('result1/<int:fromA>/<int:toA>/<str:departure>',views.result),
    path('reserve/<int:pk>',views.reserve,name = 'reserve'),
    path('success/',views.success,name = "success"),
    path('payment_success/',views.payment_success,name = "payment_success"),
    path('select/',views.select,name = "select"),
    path('transport/',views.transport,name = "transport"),


 

    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

