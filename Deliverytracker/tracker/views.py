from django.shortcuts import render

# Create your views here.

from .models import Delivery

def delivery_list(request):
    deliveries = Delivery.objects.all().order_by('-updated_at')
    return render(request, 'tracker/delivery_list.html', {'deliveries': deliveries})


def home(request):
    query = request.GET.get('q')
    if query:
        deliveries = Delivery.objects.filter(customer_name__icontains=query)
    else:
        deliveries = Delivery.objects.all()
    return render(request, 'tracker/home.html', {'deliveries': deliveries})




