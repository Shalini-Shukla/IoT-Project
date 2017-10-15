from django.shortcuts import render
from django.http import Http404
import json
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect


def index(request,date):
    return render(request,'time_wise/index.html',{'date':date})