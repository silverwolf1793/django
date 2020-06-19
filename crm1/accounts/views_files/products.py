from ..utils.view_imports_util import *
def products(request):
    pr = Product.objects.all()
    return render(request,'products/products.html', {"products": pr})