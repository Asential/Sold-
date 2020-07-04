from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from .models import User, Listing, Bid, Comment, WishList


class ListingForm(ModelForm):  
    class Meta:  
        model = Listing  
        fields = "__all__"  

#----------------------------------------------------------------

def index(request):

    listing_items = Listing.objects.all()

    return render(request, "auctions/index.html", {
        "items": listing_items
    })

#----------------------------------------------------------------

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

#----------------------------------------------------------------

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            wishlist = WishList.objects.create(name = user)
            wishlist.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

#----------------------------------------------------------------

def listing(request, id):
    
    wishlist = WishList.objects.get(name=request.user)
    item = Listing.objects.get(id=id)

    for i in wishlist.item.all():
        if i == item:
            return render(request, "auctions/listing.html", {
                "item": item,
                "wishlisted": True
            })

    return render(request, "auctions/listing.html", {
        "item": item,
        "wishlisted": False
    })

#----------------------------------------------------------------

@login_required
def create(request):
    form = ListingForm()
    return render(request, "auctions/create.html", {
        "form": form
    })

@login_required
def save(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form:
            Listing.objects.create(
                item = form.data.get('item'), 
                description = form.data.get('description'), 
                category =  form.data.get('category'), 
                startbid =  form.data.get('startbid'),
                user = request.user
            )
            return HttpResponseRedirect(reverse("index")) 
        else:
            print("Error")
            return HttpResponseRedirect(reverse("index"))

@login_required
def wishlist(request, id):
    if request.method == "POST":
        item = Listing.objects.get(id=id)
        wishlist = WishList.objects.get(name=request.user)
        
        for i in wishlist.item.all():
            if i == item:
                print("ALREADY THERE")
                return HttpResponseRedirect(reverse("listing",args=(id,)))

        wishlist.item.add(item)
        print("ADDED")
        return HttpResponseRedirect(reverse("listing",args=(id,)))
            
        
    else:
        print("Error")
        return HttpResponseRedirect(reverse("listing",args=(id,)))

@login_required
def unwishlist(request, id):
    if request.method == "POST":
        print("Unwishlisting")
        item = Listing.objects.get(id=id)
        wishlist = WishList.objects.get(name=request.user)
        
        for i in wishlist.item.all():
            if i == item:
                wishlist.item.remove(item)
                return HttpResponseRedirect(reverse("listing",args=(id,)))
        
    else:
        print("Error")
        return HttpResponseRedirect(reverse("listing",args=(id,)))

@login_required
def watchlist(request):

    wishlist = WishList.objects.get(name=request.user)
    watchlist_items = wishlist.item.all()
    return render(request, "auctions/watchlist.html", {
        "items": watchlist_items
    })

@login_required
def placebid(request, id):
    form = request.POST
    bid = int(form["bid"])
    item = Listing.objects.get(id=id)
    if bid >= item.startbid:
        currentbid = bid
        if Bid.objects.filter(item=item):
            totalbids = Bid.objects.filter(item=item)
            for bid in totalbids:
                if currentbid <= bid.amount:
                    print("Bid Smaller than other bids!")
                    return HttpResponseRedirect(reverse("listing",args=(id,)))

            print("New Bid Placed!")
            newbid = Bid.objects.create(placer = request.user, item=item, amount = currentbid)
            return HttpResponseRedirect(reverse("listing",args=(id,)))

        else:
            print("First Bid Placed!")
            newbid = Bid.objects.create(placer = request.user, item=item, amount = currentbid)
            return HttpResponseRedirect(reverse("listing",args=(id,)))

        print("Bid smaller than other bids!")
        return HttpResponseRedirect(reverse("listing",args=(id,)))

    print("Bid smaller than starting bid!")
    return HttpResponseRedirect(reverse("listing",args=(id,)))