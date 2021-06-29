from django.shortcuts import render
from django.http import HttpResponse
import datetime
from calc.models import Request
# Create your views here.


def home(request):
    return render(request,'home.html')

def display(request):
    firstname = request.GET['Firstname']
    lastname = request.GET['Lastname']
    DOB = request.GET['Dateofbirth']
    Gender = request.GET['Gen']
    nationality = request.GET['nation']
    Currentcity = request.GET['city']
    state = request.GET['state']
    pincode = request.GET['pin']
    Qualification = request.GET['qualify']
    salary = int(request.GET['salary'])
    pan_card = request.GET['pan']

    if len(firstname) != 0 or len(firstname) > 3:
        if len(lastname) > 3:
            if datetime.datetime.strptime(DOB, '%Y-%m-%d'):
                if Gender == 'male' or Gender == 'female':
                    if len(nationality) > 2: 
                        if len(Currentcity) > 3:
                            if len(state) != 0:
                                if len(pincode) > 5 or len(pincode) < 7:
                                    if len(Qualification) > 2:
                                        if salary > 10000:
                                            if len(pan_card) == 10:
                                                a = Request(requestid = 1,fname = firstname ,lname = lastname ,dob = DOB ,gender = Gender ,nationality = nationality ,state = state ,city = Currentcity ,pincode = pincode ,qualification = Qualification ,salary = salary ,pancard = pan_card)
                                                a.save()
                                                return render(request,'result.html',{'operation' : 'success'})
                                            else:
                                                return render(request,'result.html',{'operation' : 'reject'})

                                            

    