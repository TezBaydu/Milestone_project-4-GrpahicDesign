from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'order_total', 'grand_total',)

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'street_address1',
              'street_address2', 'town_or_city',
              'postcode',  'county', 'country',
              'order_total', 'grand_total',
              'company_name', 'company_slogan',
              'company_description', 'company_colors',
              'company_look',
              )

    list_display = ('order_number', 'date', 'full_name',
                    'company_name', 'order_total', 
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
