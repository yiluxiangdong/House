from django.shortcuts import render
from django.shortcuts import render_to_response,redirect,HttpResponse,render,HttpResponseRedirect
from .models import *
import time
# Create your views here.
def  longin(request):
    return render(request,'index.html',locals())


def  insert(request):
     if request.method =='POST':
        ip = request.POST['ipadress']
        addtime = time.strftime('%Y-%m-%d:%H:%M:%S')
        host = HostInfo()
        host.ip=ip
        host.createTime=addtime
        host.save()
        print addtime
        return render_to_response('main.html',locals())
     else:
         return HttpResponse('no data return')

