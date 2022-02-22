from django.shortcuts import render

from .models import Products, Categories


def index(request):
    data = {
        "nav": Products.objects.filter(category=1, is_published=True),
        "new": Products.objects.filter(category=3, is_published=True),
        "categories": {
            "oshxona": Products.objects.filter(category=4, is_published=True),
            "mehmonxona": Products.objects.filter(category=5, is_published=True),
            "shifoxona": Products.objects.filter(category=6, is_published=True),
            "maktab": Products.objects.filter(category=7, is_published=True)
        },
        "all": Products.objects.all()
    }

    return render(request, 'components/index.html', data)


def contacts(request):
    return render(request, 'components/_contacts.html')


def about(request):
    return render(request, 'components/_about.html')


def product_detail(request, pk):
    product = Products.objects.filter(pk=pk)
    return render(request, 'components/product_detail.html', context={
        "product": product
    })
