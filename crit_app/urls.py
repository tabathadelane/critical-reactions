from django.urls import path
from . import views

app_name = 'crit_app' # for namespacing
urlpatterns = [
    path('', views.<viewname>, name='<viewname>')
]