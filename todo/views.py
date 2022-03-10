from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todo.serializers import ToDoSerializer
from rest_framework.permissions import IsAuthenticated
from .models import ToDo
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from todo.pagination import CustomPageNumberPagination

# Create your views here.

class ToDoApiView(ListCreateAPIView):

    serializer_class=ToDoSerializer
    pagination_class=CustomPageNumberPagination
    permission_classes=(IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields= ['id', 'title', 'is_complete']
    search_fields= ['id', 'title','desc' ,'is_complete']
    ordering_fields= ['id', 'title','desc' ,'is_complete']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return ToDo.objects.filter(owner=self.request.user) 


class ToDoDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=ToDoSerializer
    permission_classes=(IsAuthenticated,)
    lookup_field="id"

    def get_queryset(self):
        return ToDo.objects.filter(owner=self.request.user) 

