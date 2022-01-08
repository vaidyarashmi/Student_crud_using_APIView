from django.core.exceptions import ValidationError
from django.db.models import fields
from rest_framework import serializers
from testapp.models import Student

class StudentSerializers(serializers.ModelSerializer):
    def validate(self,data):
        age=data.get('age')
        if age < 9:
            raise ValidationError('Age must be greater than nine year old.')
        return data
    
    class Meta:
        model=Student
        fields='__all__'