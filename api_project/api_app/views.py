from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

class StudentListView(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        class_filter = self.request.query_params.get('class', None)
        data_fields = self.request.query_params.get('data', None)

        queryset = Student.objects.all()

        if class_filter:
            queryset = queryset.filter(class_level=class_filter)

        if data_fields:
            fields = [field.strip() for field in data_fields.split(',')]
            self.serializer_class.Meta.fields = fields

        return queryset.order_by('-total_score')
