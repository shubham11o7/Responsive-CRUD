from django.conf.urls import url, include
from django.views.generic import TemplateView

from employe import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^employees/$', views.employee_list, name='employee_list'),
    url(r'^employees/create/$', views.employee_create, name='employee_create'),
    url(r'^employees/(?P<emp_id>\d+)/update/$', views.employee_update, name='employee_update'),
    url(r'^employees/(?P<emp_id>\d+)/delete/$', views.employee_delete, name='employee_delete'),
]
