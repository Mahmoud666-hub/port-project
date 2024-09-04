"""
URL configuration for restaurant project.

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

# from django.contrib import admin
# from django.urls import path
# from reservations.views import make_reservation

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/make_reservation/', make_reservation, name='make_reservation'),
# ]
####################
from django.contrib import admin
from django.urls import path
from reservations import views  # Ensure 'reservations' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # This is the root URL
    path('api/make_reservation/', views.make_reservation, name='make_reservation'),
]
