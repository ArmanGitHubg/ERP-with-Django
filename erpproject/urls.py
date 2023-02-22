from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
#from erpproject.settings import settings
from erpproject.views import home
from workflow.views import start, approve, restart
import invent.urls
import basedata.urls
import selfhelp.urls
import erpproject.views

urlpatterns = [
    path(r'^$', home, name='home'),
    path(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/start", start,name='start'),
    path(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/approve/(?P<operation>\d+)", approve, name='approve'),
    path(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/restart/(?P<instance>\d+)", restart, name='restart'),
    path(r'^admin/', include(admin.site.urls)),
    path(r'^admin/invent/', include('invent.urls')),
    path(r'^admin/basedata/', include('basedata.urls')),
    path(r'^admin/selfhelp/', include('selfhelp.urls')),
]
urlpatterns += static.static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static.static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
