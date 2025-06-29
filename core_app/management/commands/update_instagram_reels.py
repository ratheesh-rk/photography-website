from django.core.management.base import BaseCommand
from core_app.models import InstagramReel

class Command(BaseCommand):
    help = 'Update Instagram reel with specific Instagram link'

    def handle(self, *args, **options):
        # Update the existing reel with the real Instagram link
        reel_data = {
            'title': 'Wedding Photography Reel',
            'instagram_url': 'https://www.instagram.com/reel/DJ8SUP6yIeE/?hl=en',
            'caption': 'Beautiful wedding photography moments captured with love and care. Every frame tells a unique love story! ✨ #weddingphotography #love #photography',
            'likes_count': 2347,
            'comments_count': 156,
            'views_count': 28450,
            'order': 1
        }

        # Try to update existing reel or create new one
        try:
            reel = InstagramReel.objects.get(title__icontains='Wedding')
            reel.instagram_url = reel_data['instagram_url']
            reel.title = reel_data['title']
            reel.caption = reel_data['caption']
            reel.likes_count = reel_data['likes_count']
            reel.comments_count = reel_data['comments_count']
            reel.views_count = reel_data['views_count']
            reel.save()
            
            self.stdout.write(
                self.style.SUCCESS(f'Updated Instagram reel: {reel.title}')
            )
            self.stdout.write(
                self.style.SUCCESS(f'Instagram URL: {reel.instagram_url}')
            )
        except InstagramReel.DoesNotExist:
            # Create new reel if none exists
            reel = InstagramReel.objects.create(**reel_data)
            self.stdout.write(
                self.style.SUCCESS(f'Created new Instagram reel: {reel.title}')
            )
            self.stdout.write(
                self.style.SUCCESS(f'Instagram URL: {reel.instagram_url}')
            )

    def show_setup_instructions(self):
        """Show instructions for setting up Instagram API access"""
        instructions = """
To connect to real Instagram reels, you need to:

1. Create a Facebook App:
   - Go to https://developers.facebook.com/
   - Create a new app or use existing one
   - Add Instagram Basic Display or Instagram Graph API

2. Get Instagram Business Account ID:
   - Connect your Instagram account to Facebook Page
   - Use Graph API Explorer to get your Instagram Business Account ID

3. Generate Access Token:
   - Use Graph API Explorer with your app
   - Request permissions: instagram_basic, instagram_content_publish
   - Generate access token

4. Run this command:
   python manage.py update_instagram_reels --access-token YOUR_TOKEN --instagram-id YOUR_ID

5. For automatic updates, set up a cron job or use Celery to run this command periodically.

Note: Instagram API has rate limits and requires business/creator accounts.
        """
        self.stdout.write(instructions) 