from django.contrib import admin
from .models import Ticket, Category

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Category)


# @admin.register(Ticket)
# class TicketAdmin(admin.ModelAdmin):
# 	list_display = ('title', 'user', 'content', 'category', 'ticket_id', 'created', 'modified')
# 	search_fields = ('title', 'user', 'content', 'category', 'ticket_id', 'created', 'modified')

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
# 	list_display = ('name', 'slug')
# 	search_fields = ('name', 'slug')