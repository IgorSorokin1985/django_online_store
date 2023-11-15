from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'main/index.html')

def contact_us(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        print(username, email)
    return render(request, 'main/contact.html')
