from django.contrib import admin

# Register your models here.
from.models import Category,Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['Name','Slug']
    prepopulated_fields = {'Slug':('Name',)}
admin.site.register (Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['Name','Price','Stock','Available','Created','Updated']
    list_editable = ['Price','Stock','Available']
    prepopulated_fields = {'Slug':('Name',)}
    list_per_page = 20
admin.site.register (Product,ProductAdmin)