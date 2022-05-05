from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'created_on',
                       'delivery_cost', 'order_total',
                       'grand_total')

    fields = ('order_number', 'customer_profile', 'created_on', 'delivery_cost',
              'order_total', 'grand_total')

    list_display = ('order_number', 'created_on', 'customer_profile',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-created_on',)


admin.site.register(Order, OrderAdmin)
