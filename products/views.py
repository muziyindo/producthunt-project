from django.shortcuts import render, redirect ,get_object_or_404 #add redirect, get_object_or_404
from django.contrib.auth.decorators import login_required #added this
from .models import Product #added this
from django.utils import timezone #added this


# Create your views here.

def home(request):
	return render(request,'products/home.html')

@login_required(login_url="accounts/signup")
def create(request):
	if request.method == 'POST':
		if (request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['image'] and request.FILES['icon']) :

			product = Product() #creating model object
			product.title = request.POST['title']
			product.body = request.POST['body']
			if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
				product.url = request.POST['url']
			else:
				product.url = 'http://'+request.POST['url']
			product.icon = request.FILES['icon']
			product.image = request.FILES['image']
			product.pub_date = timezone.datetime.now()
			product.votes_total = 1 # assunming the user who created the product, automatically give 1 vote
			product.hunter = request.user
			product.save()
			return redirect('/products/'+str(product.id))


		else:
			return render(request,'products/create.html',{'error':'All fields are required'})


	else:
		return render(request,'products/create.html')

def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request,'products/detail.html',{'product':product})

def upvote(request,product_id):
	if request.method=='POST':
		product = get_object_or_404(Product, pk=product_id)
		product.votes_total = product.votes_total+1
		product.save()
		return redirect('/products/'+str(product_id))
	else:
		return redirect('/products/'+str(product_id))


