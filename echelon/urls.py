"""
URL configuration for echelon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path, re_path
from project_management import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project_management/', include('project_management.urls')),
    path('api/', include('project_management.api_urls')),
    re_path(r'^manifest.json$', TemplateView.as_view(template_name='manifest.json', content_type='application/json')),
    re_path(r'^favicon.ico$', TemplateView.as_view(template_name='favicon.ico', content_type='image/vnd.microsoft.icon')),
    re_path(r'^logo192.png$', TemplateView.as_view(template_name="logo192.png", content_type='image/png')),
    re_path(r'^logo512.png$', TemplateView.as_view(template_name="logo512.png", content_type="image/png")),
    re_path(r'^(?:.*)/?$', TemplateView.as_view(template_name='index.html')),

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

