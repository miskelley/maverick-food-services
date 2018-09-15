from django.conf.urls import url
from . import views
from django.urls import path


app_name = 'crm'
urlpatterns = [

    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/create/', views.customer_new, name='customer_new'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('service_list', views.service_list, name='service_list'),
    path('service/create/', views.service_new, name='service_new'),
    path('service/<int:pk>/edit/', views.service_edit, name='service_edit'),
    path('service/<int:pk>/delete/', views.service_delete, name='service_delete'),
    path('product_list', views.product_list, name='product_list'),
    path('product/create/', views.product_new, name='product_new'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('customer/<int:pk>/summary/', views.summary, name='summary'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^password_reset_complete/$', views.password_reset_complete, name='password_reset_complete'),
    url(r'^password_reset_confirm/$', views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password_reset_done/$', views.password_reset_done, name='password_reset_done'),
    url(r'^password_reset_email/$', views.password_reset_email, name='password_reset_email'),
    url(r'^password_reset_form/$', views.password_reset_form, name='password_reset_form'),

]

