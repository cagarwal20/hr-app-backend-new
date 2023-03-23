from rest_framework import serializers
from .models import Staff,MoneyLogs
from datetime import datetime
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class MoneyLogsSerializer(serializers.ModelSerializer):
    staff_name =  serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    def get_staff_name(self,obj):
        data = Staff.objects.get(id=obj.staff.id)
        serialized_data = StaffSerializer(data)
        return serialized_data.data['first_name']+ " " + serialized_data.data['last_name']
    
    def get_date(self,obj):
        datetime_obj = obj.time.strftime("%d-%m-%Y")
        return datetime_obj
    class Meta:
        model=MoneyLogs
        fields='__all__'