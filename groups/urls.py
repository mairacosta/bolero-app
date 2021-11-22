from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='groups'),
    path('create/', views.create, name='group-create'),
    path('<code>', views.detail, name='group-detail')
]
