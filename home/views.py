from django.shortcuts import render
from home.models import Board
#-*- coding: utf-8 -*-
# Create your views here.
def home(request):
    return render(request, 'index.html')

def board_list(request):
    blist = Board.objects.all();
        
    return render(request, 'board_list.html', {'boardList': blist})