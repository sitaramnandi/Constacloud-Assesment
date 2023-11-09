from django import forms
from .models import StudentMarkSheet

class MarkSheetForm(forms.ModelForm):
    class Meta:
        model = StudentMarkSheet
        fields = '__all__'
