from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='groups'),
    path('create', views.create, name='group-create'),
    path('<code>', views.detail, name='group-detail'),
    path('<code>/edit', views.edit, name='group-edit'),
    path('<code>/remove', views.remove, name='group-remove'),
    path('<code>/subscribe', views.subscribe, name='group-subscribe'),
    path('<code>/unsubscribe', views.unsubscribe, name='group-unsubscribe'),
    path('<code>/claim-admin', views.claim_admin, name='group-claim-admin'),
]
