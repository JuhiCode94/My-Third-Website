"""
URL configuration for JTypingTest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from JTypingTestApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Home page
    path("", views.welcome, name='welcome'),
    path("home", views.home, name='home'),
    path("about", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("english_typing", views.english_typing, name='english_typing'),
    path('english_typing/<str:section>/<str:difficulty>/', views.english_typing, name='english_typing'),
    path("typing_test", views.typing_test, name='typing_test'),   
    path("result/", views.result, name='result'),
]
# Serve static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
