from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import datetime
from home.models import Board, Contact
#-*- coding: utf-8 -*-
# Create your views here.
def home(request):
    return render(request, 'index.html')

def board_list(request):
    blist = Board.objects.all();
        
    return render(request, 'board_list.html', {'boardList': blist})

@csrf_exempt
def contact(request):
    cont = Contact.objects.create(
            customer_name = nullcheck(request.POST.get('customer_name')),
            customer_email = nullcheck(request.POST.get('email')),
            title = nullcheck(request.POST.get('title')),
            content = nullcheck(request.POST.get('content')),
            reg_date = datetime.date.today()
            )
    return render(request, 'contact.html')

def nullcheck(val):
    if val == None:
        return val
    val = val.strip()
    if val == "" or val == "null" or val == "None":
        return None
    else:
        return val