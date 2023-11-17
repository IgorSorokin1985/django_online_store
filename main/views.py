from django.shortcuts import render
from catalog.models import Product
from main.models import ContactData

# Create your views here.


def index(request):
    print(Product.objects.all())
    return render(request, 'main/index.html')

def contact_us(request):
    data = {'name': ContactData.objects.get(pk=1)}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        print(username, email)
    return render(request, 'main/contact.html', context=data)
