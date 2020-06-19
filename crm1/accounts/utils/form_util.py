def evalForm(request, eval_type, **kwargs):
    if request is None: return False
    if eval_type is None: return False

    method = kwargs.get('method', 'POST')
    if request.method != method: return False

    element = kwargs.get('element', None)
    model = kwargs.get('model', None)

    RESPONSE = False

    if(
            eval_type == 'create_form_set' and
            element is not None and
            model is not None
    ):
        formset = model(request.POST,instance=element)
        if formset.is_valid():
            formset.save()
            RESPONSE = True
    elif(
        eval_type == 'update' and
        element is not None and
        model is not None
    ):
        form = model(request.POST,instance=element)
        if form.is_valid():
            form.save()
            RESPONSE = True
    elif(
        eval_type == 'delete' and
        element is not None
    ):
        element.delete()
        RESPONSE = True

    return RESPONSE
