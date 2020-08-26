from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSeralizers, UserSerializer
from .models import Task
from rest_framework import filters 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView


class TaskViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)

    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = TaskSeralizers

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('completed',)  # http://127.0.0.1:8000/task/?completed=False
    ordering = ('-date_created',)
    search_fields = ('task_name',)  # http://127.0.0.1:8000/task/?search=Image


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


# username = Kritika_Parmar
# password = CodingisLove

'''
class DueTaskViewSet(viewsets.ModelViewSet):
    
    queryset = Task.objects.all().order_by('-date_created').filter(completed=False)
    serializer_class = TaskSeralizers

class CompletedTaskViewSet(viewsets.ModelViewSet):
    
    queryset = Task.objects.all().order_by('-date_created').filter(completed=True)
    serializer_class = TaskSeralizers

'''

