
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("category/<slug:category_slug>/", views.home,name="category_wise_post"),
    path("people/", include("people.urls")),
    path("car/", include("car.urls")),
]
urlpatterns += staticfiles_urlpatterns()