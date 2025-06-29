from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import BannerImage, PortfolioImage, GalleryImage, Testimonial, InstagramReel, Couple, RandomPhoto

def home(request):
    """Home page view"""
    # Get banner images
    banner_images = BannerImage.objects.filter(is_active=True).order_by('order')
    
    # Get couples for the slider (latest 10)
    slider_couples = Couple.objects.all().order_by('-wedding_date')[:10]
    
    # Get testimonials
    testimonials = Testimonial.objects.filter(is_active=True).order_by('order')
    
    # Get Instagram reels
    instagram_reels = InstagramReel.objects.filter(is_active=True).order_by('order')[:4]
    
    # Get random photos for the section above FAQ
    random_photos = RandomPhoto.objects.filter(is_active=True).order_by('order')
    
    context = {
        'banner_images': banner_images,
        'slider_couples': slider_couples,
        'testimonials': testimonials,
        'instagram_reels': instagram_reels,
        'random_photos': random_photos,
    }
    
    return render(request, 'core_app/home.html', context)

@csrf_exempt
@require_http_methods(["POST"])
def upload_image(request):
    """Handle image uploads via AJAX"""
    try:
        if 'image' in request.FILES:
            image_file = request.FILES['image']
            image_type = request.POST.get('image_type', 'other')
            title = request.POST.get('title', '')
            alt_text = request.POST.get('alt_text', '')
            
            # Create the appropriate model instance
            if image_type == 'banner':
                image_instance = BannerImage.objects.create(
                    title=title,
                    image=image_file,
                    alt_text=alt_text
                )
            elif image_type == 'portfolio':
                image_instance = PortfolioImage.objects.create(
                    title=title,
                    image=image_file,
                    alt_text=alt_text
                )
            elif image_type == 'gallery':
                image_instance = GalleryImage.objects.create(
                    title=title,
                    image=image_file,
                    alt_text=alt_text
                )
            else:
                return JsonResponse({'error': 'Invalid image type'}, status=400)
            
            return JsonResponse({
                'success': True,
                'image_id': image_instance.id,
                'image_url': image_instance.get_image_url(),
                'message': 'Image uploaded successfully'
            })
        else:
            return JsonResponse({'error': 'No image file provided'}, status=400)
            
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_images(request, image_type):
    """Get images by type for AJAX requests"""
    try:
        if image_type == 'banner':
            images = BannerImage.objects.filter(is_active=True).order_by('order')
        elif image_type == 'portfolio':
            images = PortfolioImage.objects.filter(is_active=True).order_by('order')
        elif image_type == 'gallery':
            images = GalleryImage.objects.filter(is_active=True).order_by('order')
        else:
            return JsonResponse({'error': 'Invalid image type'}, status=400)
        
        image_data = []
        for image in images:
            image_data.append({
                'id': image.id,
                'title': image.title,
                'url': image.get_image_url(),
                'alt_text': image.alt_text,
                'order': image.order
            })
        
        return JsonResponse({'images': image_data})
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def portfolio(request):
    """Portfolio page view (now using Couple model)"""
    couples = Couple.objects.all().order_by('-wedding_date')
    context = {
        'couples': couples,
    }
    return render(request, 'core_app/portfolio.html', context)

def couple_detail(request, slug):
    couple = get_object_or_404(Couple, slug=slug)
    photos = couple.photos.all()
    context = {
        'couple': couple,
        'photos': photos,
    }
    return render(request, 'core_app/couple_detail.html', context)

def about(request):
    """About page view"""
    context = {
        'page_title': 'About Us',
    }
    return render(request, 'core_app/about.html', context)
