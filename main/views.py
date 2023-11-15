from django.shortcuts import render
from django.db import connection

# Create your views here.


def index(request):
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM catalog_product')
        print(cursor.fetchall())
    return render(request, 'main/index.html')

def contact_us(request):
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM main_contactdata')
        data = {'name': cursor.fetchall()}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        print(username, email)
    return render(request, 'main/contact.html', context=data)
