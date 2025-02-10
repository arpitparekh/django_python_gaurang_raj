from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Blog

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

def show_product(request, product_id=None):
    products = Product.objects.all()

    # If product_id is provided in the URL, fetch product for update
    if product_id is not None and request.method != 'POST':
        print("Fetching Product for Update")
        p = get_object_or_404(Product, id=product_id)
        return render(request, 'product_crud.html', {"products": products, "product": p})

    if request.method == 'POST':
        my_id = request.POST.get('product_id')  # Get ID from form
        name = request.POST.get('product_name')
        price = request.POST.get('product_price')
        description = request.POST.get('product_description')
        image = request.FILES.get('product_image')

        if my_id and my_id.strip():  # Ensure my_id is not empty
            print("Updating Product...")

            # Fetch the existing product
            p = get_object_or_404(Product, id=my_id)
            p.name = name
            p.price = price
            p.description = description

            # Only update image if a new one is uploaded
            if image:
                p.image = image

            p.save()
            print("Product Updated")
        else:
            print("Adding New Product...")
            p = Product(name=name, price=price, description=description, image=image)
            p.save()
            print("Product Saved")

        return redirect('product_crud')

    return render(request, 'product_crud.html', {"products": products})

def delete_product(request):

    product_id = request.POST.get('product_id')

    p = Product.objects.get(id=product_id)  # find specific product by id
    p.delete()
    return redirect('product_crud')


def show_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs.html',{"blogs":blogs})


