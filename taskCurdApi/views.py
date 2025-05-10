from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

# Create your views here.
class TaskView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                task = Task.objects.get(pk=pk)
                serializer = TaskSerializer(task)
                return Response(serializer.data)
            except Task.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
   


