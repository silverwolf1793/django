from ..utils.view_imports_util import *
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
    return render(request,'custumers/custumer.html',context)

