from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import FormTemplate, FormField, EmployeeRecord
from .serializers import FormTemplateSerializer, FormFieldSerializer, EmployeeRecordSerializer

class FormTemplateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        name = request.data.get('name')
        description = request.data.get('description')
        fields = request.data.get('fields', [])

        if FormTemplate.objects.filter(name=name).exists():
            return Response({'error': 'FormTemplate with this name already exists'}, status=status.HTTP_400_BAD_REQUEST)

        template = FormTemplate.objects.create(name=name, description=description, created_by=request.user)

        for field in fields:
            FormField.objects.create(
                template=template,
                label=field['label'],
                field_type=field['field_type'],
                required=field.get('required', False),
                order=field.get('order', 0)
            )

        return Response(FormTemplateSerializer(template).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        templates = FormTemplate.objects.filter(created_by=request.user)
        serializer = FormTemplateSerializer(templates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EmployeeRecordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        template_id = request.data.get('template_id')
        data = request.data.get('data', {})

        try:
            template = FormTemplate.objects.get(id=template_id, created_by=request.user)
        except FormTemplate.DoesNotExist:
            return Response({'error': 'Template not found'}, status=status.HTTP_404_NOT_FOUND)

        record = EmployeeRecord.objects.create(template=template, data=data)
        return Response(EmployeeRecordSerializer(record).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        records = EmployeeRecord.objects.all()
        serializer = EmployeeRecordSerializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            record = EmployeeRecord.objects.get(pk=pk, template__created_by=request.user)
        except EmployeeRecord.DoesNotExist:
            return Response({'error': 'Employee record not found'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.get('data', {})
        record.data = data
        record.save()
        return Response(EmployeeRecordSerializer(record).data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        try:
            record = EmployeeRecord.objects.get(pk=pk, template__created_by=request.user)
        except EmployeeRecord.DoesNotExist:
            return Response({'error': 'Employee record not found'}, status=status.HTTP_404_NOT_FOUND)

        record.delete()
        return Response({'message': 'Employee record deleted successfully'}, status=status.HTTP_200_OK)


