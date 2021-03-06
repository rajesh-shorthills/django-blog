"""try_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,re_path,include
from blog.views import (
    blog_post_create_view
    )

from .views import (
    home_page,
    contact_page,
    about_page,
    example_page
)

app_name = "test_app"

urlpatterns = [
    path('', home_page),

    path('blog-new',blog_post_create_view, name="blog_post"),
    path('blog/',include("blog.urls")),
    # re_path(r'^pages?/$', about_page),## This one line render 'page' por 'pages' to about_us view
    # path('page', about_page),
    # path('pages', about_page),
    # re_path(r'^about/$', about_page),
    path('admin/', admin.site.urls),
    path('about/', about_page),
    path('example/', example_page),
    path('contact/', contact_page),
    # path('blog/<str:slug>', blog_post_detail_page),# Use blog slug to render
    # path('blog/<int:post_id>', blog_post_detail_page),# Note: in blog_post_detail_page view function parameter name must be post_id
    # re_path(r'^blog/(?P<post_id>\d+)/$', blog_post_detail_page),
    
    
    
]
