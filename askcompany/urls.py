"""askcompany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

# settting.py 에 접근하려면..
from django.conf import settings

# 정적 파일에 접근하려면...
from django.conf.urls.static import static

import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__', include(debug_toolbar.urls)),
    path('instagram/', include('instagram.urls')),
    path('accounts/', include('accounts.urls')),

]

# settings 에서 DEBUG 가 True 일 경우 (안써도 되긴 함. 명시적으로 쓰기 위한것.)
# 정적 파일에 접근하기 위하여 urlpatterns 에 static() 함수를 통한 정적 리소스 URL 을 등록해준다. (이 때 DEBUG 가 False 인 경우는 빈 List 를 반환해준다.)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)