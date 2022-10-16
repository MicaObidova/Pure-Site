from decimal import Decimal
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render,redirect, HttpResponseRedirect
from .models import *

def index(request):
    user = request.user
    total = 0
    card = []
    product_count = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
        product_count = card.count()
    context = {
        'review': Review.objects.all(),
        "product_count": product_count,
        "total": total,
        "card": card,
        'subcat': SubCategory.objects.all(),
        'category': Category.objects.all(),
        'products': Product.objects.all(),
        'random': Product.objects.order_by('?')[:3],
        'blogs': Blog.objects.all(),
    }
    return render(request, 'index2.html', context)

def about(request):
    user = request.user
    total = 0
    card = []
    product_count = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
        product_count = card.count()
    context = {
        'expert': Expert.objects.all(),
        "product_count": product_count,
        "total": total,
        "card": card,
        'products': Product.objects.all(),
    }
    return render(request, 'about.html', context)

def blogview(request,pk):
    user = request.user
    total = 0
    card = []
    product_count = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
        product_count = card.count()
    context = {
        "product_count": product_count,
        "total": total,
        "card": card,
        'blog': Blog.objects.get(id=pk),
        'blogs': Blog.objects.all(),
        'avtor': Author.objects.all(),
        'coment': Comment.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'blog-single.html', context)

def ADDcomment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        coment = request.POST.get('comment')
        Comment.objects.create(fullname=name,email=email,comment=coment)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def blog(request):
    user = request.user
    total = 0
    card = []
    product_count = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
        product_count = card.count()
    context = {
        "product_count": product_count,
        "total": total,
        "card": card,
        'blogs': Blog.objects.all(),
        'product': Product.objects.order_by('?')[:3],
        'products': Product.objects.all(),
    }
    return render(request, 'blog.html', context)

def cart(request):
    user = request.user
    total = 0
    card = []
    product_count = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
        product_count = card.count()
    context = {
        "product_count": product_count,
        "total": total,
        "card": card,
        'products': Product.objects.all(),
    }
    return render(request, 'cart.html', context)
        

def AddCard(request, pk):
    user = request.user
    product = Product.objects.get(id=pk)
    Card.objects.create(user=user, product=product)
    return redirect('cart')

def DeleteCard(request, pk):
    Card.objects.get(id=pk).delete()
    return redirect('cart')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    user = request.user
    total = 0
    card = []
    product_count = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
        product_count = card.count()
    context = {
        "product_count": product_count,
        "total": total,
        "card": card,
        'products': Product.objects.all(),
    }
    return render(request, 'contact.html', context)

def productviews(request, pk):
    user = request.user
    total = 0
    card = []
    product_count = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
        product_count = card.count()
    context = {
        "product_count": product_count,
        "total": total,
        "card": card,
        'product':Product.objects.get(id=pk),
        'products':Product.objects.order_by('?')[:3],
        'productss': Product.objects.all(),
    }
    return render(request, 'product-single.html',context)

def profile(request):
    context = {
        'user': User.objects.all()
    }
    return render(request, 'profile.html', context)

def service(request):
    user = request.user
    total = 0
    card = []
    product_count = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
        product_count = card.count()
    context = {
        'expert': Expert.objects.all(),
        "product_count": product_count,
        "total": total,
        "card": card,
        'products': Product.objects.all(),
    }
    return render(request, 'service.html', context)

def shop(request):
    user = request.user
    total = 0
    card = []
    product_count = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
        product_count = card.count()
    context = {
        "product_count": product_count,
        "total": total,
        "card": card,
        'subcat': SubCategory.objects.all(),
        'category': Category.objects.all(),
        'products': Product.objects.all(),
        'random': Product.objects.order_by('?')[:3],
    }
    return render(request, 'shop.html', context)

def Search(request):
    blog = []
    if request.method == "POST":
        name = request.POST.get('name')
        blog = Blog.objects.filter(name__icontains=name)
        print(blog)
    return redirect('blog')

def Searching(request):
    product = []
    if request.method == "POST":
        name = request.POST.get('name')
        product = Product.objects.filter(name__icontains=name)
        print(product)
    return redirect('shop')

from django.contrib.auth import login, logout, authenticate

def Registration(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('registration')
    return render(request, 'registration.html')

def ForLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.count() > 0:
            usr = authenticate(username=username, password=password)
            if usr is not None:
                login(request, usr)
                return redirect('index')
            else:
                return redirect('registration')
        else:
            return redirect('registration')
    return redirect('registration')

def LogOutView(request):
    logout(request)
    return redirect('index')


def CheckoutView(request):
    user = request.user
    total = 0
    card = []
    product_count = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
        product_count = card.count()
    context = {
        "product_count": product_count,
        "total": total,
        "card": card,
        'products': Product.objects.all(),
    }
    return render(request, 'checkout.html', context)

def OrderView(request):
    if request.method == "POST":
        user_id = request.POST.get('user')
        name = request.POST.get('username')
        adress = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        city = request.POST.get('city')
        index = request.POST.get('index')
        user = User.objects.get(id=user_id)
        order = Order.objects.create(
            user=user,
            name=name,
            adress=adress,
            phone=phone,
            email=email,
            city=city,
            index=index,
            price=0
        )
        total_price = 0
        for i in Card.objects.filter(user=user):
            OrderItem.objects.create(
                order=order,
                product=i.product,
                price=i.product.price
            )
            total_price += i.product.price
        order.price = total_price
        order.save()
        for i in Card.objects.filter(user=user):
            i.delete()
        return redirect('index')
    return redirect('checkout')


class SearchBlog():

    def get_queryset(self):
        paginate_by = 3
        return Blog.objects.filter(name__icontains=self.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['q']= self.request.GET.get('q')
        return context

