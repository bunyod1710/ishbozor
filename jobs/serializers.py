from rest_framework import serializers
from .models import Job , Application
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id','title','description','job_type','location','salary','status','employer','required_workers','created_at','updated_at']
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id','worker','job','status','applied_at']