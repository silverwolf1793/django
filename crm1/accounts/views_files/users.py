from ..utils.view_imports_util import *

def login(request):
    context = {}
    return render(request,'users/login.html',context)

def register(request):
    context = {}
    return render(request,'users/register.html',context)