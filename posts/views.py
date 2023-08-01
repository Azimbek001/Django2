from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Product, Hashtag, Category, Review
from posts.forms import ProductCreateForm, ReviewCreateForm


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context_data = {
            'posts': products,
            'user': request.user
        }

        return render(request, 'products/products.html', context=context_data)


def hashtags_view(request):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()

        context_data = {
            'hashtags': hashtags
        }
        return render(request, 'hashtags/hashtags.html', context=context_data)


def show_categories(request):
    categories = Category.objects.all()

    contex_data = {
        'categories':categories
    }
    return render(request, 'categories/categories.html', context=contex_data)


def post_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context_data = {
            'product': product
        }

        return render(request, 'products/detail.html', context=context_data)
    if request.method == "POST":
        product = Product.objects.get(id=id)
        form = ReviewCreateForm(data=request.POST)

        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                product_id=id
            )

        context = {
            'product': product,
            'reviews': product.reviews.all(),
            'form': form
        }
        return render(request, 'products/detail.html', context=context)


def post_create_view(request):
    if request.method == 'GET':
        context_data = {
            'form': ProductCreateForm()
        }
        return render(request, 'products/create.html', context=context_data)

    if request.method == 'POST':
        data = request.POST
        form = ProductCreateForm(data)

        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
            )
            return redirect('/products/')

        return render(request, 'products/create.html', context={
            'form': form
        })









