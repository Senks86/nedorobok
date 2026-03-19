from django.shortcuts import render

# Create your views here.
def games_list(request):
    return render(request,"games/games_list.html")
def circle(request):
    return render(request,"games/circle.html")