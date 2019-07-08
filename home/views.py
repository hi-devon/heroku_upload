from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def board_list(request):
    blist = None
    return render(request, 'board_list.html', {'boardList': blist})