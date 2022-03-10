from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from todo.models import ToDo

class ToDoSerializer(ModelSerializer):
    class Meta:
        model=ToDo
        fields=('id','title', 'desc', 'is_complete')
