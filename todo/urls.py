from todo.views import  ToDoApiView, ToDoDetailApiView
from django.urls import path


urlpatterns = [

    path('' , ToDoApiView.as_view(), name='todo'),
    path('<int:id>' , ToDoDetailApiView.as_view(), name='tododetail'),
    

]
