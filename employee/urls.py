from django.urls import path
from .views import *

urlpatterns = [
    path('login', employee_login_view, name="login"),
    path('register', employee_register_view, name="register"),
    path('logout', employee_logout_view, name="logout"),

    path('<int:id>/edit', employee_edit_view, name="employee-edit"),
    path('<int:id>/delete', employee_delete_view, name="employee-delete"),
]
