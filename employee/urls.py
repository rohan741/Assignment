from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('index', views.index, name = 'index'),
    path('upload/', views.upload, name = 'add-employee'),
    path('update/<int:employee_id>', views.update_employee),
    path('delete/<int:employee_id>', views.delete_employee)
]

