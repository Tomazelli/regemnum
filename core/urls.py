from django.urls import path
from django.contrib import admin
from .views import IndexView, Error404View, Error500View, CsvUploadView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('404/', Error404View.as_view(), name='404'),
    path('500/', Error500View.as_view(), name='500'),
    path('admin/', IndexView.as_view(), name='login'),
    path('csv-upload/', CsvUploadView.as_view(), name='csv-upload')
]