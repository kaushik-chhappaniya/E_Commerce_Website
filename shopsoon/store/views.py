from django.shortcuts import render

from . models import Category, Product

from django.shortcuts import get_object_or_404

# Create your views here.
def store(request):

    all_products = Product.objects.all()

    context =   {'all_products': all_products}

    return render(request, 'store/store.html', context)

def categories(request):
    # Get all categories from the database
    all_categories = Category.objects.all()

    return {'all_categories': all_categories}

# Add to context processor
def product_info(request, slug):

    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, 'store/product-info.html', context )

def list_category(request, category_slug=None):

    category = get_object_or_404(Product, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {'category': category, 'products': products}
    return render(request, 'store/list-category.html', context)