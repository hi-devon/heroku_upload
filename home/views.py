from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import datetime
from home.models import Board, Contact, SettingsInfo
from passlib.hash import pbkdf2_sha256
from django.http.response import JsonResponse
from django.db.models import Max

#-*- coding: utf-8 -*-
# Create your views here.
def home(request):
    return render(request, 'index.html')

def board_list(request):
    blist = Board.objects.all();
        
    return render(request, 'board_list.html', {'boardList': blist})
    
@csrf_exempt
def password_check(request):
    pwd = request.POST.get('pwd')
    si = SettingsInfo.objects.get(itemkey="admin_password")
    if pbkdf2_sha256.verify(pwd, si.itemval):
        retval = "ok"
        request.session['is_authenticated'] = True
    else:
        retval = "fail"
        request.session['is_authenticated'] = False
    data = {"is_authenticated": retval}
    return JsonResponse(data, safe=False)
    
@csrf_exempt
def contact(request):
    if nullcheck(request.POST.get('customer_name')) != None and \
        nullcheck(request.POST.get('email')) != None and \
        nullcheck(request.POST.get('content')) != None:
    
        cont = Contact.objects.create(
                customer_name = nullcheck(request.POST.get('customer_name')),
                customer_email = nullcheck(request.POST.get('email')),
                title = nullcheck(request.POST.get('title')),
                content = nullcheck(request.POST.get('content')),
                reg_date = datetime.date.today()
                )
    return render(request, 'contact.html')
@csrf_exempt
def board_detail(request):
    if request.method == "POST":
        brd = Board.objects.get(pk=request.POST.get("board_id"))
        brd.delete()
    else:
        brd = Board.objects.get(pk=request.GET.get('id'))
    return render(request, 'board_detail.html', {"board": brd})

def register_board(request):
    if nullcheck(request.POST.get('gubun')) != None and \
        nullcheck(request.POST.get('title')) != None and \
        nullcheck(request.POST.get('content')) != None:
        nm = Board.objects.aggregate(Max('num'))

        nm['num__max'] += 1
        Board.objects.create(
            num = nm['num__max'],
            gubun = nullcheck(request.POST.get('gubun')),
            title = nullcheck(request.POST.get('title')),
            reg_date = datetime.date.today(),
            content = nullcheck(request.POST.get('content'))
            )
    return render(request, 'register_board.html')

def auth_check(request):
    data = {"is_authenticated": request.session.get('is_authenticated')}

    return JsonResponse(data, safe=False)

    
def nullcheck(val):
    if val == None:
        return val
    val = val.strip()
    if val == "" or val == "null" or val == "None":
        return None
    else:
        return val