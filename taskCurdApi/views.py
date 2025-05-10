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
                return Response({
                    "message": "Task not found"
                }, status=status.HTTP_404_NOT_FOUND)
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Task created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Task creation failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({
                "message": "Task not found"
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Task updated successfully",
                "data": serializer.data
            }, status=status.HTTP_202_ACCEPTED)
        return Response({
            "message": "Task update failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({
                "message": "Task not found"
            }, status=status.HTTP_404_NOT_FOUND)
        
        task.delete()
        return Response({
            "message": "Task deleted successfully"
        }, status=status.HTTP_200_OK)


