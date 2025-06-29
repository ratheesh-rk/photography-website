from django.contrib import admin
from .models import BannerImage, PortfolioImage, GalleryImage, ImageUpload, Testimonial, InstagramReel, Couple, CouplePhoto, RandomPhoto

@admin.register(RandomPhoto)
class RandomPhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'created_at']
    
    fieldsets = (
        ('Image', {
            'fields': ('image',)
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(BannerImage)
class BannerImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    list_editable = ['order', 'is_active']
    search_fields = ['title', 'alt_text']
    ordering = ['order', 'created_at']
    
    fieldsets = (
        ('Image Information', {
            'fields': ('title', 'image', 'alt_text')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(PortfolioImage)
class PortfolioImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'order', 'is_featured', 'is_active', 'created_at']
    list_filter = ['category', 'is_featured', 'is_active', 'created_at']
    list_editable = ['order', 'is_featured', 'is_active']
    search_fields = ['title', 'alt_text', 'description']
    ordering = ['order', 'created_at']
    
    fieldsets = (
        ('Image Information', {
            'fields': ('title', 'image', 'alt_text', 'description')
        }),
        ('Categorization', {
            'fields': ('category',)
        }),
        ('Display Settings', {
            'fields': ('order', 'is_featured', 'is_active')
        }),
    )

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    list_editable = ['order', 'is_active']
    search_fields = ['title', 'alt_text', 'description']
    ordering = ['order', 'created_at']
    
    fieldsets = (
        ('Image Information', {
            'fields': ('title', 'image', 'alt_text', 'description')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(ImageUpload)
class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_type', 'is_active', 'created_at']
    list_filter = ['image_type', 'is_active', 'created_at']
    list_editable = ['is_active']
    search_fields = ['title', 'alt_text', 'description']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Image Information', {
            'fields': ('title', 'image', 'image_type', 'alt_text', 'description')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'rating', 'is_active', 'order', 'created_at']
    list_filter = ['rating', 'is_active', 'created_at']
    list_editable = ['order', 'is_active', 'rating']
    search_fields = ['name', 'role', 'testimonial_text']
    ordering = ['order', 'created_at']
    
    fieldsets = (
        ('Client Information', {
            'fields': ('name', 'photo', 'role', 'wedding_date')
        }),
        ('Testimonial Content', {
            'fields': ('testimonial_text', 'rating')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(InstagramReel)
class InstagramReelAdmin(admin.ModelAdmin):
    list_display = ['title', 'likes_count', 'comments_count', 'is_active', 'order', 'created_at']
    list_filter = ['is_active', 'created_at']
    list_editable = ['order', 'is_active', 'likes_count', 'comments_count']
    search_fields = ['title', 'caption']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Reel Information', {
            'fields': ('title', 'video_url', 'thumbnail_url', 'caption')
        }),
        ('Instagram Data', {
            'fields': ('instagram_post_id', 'instagram_url', 'likes_count', 'comments_count', 'views_count')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

class CouplePhotoInline(admin.TabularInline):
    model = CouplePhoto
    extra = 1

@admin.register(Couple)
class CoupleAdmin(admin.ModelAdmin):
    list_display = ['names', 'wedding_date', 'location', 'slug']
    prepopulated_fields = {"slug": ("names",)}
    search_fields = ['names', 'location', 'heading', 'description']
    inlines = [CouplePhotoInline]
    fieldsets = (
        ('Couple Information', {
            'fields': ('names', 'wedding_date', 'location', 'quote', 'cover_photo', 'slug')
        }),
        ('Story Content', {
            'fields': ('heading', 'description')
        }),
    )
