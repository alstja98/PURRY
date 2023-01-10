from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='base'),
    # app1/ 이후 다른 경로로 라우팅필요하면 추가로 쓰면 됨.
    path('openbeta/', views.openbeta, name='openbeta'),

]
