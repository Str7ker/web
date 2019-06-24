from index.models import Logo
from index.forms import OrderForm

def logos(request):
    return {"logose": Logo.objects.last()}

def form_order(request):
    order_form = OrderForm()
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
    else:
        order_form = OrderForm()
    return {"order": order_form}