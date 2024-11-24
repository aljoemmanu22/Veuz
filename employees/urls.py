from django.urls import path
from .views import FormTemplateView, EmployeeRecordView

urlpatterns = [
    path('templates/', FormTemplateView.as_view(), name='form_templates'),
    path('records/', EmployeeRecordView.as_view(), name='employee_records'),
    path('records/<int:pk>/', EmployeeRecordView.as_view(), name='employee_record_detail'),
]
