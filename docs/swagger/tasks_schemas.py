
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Response schemas
task_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
        'title': openapi.Schema(type=openapi.TYPE_STRING),
        'description': openapi.Schema(type=openapi.TYPE_STRING),
        'status': openapi.Schema(type=openapi.TYPE_STRING),
        'created_at': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
    }
)

error_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'message': openapi.Schema(type=openapi.TYPE_STRING),
        'errors': openapi.Schema(type=openapi.TYPE_OBJECT),
    }
)

# Common parameters
task_id_parameter = openapi.Parameter(
    'pk',
    openapi.IN_PATH,
    description="Task ID",
    type=openapi.TYPE_INTEGER,
    required=True
)


# Swagger decorators
def swagger_list_tasks():
    return swagger_auto_schema(
        operation_summary="List all tasks",
        operation_description="Retrieve a list of all tasks",
        responses={200: task_response_schema},
        tags=['Tasks']
    )


def swagger_create_task():
    return swagger_auto_schema(
        operation_summary="Create a new task",
        operation_description="Create a new task",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING, example="demo task 1"),
                'description': openapi.Schema(type=openapi.TYPE_STRING, example="this is demo task one ..."),
                'due_date': openapi.Schema(type=openapi.TYPE_STRING, format="date", example="2024-05-07"),
                'status': openapi.Schema(type=openapi.TYPE_STRING, example="to do"),
                'estimated_time': openapi.Schema(type=openapi.TYPE_STRING, example="2.00"),
            },
            required=['title']
        ),
        responses={
            201: task_response_schema,
            400: error_response_schema
        },
        tags=['Tasks']
    )


def swagger_get_task():
    return swagger_auto_schema(
        operation_summary="Get a specific task",
        manual_parameters=[task_id_parameter],
        responses={200: task_response_schema, 404: error_response_schema},
        tags=['Tasks']
    )


def swagger_update_task():
    return swagger_auto_schema(
        operation_summary="Update a task",
        manual_parameters=[task_id_parameter],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING),
                'description': openapi.Schema(type=openapi.TYPE_STRING),
                'status': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={200: task_response_schema, 404: error_response_schema},
        tags=['Tasks']
    )


def swagger_delete_task():
    return swagger_auto_schema(
        operation_summary="Delete a task",
        manual_parameters=[task_id_parameter],
        responses={200: 'Task deleted successfully', 404: error_response_schema},
        tags=['Tasks']
    )
