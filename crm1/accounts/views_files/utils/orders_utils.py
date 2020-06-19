from ...utils.view_imports_util import redirect
def order_redirect(id,cid):
    if cid != '-1':
        return redirect('/custumer/' + cid)
    return redirect('/')