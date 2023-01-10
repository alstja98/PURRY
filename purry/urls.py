"""purry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# 라우팅과 관련된 정보가 적힌 곳
urlpatterns = [
    path("admin/", admin.site.urls), #기본 값
    path('app1/',include('app1.urls')) #추가로 넣어줌. http://127.0.0.1/app1/로 접속하면 app1.urls.py로 연결
    #path('read/<id>/', view.read) #id값을 받아서 view.read로 연결 즉, id값이 가변적일 경우에 사용 가능.
]
