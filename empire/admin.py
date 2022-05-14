from django.contrib import admin
from .models import *
# Register your models here.


def copy_items(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()

copy_items.description = 'Copy Items'

class PropertyAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'category',
    ]
    list_filter = ['id', 'title', 'category']
    search_fields = ['title', 'category']
    prepopulated_fields = {"slug": ("title",)}
    actions = [copy_items]

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'name', 'email', 'contact_date')
    list_display_links = ('id', 'listing', 'name')
    search_fields = ('name', 'listing', 'email')
    list_filter = ('listing',)
    list_per_page = 20



class RealtorAdmin(admin.ModelAdmin):
    list_display =('id', 'name', 'is_mvp', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    list_editable = ('is_mvp',)
    search_fields = ('name',)
    list_per_page = 20



class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'is_active'
    ]
    list_filter = ['title', 'is_active']
    search_fields = ['title', 'is_active']
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Property, PropertyAdmin),
admin.site.register(Contact, ContactAdmin),
admin.site.register(Category, CategoryAdmin),
admin.site.register(Realtor, RealtorAdmin)
#admin.site.register()
#admin.site.register()
#admin.site.register()