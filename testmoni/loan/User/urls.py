# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.loan_form, name='loan'),
    url(r'^administrador/$', views.loan_list, name='loan-list'),
    url(r'^administrador/editar/(?P<id>\d+)/$', views.loan_edit, name="loan-edit"),
    url(r'^administrador/borrar/(?P<id>\d+)/$', views.loan_remove, name="loan-remove"),
    url(r'^administrador/detalles/(?P<id>\d+)/$', views.loan_details,
        name="loan-details")
]