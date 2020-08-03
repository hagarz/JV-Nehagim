from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import Drivers, Schedule
from .serializers import DriversSerializer, ScheduleSerializer



class DriversList(generics.ListCreateAPIView):
    queryset = Drivers.objects.all()
    serializer_class = DriversSerializer


class DriversDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drivers.objects.all()
    serializer_class = DriversSerializer


class ScheduleList(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


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

