from rest_framework import serializers
from .models import FormTemplate, FormField, EmployeeRecord

class FormFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormField
        fields = ['id', 'label', 'field_type', 'required', 'order']

class FormTemplateSerializer(serializers.ModelSerializer):
    fields = FormFieldSerializer(many=True, read_only=True)

    class Meta:
        model = FormTemplate
        fields = ['id', 'name', 'description', 'created_by', 'fields']

class EmployeeRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRecord
        fields = ['id', 'template', 'data', 'created_at']
