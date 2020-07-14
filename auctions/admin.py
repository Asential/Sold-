from django.contrib import admin
from auctions.models import User, Comment, Bid, Listing, WishList
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ("liked",)

admin.site.register(User)
admin.site.register(WishList, UserAdmin)
admin.site.register(Comment)
admin.site.register(Bid)
admin.site.register(Listing)