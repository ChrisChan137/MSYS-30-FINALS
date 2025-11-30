from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
# admin stuff
    path('admin/', admin.site.urls),

# account stuff
    path('', views.login_user, name='login_user'),
    path('signup', views.signup_user, name='signup_user'),
    path('manage_account/<int:pk>/', views.manage_account, name='manage_account'),
    path('change_password/<int:pk>/', views.change_password, name='change_password'),
    path('delete_account/<int:pk>/', views.delete_account, name='delete_account'),

# customer stuff
    path('view_customers',views.view_customers, name='view_customers'),
    path('customers/add/', views.add_customers, name='add_customers'),
    path('delete_customers', views.delete_customers, name='delete_customers'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
]
