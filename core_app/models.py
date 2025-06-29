from django.db import models
from django.utils.text import slugify
from django.utils import timezone
import os

def get_upload_path(instance, filename):
    """Generate upload path based on image type"""
    if hasattr(instance, 'image_type'):
        return f'images/uploads/{instance.image_type}/{filename}'
    return f'images/uploads/{filename}'

class BannerImage(models.Model):
    """Model for banner/hero section images"""
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/uploads/banner/')
    alt_text = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = 'Banner Image'
        verbose_name_plural = 'Banner Images'

    def __str__(self):
        return self.title or f'Banner Image {self.id}'

    def get_image_url(self):
        """Return the URL for the image"""
        if self.image:
            return self.image.url
        return None

class PortfolioImage(models.Model):
    """Model for portfolio section images"""
    CATEGORY_CHOICES = [
        ('wedding', 'Wedding'),
        ('engagement', 'Engagement'),
        ('portrait', 'Portrait'),
        ('ceremony', 'Ceremony'),
        ('reception', 'Reception'),
        ('details', 'Details'),
    ]

    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/uploads/portfolio/')
    alt_text = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='wedding')
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = 'Portfolio Image'
        verbose_name_plural = 'Portfolio Images'

    def __str__(self):
        return self.title or f'Portfolio Image {self.id}'

    def get_image_url(self):
        """Return the URL for the image"""
        if self.image:
            return self.image.url
        return None

class GalleryImage(models.Model):
    """Model for gallery images"""
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/uploads/gallery/')
    alt_text = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return self.title or f'Gallery Image {self.id}'

    def get_image_url(self):
        """Return the URL for the image"""
        if self.image:
            return self.image.url
        return None

class ImageUpload(models.Model):
    """Generic model for any image upload"""
    IMAGE_TYPE_CHOICES = [
        ('banner', 'Banner'),
        ('portfolio', 'Portfolio'),
        ('gallery', 'Gallery'),
        ('logo', 'Logo'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to=get_upload_path)
    image_type = models.CharField(max_length=20, choices=IMAGE_TYPE_CHOICES, default='other')
    alt_text = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Image Upload'
        verbose_name_plural = 'Image Uploads'

    def __str__(self):
        return self.title or f'Image Upload {self.id}'

    def get_image_url(self):
        """Return the URL for the image"""
        if self.image:
            return self.image.url
        return None

    def save(self, *args, **kwargs):
        # Set image_type based on upload path if not specified
        if not self.image_type and self.image:
            path = self.image.name
            if 'banner' in path:
                self.image_type = 'banner'
            elif 'portfolio' in path:
                self.image_type = 'portfolio'
            elif 'gallery' in path:
                self.image_type = 'gallery'
            elif 'logo' in path:
                self.image_type = 'logo'
        super().save(*args, **kwargs)

class Testimonial(models.Model):
    """Model for client testimonials"""
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/uploads/testimonials/', blank=True, null=True)
    role = models.CharField(max_length=200, blank=True)  # e.g., "Bride", "Groom", "Couple"
    testimonial_text = models.TextField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    wedding_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return f"{self.name} - {self.role}"

    def get_photo_url(self):
        """Return the URL for the photo"""
        if self.photo:
            return self.photo.url
        return None

class InstagramReel(models.Model):
    """Model for Instagram reels"""
    title = models.CharField(max_length=200)
    video_url = models.URLField()
    thumbnail_url = models.URLField(blank=True, null=True)
    caption = models.TextField()
    likes_count = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)
    views_count = models.PositiveIntegerField(default=0)
    instagram_post_id = models.CharField(max_length=100, blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Instagram Reel'
        verbose_name_plural = 'Instagram Reels'

    def __str__(self):
        return f"{self.title} - {self.likes_count} likes"

    def get_formatted_likes(self):
        """Return formatted likes count (e.g., 1.2k, 856)"""
        if self.likes_count >= 1000:
            return f"{self.likes_count/1000:.1f}k"
        return str(self.likes_count)

    def get_formatted_comments(self):
        """Return formatted comments count"""
        if self.comments_count >= 1000:
            return f"{self.comments_count/1000:.1f}k"
        return str(self.comments_count)

class Couple(models.Model):
    names = models.CharField(max_length=200)
    wedding_date = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    quote = models.TextField(blank=True)
    cover_photo = models.ImageField(upload_to='couple_photos/covers/')
    slug = models.SlugField(unique=True, blank=True)
    heading = models.CharField(max_length=255)
    description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.names)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.names

class CouplePhoto(models.Model):
    couple = models.ForeignKey(Couple, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='couple_photos/gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.couple.names} - {self.caption or 'Photo'}"

class RandomPhoto(models.Model):
    """Model for random photos section above FAQ"""
    image = models.ImageField(upload_to='images/uploads/random_photos/')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = 'Random Photo'
        verbose_name_plural = 'Random Photos'

    def __str__(self):
        return f'Random Photo {self.id}'

    def get_image_url(self):
        """Return the URL for the image"""
        if self.image:
            return self.image.url
        return None
