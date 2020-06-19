from ..utils.view_imports_util import *

def home(request):
    orders = Order.objects.all().order_by('-date_created')
    orders_paginator =  Paginator(orders,5)
    orders_page = request.GET.get('page')
    orders_post = orders_paginator.get_page(orders_page)

    custumers = Custumer.objects.all()
    total_custumers = custumers.count()
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()

    context = {
        'orders': orders_post ,
        'custumers': custumers,
        'total_custumers': total_custumers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
        'paging_range': 5
    }
    return render(request,'dashboard/dashboard.html',context)