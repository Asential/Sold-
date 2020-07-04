from django.contrib import admin
from auctions.models import User, Comment, Bid, Listing
# Register your models here.

admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Bid)
admin.site.register(Listing)