from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from docs.swagger.tasks_schemas import *


class TaskCreateView(APIView):
    # @swagger_auto_schema(
    #     operation_summary="Get all tasks",
    #     operation_description="Retrieve a list of all tasks",
    #     responses={
    #         200: TaskSerializer(many=True),
    #     },
    #     #tags=['Tasks']
    # )

    @swagger_list_tasks()
    def get(self, request):
        try:
            tasks = Task.objects.all()
            if not tasks:
                return Response({
                    "message": "No tasks found"
                }, status=status.HTTP_404_NOT_FOUND)
            
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({
                "message": "An error occurred while retrieving tasks",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # @swagger_auto_schema(
    #     operation_description="Create a new task",
    #     request_body=TaskSerializer,
    #     responses={
    #         201: TaskSerializer,
    #         400: "Bad Request"
    #     }
    # )
    @swagger_create_task()
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

class TaskDetailView(APIView):

    @swagger_auto_schema(
        operation_description="Retrieve all tasks or a specific task by ID",
        # manual_parameters=[
        #     openapi.Parameter('pk', openapi.IN_PATH, description="Task ID", type=openapi.TYPE_INTEGER)
        # ],
        responses={
            200: TaskSerializer(many=True),
            404: "Task not found"
        }
    )
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


    @swagger_auto_schema(
        operation_description="Update an existing task",
        request_body=TaskSerializer,
        responses={
            202: TaskSerializer,
            404: "Task not found",
            400: "Bad Request"
        }
    )
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
    
    
    @swagger_auto_schema(
        operation_description="Delete a specific task by ID",
        responses={
            200: "Task deleted successfully",
            404: "Task not found"
        }
    )
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


