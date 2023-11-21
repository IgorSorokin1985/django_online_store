from django.shortcuts import render
from catalog.models import Product
from main.models import ContactData

# Create your views here.


def index(request):

    contex = {
        'objects_list': Product.objects.all()
    }
    return render(request, 'main/index.html', contex)

def contact_us(request):
    data = {'name': ContactData.objects.get(pk=1)}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        print(username, email)
    return render(request, 'main/contact.html', context=data)


def product_info(request, pk):

    contex = {
        'object': Product.objects.get(pk=pk)
    }
    print(contex)
    return render(request, 'main/product_info.html', contex)