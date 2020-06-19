from ..utils.view_imports_util import *
from .utils.orders_utils import *
from ..utils.form_util import evalForm

def createOrder(request,id):
    OrderFormSet = inlineformset_factory(Custumer, Order, fields=('product','status'), extra=10, can_delete=False)
    custumer = Custumer.objects.get(id=id)
    context = {
        "formset": OrderFormSet(queryset=Order.objects.none(),instance=custumer)
    }

    if evalForm(request,'create_form_set',element=custumer,model=OrderFormSet):
        return order_redirect(id,id)

    return render(request,'orders/order_form.html',context)

def updateOrder(request,id,cid):
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)
    context = {'form' : form}
    
    if evalForm(request,'update',element=order,model=OrderForm):
        return order_redirect(id,cid)

    return render(request,'orders/order_form.html',context)

def deleteOrder(request,id,cid):
    order = Order.objects.get(id=id)
    context = {'item': order}

    if evalForm(request,'delete',element=order):
        return order_redirect(id,cid)
    return render(request, 'orders/delete.html', context)
