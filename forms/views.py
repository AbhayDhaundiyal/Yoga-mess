import datetime
from dateutil.relativedelta import relativedelta
from calendar import monthrange
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import User
from django.http import JsonResponse
from django.utils import dateparse, timezone
import simplejson as json
from django.core import serializers

def calculate_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
def calculate_validity(payment):
    today = datetime.date.today()
    res = today + relativedelta(day=31)
    return (res - payment).days
def signup(request):
    new_user = json.loads(request.body)
    try:
        check = User.objects.get(Email = new_user['Email'])
    except User.DoesNotExist:
        check = None
        
    if check != None:
        return JsonResponse({"message" : "User already exists"}, status=401)
    DOB = datetime.datetime.strptime(new_user["DOB"], "%d/%m/%Y").date()
    age = calculate_age(DOB)
    if age < 18 or age > 65:
        return JsonResponse({"message" : "Your age should be between 18-65"}, status=401)
    std = User(Name = new_user['Name'], 
    Email = new_user['Email'],
    Password = new_user["Password"],
    DOB=DOB)
    std.save()
    return JsonResponse({'Name': new_user['Name'], "status":"200"})


def login(request):
    data = json.loads(request.body)
    try:
        std = User.objects.get(Email = data['Email'], Password = data['Password'])
    except User.DoesNotExist:
        std = None
    if std == None:
        return JsonResponse(data={"status": 401}, status=401)
    dict = {}
    dict['Email'] = std.Email
    dict['Name'] = std.Name
    dict['Batch'] = std.Batch
    # send = serializers.serialize("json", User.objects.filter(Email = data['Email'], Password = data['Password']))
    # send["Validity"] = 
    # print(datetime.date.today())
    # print(std.Payment_Date)
    valid = calculate_validity(std.Payment_Date)
    if std.Payment_Date.month != datetime.date.today().month or valid >= 31:
        valid = -1
    dict['Validity'] = valid
    return HttpResponse(json.dumps(dict), content_type='application/json')

def update(request):
    data = json.loads(request.body)
    try:
        usr = User.objects.get(Email = data['Email'])
    except User.DoesNotExist:
        return HttpResponse(status=401)
    usr.Payment_Date = timezone.now()
    usr.Batch = int(data['batch'])
    usr.save()
    dict = {}
    dict['Validity'] = calculate_validity(datetime.date.today())
    dict['Batch'] = data['batch']
    return HttpResponse(json.dumps(dict), content_type='application/json')