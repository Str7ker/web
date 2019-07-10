from index.models import Logo
from index.forms import OrderForm, EmailForm

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

def form_email(request):
    email_form = EmailForm()
    if request.method == 'POST':
        email_form = EmailForm(request.POST)
        if email_form.is_valid():
            email_form.save()
    else:
        email_form = EmailForm()
    return {"email_form": email_form}