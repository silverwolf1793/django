from ..utils.view_imports_util import *
from .serializers.home_serializers import home_serializer,home_page


def home_post(request):
    orders = Order.objects.all().order_by('-date_created')
    orders_paginator =  Paginator(orders,5)
    orders_page = request.POST.get('page')
    orders_post = orders_paginator.get_page(orders_page)

    page = home_page(
        page_start= orders_paginator.page_range[0],
        page_end= orders_paginator.page_range[-1],
        page_active= orders_page,
        items= orders_post
    )    
    return Response(home_serializer(page).data,status=status.HTTP_201_CREATED)


def home_get(request):
    orders = Order.objects.all()
    custumers = Custumer.objects.all()
    total_custumers = custumers.count()
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()

    context = {
        'custumers': custumers,
        'total_custumers': total_custumers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending
    }

    return context

@api_view(('POST','GET'))
@requires_csrf_token   
def home(request):
    if request.method == 'POST': return home_post(request)
    return render(request,'dashboard/dashboard.html', home_get(request))
    
    
    
    
    