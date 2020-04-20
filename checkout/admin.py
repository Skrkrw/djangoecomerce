from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.
# Adding the two models to be able to edit them

# Tabular subclass defines the template used to
# render the Order in the admin interface.
# StackedInline is anoter option
class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem

# The admin interface has the ability to edit 
# more than one model on a single page. This is
# known as "inlines"

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )

# Register of both in the admin site to be able
# to edit them when necessary
admin.site.register(Order, OrderAdmin)