from django.shortcuts import render,redirect
from .models import Product

# Create your views here.
def show_intro(request):
    return render(request, 'intro.html',{"data":"Hello World"})

def show_pass_data(request):

    student = {
        'name':'Rajesh',
        'age':30,
        'address':'123 Main St',
        'img':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQn9zilY2Yu2hc19pDZFxgWDTUDy5DId7ITqA&s'
    }

    data = {
        "fruits":["apple","banana","cherry","date","elderberry","fig","grape","honeydew melon","jackfruit","kiwi","lemon","mango","nectarine","orange","papaya","quince","raspberry","strawberry","tangerine","watermelon","xigua","yuzu","zucchini"],
        "title":'Bascom Bridge',
        "student":student
    }

    return render(request,'pass_data.html',data)

def show_product(request):
    if request.method == 'POST':
        print("Calling")
        name = request.POST.get('product_name')
        price = request.POST.get('product_price')
        description = request.POST.get('product_description')
        image = request.FILES.get('product_image')

        p = Product(name=name,price=price,description=description,image=image)
        p.save()
        print("Saved")
        return redirect('product_crud')


    return render(request,'product_crud.html')
