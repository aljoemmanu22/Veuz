from django.contrib import admin
from .models import FormField, FormTemplate, EmployeeRecord

# Register your models here.
admin.site.register(FormTemplate)
admin.site.register(FormField)
admin.site.register(EmployeeRecord)