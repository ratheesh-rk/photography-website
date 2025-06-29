from django.core.management.base import BaseCommand
from core_app.models import InstagramReel

class Command(BaseCommand):
    help = 'Add a specific Instagram reel for testing video display'

    def handle(self, *args, **options):
        # Sample reel with video URL
        reel_data = {
            'title': 'Wedding Ceremony Highlights',
            'video_url': 'https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4',
            'thumbnail_url': 'https://picsum.photos/400/600?random=1',
            'caption': 'Beautiful moments from Sarah & John\'s wedding ceremony. Every detail was perfect!',
            'likes_count': 1247,
            'comments_count': 89,
            'views_count': 15420,
            'instagram_url': 'https://www.instagram.com/p/sample1/',
            'order': 1
        }

        reel, created = InstagramReel.objects.get_or_create(
            title=reel_data['title'],
            defaults=reel_data
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created Instagram reel: {reel.title}')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'Instagram reel already exists: {reel.title}')
            )

        self.stdout.write(
            self.style.SUCCESS(
                f'Instagram reel added successfully!\n'
                f'Title: {reel.title}\n'
                f'Likes: {reel.get_formatted_likes()}\n'
                f'Comments: {reel.get_formatted_comments()}\n'
                f'Instagram URL: {reel.instagram_url}'
            )
        ) 