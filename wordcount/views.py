from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def count(request):
    data=request.GET['para']
    w_list=data.split()
    l=len(w_list)
    w_dict={}
    for w in w_list:
        if w in w_dict:
            w_dict[w]+=1
        else:
            w_dict[w]=1
    return render(request,'count.html',{'text_no':l,'word':w_dict})