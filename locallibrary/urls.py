"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

# Use include() to add paths from the catalog application
from django.urls import include
# Use RedirectView to  takes the new relative URL to redirect to (/catalog/) as its first 
# argument when the URL pattern specified in the path() function is matched (the root URL, in this case).
from django.views.generic import RedirectView

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
]
# add catalog url pattern
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

# Add URL maps to redirect the base URL to our application
urlpatterns += [
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]

#enable the serving of static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
