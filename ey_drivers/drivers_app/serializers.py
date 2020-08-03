from rest_framework import serializers
from .models import Drivers, Schedule

class DriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields = ['driver_id', 'driver_name', 'is_active']

    # driver_id = serializers.IntegerField(read_only=True)
    # driver_name = serializers.CharField(required=True, allow_blank=False, max_length=32)
    # is_active = serializers.BooleanField(required=True)

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Driver` instance, given the validated data.
    #     """
    #     return Drivers.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing instance, given the validated data.
    #     """
    #     instance.driver_id = validated_data.get('driver_id', instance.driver_id)
    #     instance.driver_name = validated_data.get('driver_name', instance.driver_name)
    #     instance.is_active = validated_data.get('is_active', instance.is_active)
    #     instance.save()
    #     return instance



class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['driver_id', 'start_time', 'end_time']

    # driver_id = serializers.IntegerField(read_only=True)
    # start_time = serializers.DateTimeField(required=True)
    # end_time = serializers.DateTimeField(required=True)
    #
    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Schedule.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.driver_id = validated_data.get('driver_id', instance.driver_id)
    #     instance.start_time = validated_data.get('start_time', instance.start_time)
    #     instance.end_time = validated_data.get('end_time', instance.end_time)
    #     instance.save()
    #     return instance


