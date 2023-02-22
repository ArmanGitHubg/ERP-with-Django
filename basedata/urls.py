from django.urls import path
from . import views

urlpatterns = [
    path(r"dataimport/(?P<object_id>\d+)/action",views.action_import, name='action_import'),
]
