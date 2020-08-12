
from django.urls import path
from .views import Home,CreateView,UpdateView,DeleteView,search

urlpatterns = [

    path('',Home),
    path('create/',CreateView),
    path('update/<emp_id>',UpdateView),
    path('delete/<emp_id>',DeleteView),
    path('search/', search, name="search"),
    # url(r'^'update/(?P<emp_id>\d+)/$',UpdateView)

]