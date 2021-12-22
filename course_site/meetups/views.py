from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Meetup
# Create your views here.

def index(request):
    all_obj=Meetup.objects.all()


    return render(request,'meetups/index.html',{
        'meetups': all_obj,

    })
def meetup_details(request,slug):
    obj=get_object_or_404(Meetup,slug=slug)
    return render(request,'meetups/meetup-detail.html',{
        'meetup':obj,
    })