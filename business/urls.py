from django.urls import path
from .views import *

urlpatterns = [
    path('', business_list_view, name="business-list"),
    path('create', business_create_view, name="business-create"),
    path('<int:id>/employees', business_employees_view, name="business-employees"),
    path('<int:id>/edit', business_edit_view, name="business-edit"),
    path('<int:id>/delete', business_delete_view, name="business-delete"),
]
