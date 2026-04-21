from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'product_count', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = 'Products'


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3
    fields = ['image', 'caption', 'order', 'image_preview']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="60" style="border-radius:4px;" />', obj.image.url)
        return "No image"
    image_preview.short_description = 'Preview'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['image_thumbnail', 'name', 'category', 'price', 'stock', 'is_active', 'created_at']
    list_display_links = ['image_thumbnail', 'name']
    list_filter = ['is_active', 'category', 'created_at']
    list_editable = ['price', 'stock', 'is_active']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]
    readonly_fields = ['image_preview', 'created_at', 'updated_at']
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'slug', 'category', 'description')
        }),
        ('Pricing & Stock', {
            'fields': ('price', 'stock', 'is_active')
        }),
        ('Main Image', {
            'fields': ('image', 'image_preview')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" height="50" width="50" style="object-fit:cover; border-radius:6px;" />',
                obj.image.url
            )
        return format_html('<span style="color:#aaa;">No image</span>')
    image_thumbnail.short_description = 'Photo'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="150" style="border-radius:8px;" />', obj.image.url)
        return "No image uploaded yet"
    image_preview.short_description = 'Image Preview'
