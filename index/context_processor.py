from index.models import Logo

def logos(request):
    return {"logose": Logo.objects.last()}