from .models import *
from django import forms
from dubirealestate import settings
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView , DetailView, ListView, TemplateView, View
from .views import *
from django.contrib import messages
from django.core.mail import send_mail


class IndexView(ListView):
    template_name = "index.html"
    queryset = Property.objects.filter(is_active=True)
    context_object_name = 'properties'
    paginate_by = 10

class CategoryView(View):
    def get(self, *args, **kwargs):
        category = Category.objects.get(slug=self.kwargs['slug'])
        property = Property.objects.filter(category=category, is_active=True)
        context = {
            'object_list': property,
            'category_title': category,
            'category_description': category.description,
            'category_image': category.image
        }
        return render(self.request, "category.html", context)

@login_required
class PropertyDetailView(DetailView):
    model = Property
    template_name = 'listing.html'
    context_object_name = 'property'
    pk_url_kwarg = 'id'



def contacts(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        listing_id = request.POST['listing_id']
        listing = request.POST.get('listing')
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            is_present = Contact.objects.filter(user_id = user_id, listing_id = listing_id)
            if is_present:
                messages.error(request, "You've already made an inquiry for this listing.")
                return redirect('order-in-proccess')


        contact = Contact(user_id = user_id, listing_id = listing_id, listing = listing, name = name, email = email, phone = phone, message = message )
        contact.save()

        messages.success(request, "Your request have been submitted. A realtor will get back to you soon.")
        return redirect('success')


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "login.html", {
                "error_message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))
    


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "username": username,
                "email": email,
                "password": password,
                "passwords_unmatched": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "username": username,
                "email": email,
                "password": password,
                "confirmation": confirmation,
                "user_taken": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "register.html")


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
         context = super(AboutView, self).get_context_data(**kwargs)
         context['realtors'] = Realtor.objects.all()
         context['mvp'] = Mvp.objects.last()
         return context

def ceeus(request):
    return render(request, 'contact.html')

def success(request):
    return render(request, 'success.html')
    
def order_in_p(request):
    return render(request, 'order-in-proccess.html')