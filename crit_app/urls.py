from django.urls import path
from . import views

# app_name = 'crit_app' # for namespacing
urlpatterns = [
    path('party/', views.PartyList.as_view()),
    path('party/<int:pk>/', views.PartyDetail.as_view()),
    path('members/', views.MemberList.as_view()),
    path('member/<int:pk>/', views.MemberDetail.as_view()),
]