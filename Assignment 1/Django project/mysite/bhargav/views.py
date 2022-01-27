from django.shortcuts import render, HttpResponse
# Create your views here.

def show(render):
    return HttpResponse("Bhargav Sonagara")

def index(request):
    return render(request, 'index.html')
def account(request):
    return render(request, 'account.html')
def cart(request):
    return render(request, 'cart.html')
def cart1(request):
    return render(request, 'cart1.html')
def contact(request):
    return render(request, 'contact.html')
def product1(request):
    return render(request, 'product1.html')
def products(request):
    return render(request, 'products.html')
def signup(request):
    return render(request, 'signup.html')
def follower(request):
    return render(request, 'follower.html')