from django.shortcuts import render, redirect
from .models import *
# Create your views here.
from django.http import HttpResponse
from .forms import *
from django.forms import inlineformset_factory
from .filters import OrderFilter

def home(request):
    orders = Order.objects.all()
    custumers = Custumer.objects.all()
    total_custumers = custumers.count()
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()

    context = {
        'orders': orders,
        'custumers': custumers,
        'total_custumers': total_custumers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
    }
    return render(request,'accounts/dashboard.html',context)

def login(request):
    context = {}
    return render(request,'accounts/login.html',context)

def register(request):
    context = {}
    return render(request,'accounts/register.html',context)

def products(request):
    pr = Product.objects.all()
    return render(request,'accounts/products.html',{"products": pr})

def custumer(request,id):
    cstumer = Custumer.objects.get(id=id)
    orders = cstumer.order_set.all()
    totalOrders = cstumer.order_set.all().count()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    context = {
        'custumer': cstumer,
        'orders': orders,
        'totalOrders': totalOrders,
        'myFilter': myFilter
    }
    return render(request,'accounts/custumer.html',context)

def createOrder(request,id):
    OrderFormSet = inlineformset_factory(Custumer, Order, fields=('product','status'), extra=10, can_delete=False)
    cstumer = Custumer.objects.get(id=id)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=cstumer)
    context = {
        "formset": formset
    }

    if request.method == 'POST':
        formset = OrderFormSet(request.POST,instance=cstumer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    return render(request,'accounts/order_form.html',context)

def updateOrder(request,id):
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)
    context = {'form' : form}

    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request,'accounts/order_form.html',context)

def deleteOrder(request,id):
    order = Order.objects.get(id=id)
    context = {'item': order}
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    return render(request, 'accounts/delete.html', context)
