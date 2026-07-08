from rest_framework import serializers
from .models import Job, Application, Region, District
from users.models import User


# REGION SERIALIZER
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']


# DISTRICT SERIALIZER
class DistrictSerializer(serializers.ModelSerializer):
    region_name = serializers.CharField(source='region.name', read_only=True)

    class Meta:
        model = District
        fields = ['id', 'name', 'region', 'region_name']


# USER SERIALIZER (Simple)
class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'phone_number']


# JOB SERIALIZER
class JobSerializer(serializers.ModelSerializer):
    region_name = serializers.CharField(source='region.name', read_only=True)
    district_name = serializers.CharField(source='district.name', read_only=True)
    employer_name = serializers.CharField(source='employer.first_name', read_only=True, default=None)
    is_expired = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = [
            'id', 'title', 'description', 'job_type',
            'region', 'region_name', 'district', 'district_name',
            'location', 'phone_number', 'salary', 'required_workers',
            'end_date', 'status', 'is_expired',
            'employer', 'employer_name',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'is_expired']
        extra_kwargs = {
            'employer': {'required': False, 'allow_null': True},
        }

    def get_is_expired(self, obj):
        return obj.is_expired()


# APPLICATION SERIALIZER
class ApplicationSerializer(serializers.ModelSerializer):
    worker_name = serializers.CharField(source='worker.first_name', read_only=True)
    job_title = serializers.CharField(source='job.title', read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'worker', 'worker_name', 'job', 'job_title', 'status', 'applied_at']
        read_only_fields = ['applied_at']
