from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import Drivers, Schedule
from .serializers import DriversSerializer, ScheduleSerializer



# a view that supports listing all the existing drivers, or creating a new driver.
class DriversList(generics.ListCreateAPIView):
    """
    List all drivers, or create a new driver.
    """
    queryset = Drivers.objects.all()
    serializer_class = DriversSerializer


class DriversDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a driver.
    """
    queryset = Drivers.objects.all()
    serializer_class = DriversSerializer


class ScheduleList(generics.ListCreateAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        queryset = Schedule.objects.all()
        driver_id = self.request.query_params.get('driver_id', None)
        if driver_id is not None:
            queryset = queryset.filter(driver_id=driver_id)
        from_date = self.request.query_params.get('from_date', None)
        # date format: YEAR-MONTH-DAY example: 2020-05-16
        if from_date is not None:
            queryset = queryset.filter(start_time__gte=from_date)
        to_date = self.request.query_params.get('to_date', None)
        if to_date is not None:
            queryset = queryset.filter(start_time__lte=to_date)
        return queryset


    # def get_queryset(self):
    #     return Schedule.objects.annotate(
    #         total_trucks=Count('trucks'),
    #         total_capacity=Sum('trucks__capacity')
    #     )


class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


#
# @api_view(['GET', 'POST'])
# def drivers_list(request, format=None):
#     """
#     List all drivers or create a new driver.
#     """
#     if request.method == 'GET':
#         drivers = Drivers.objects.all()
#         serializer = DriversSerializer(drivers, many=True)
#         #return JsonResponse(serializer.data, safe=False)
#         return Response(serializer.data)  # Renders to content type as requested by the client.
#
#     elif request.method == 'POST':
#         serializer = DriversSerializer(data=request.data) # request.data  # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#     # elif request.method == 'POST':
#     #     data = JSONParser().parse(request)
#     #     serializer = DriversSerializer(data=data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return JsonResponse(serializer.data, status=201)
#     #     return JsonResponse(serializer.errors, status=400)
#
#
# @api_view(['GET', 'POST'])
# def schedule_list(request, format=None):
#     """
#     List schedule or create a new one.
#     """
#     if request.method == 'GET':
#         schedules = Schedule.objects.all()
#         serializer = ScheduleSerializer(schedules, many=True)
#         # return JsonResponse(serializer.data, safe=False)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = ScheduleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     # elif request.method == 'POST':
#     #     data = JSONParser().parse(request)
#     #     serializer = ScheduleSerializer(data=data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return JsonResponse(serializer.data, status=201)
#     #     return JsonResponse(serializer.errors, status=400)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def drivers_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete driver.
#     """
#     try:
#         driver = Drivers.objects.get(pk=pk)
#     except Drivers.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = DriversSerializer(driver)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = DriversSerializer(driver, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         driver.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def schedule_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete schedule.
#     """
#     try:
#         schedule = Schedule.objects.get(pk=pk)
#     except Schedule.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ScheduleSerializer(schedule)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ScheduleSerializer(schedule, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         schedule.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the index.")

