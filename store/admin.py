from django.contrib import admin
from .models import Game, Category, Order, OrderItem, Wishlist, Review


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount_percent', 'category')
    list_editable = ('discount_percent',)


admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Wishlist)
admin.site.register(Review)