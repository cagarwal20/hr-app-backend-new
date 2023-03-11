from .models import Staff,AttendanceLogs
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from staff.serializers import StaffSerializer
import datetime
from django.utils.timezone import localtime
import pytz
from django.contrib.auth import authenticate,login
from .forms import RegisterForm
from django.db.models import F

@api_view(['GET'])
def get_staff(request):
    object = Staff.objects.all()
    serialized_data = StaffSerializer(object,many=True)
    return Response({"data":serialized_data.data},status=200)

@api_view(['GET'])
def get_list_delete(request):
    data = Staff.objects.all().annotate(key=F('id'),value=F('first_name')).values('key','value')
    return Response({"data":data},status=200)

@api_view(['PATCH'])
def intime(request,id):
    try:
        object = Staff.objects.get(id=id)
        request.data["in_time"] = datetime.datetime.now()
        request.data["current_status"] = True
        serializer = StaffSerializer(object, data=request.data, partial=True)
        if serializer.is_valid():
            time_entry = serializer.save()
            return Response({"response":"updated successfully"},status=201) 
        return Response({"response":"invalid serialization"},status=400)
    except Exception as e:
        return Response({"response":str(e)},status=400)
    
@api_view(['PATCH'])
def outtime(request,id):
    try:
        object = Staff.objects.get(id=id)
        if object.in_time is not None:
            request.data["current_status"] = False
            request.data['in_time'] = None
            time_elapsed= datetime.datetime.now() - object.in_time.replace(tzinfo=None)
            serializer = StaffSerializer(object, data=request.data, partial=True)
            if serializer.is_valid():
                time_entry = serializer.save()
                return Response({"response":"updated successfully" , "time_elapsed":round(time_elapsed.total_seconds()/60)},status=201) 
            return Response({"response":"invalid serialization"},status=400)
        else:
            return Response({"response":"check in again"},status=200)
            
    except Exception as e:
        return Response({"response":str(e)},status=400)
    
@api_view(['POST'])
def login(request):
    if request.method=="POST":
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request,username=username,password=password)
        if user is None:
            return Response({"response":"no login access"},status=200)
        else:
            return Response({"response":"login success"},status=200)
        
@api_view(['DELETE'])
def delete_staff(request):
    id = request.data['id']
    object = Staff.objects.get(id=id)
    try:
        object.delete()
        return Response({"response":"deleted"},status=200)
    except Exception as e:
        return Response({"response":str(e)},status=400)

# @api_view(['POST'])
# def signup(request):
#     if request.method=="POST":



@api_view(['POST'])
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return Response({"response":"successful"},status=200)
    return Response({"response":"not able to register"},status=200)

@api_view(['PATCH'])
def edit_info(request,id):
    object = Staff.objects.get(id=id)        
    serializer = StaffSerializer(object,data=request.data,partial=True)   
    if serializer.is_valid():
        serializer.save()
        return Response({"response":"data updated succesfully"},status=200)
    else:
        return Response({"response":"wrong format"},status=200)
    
@api_view(['POST'])
def create_staff(request):
    first_name = request.data["first_name"]
    last_name = request.data["last_name"]
    try:
        data = Staff.objects.create(
            first_name=first_name,
            last_name=last_name
                    )
        serializer = StaffSerializer(data)
        return Response({"data":serializer.data},status=200)
    except Exception as e:
        return Response({"error":str(e)},status=400)
    

#attendance logging table where all the out time will be logged and total attendance of the month will queried
#I have to make a model for it.

@api_view(['GET'])
def get_attendance(request,id):
    month = request.data['month']
    try:
        count = AttendanceLogs.objects.filter(staff__id=id,date__range=["2023-{}-01".format(month), "2023-{}-20".format(month)]).count()#,in_time__month=month,out_time__month=month).count()
        return Response({"attendance":count},status=200)
    except Exception as e:
        return Response({"error":str(e)},status=200)
    
@api_view(['POST'])
def get_single_record(request):
    id = request.data['id']
    try:
        object = Staff.objects.get(id=id)
        s_data = StaffSerializer(object)
        data=s_data.data
        return Response({"data":data},status=200)
    except Exception as e:
        return Response({"error":str(e)},status=200)

@api_view(['PATCH'])
def settle_money(request,id):
    money = request.data['money']
    if money==0:
        try:
            object = Staff.objects.get(id=id)
            s_data = StaffSerializer(object,data=request.data,partial=True)
            if s_data.is_valid():
                s_data.save()
                return Response({"data":s_data.data},status=200)
        except Exception as e:
            return Response({"error":str(e)},status=200)
    
    try:
        object = Staff.objects.get(id=id)
        s_data = StaffSerializer(object)
        request.data['money'] = int(request.data['money'])
        request.data['money']+=s_data.data['money']
        s_data = StaffSerializer(object,data=request.data,partial=True)
        if s_data.is_valid():
            s_data.save()
            return Response({"data":s_data.data},status=200)
    except Exception as e:
        return Response({"error":str(e)},status=200)