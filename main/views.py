from django.shortcuts import render
from catalog.models import Product, Category
from main.models import ContactData

# Create your views here.


def index(request):
    number_page = 0
    if request.method == 'POST':
        try:
            number_page = int(request.POST.get('number_page'))
            print(number_page)
        except:
            pass
    number_objects_page = 3
    number_objects = len(Product.objects.all())
    number_pages = number_objects // number_objects_page + 1
    contex = {
        'objects_list': Product.objects.all()[number_page*number_objects_page:(number_page+1)*number_objects_page],
        'number_pages': list(range(number_pages))
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

def add_product(request):
    if request.method == 'POST':
        try:
            new_product = {
                'product_name': request.POST.get('product_name'),
                'product_description': request.POST.get('product_description'),
                'category_id': Category.objects.filter(category_name=request.POST.get('category'))[0].pk,
                'price': int(request.POST.get('price')),
            }

            Product.objects.create(**new_product)
            print(new_product)
        except:
            print('Incorrect data')

    return render(request, 'main/add_product.html')