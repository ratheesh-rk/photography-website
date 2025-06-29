from django.core.management.base import BaseCommand
from core_app.models import InstagramReel

class Command(BaseCommand):
    help = 'Add sample Instagram reels to the database'

    def handle(self, *args, **options):
        # Sample Instagram reels data
        sample_reels = [
            {
                'title': 'Sunset Wedding Magic',
                'video_url': 'https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4',
                'caption': 'Beautiful sunset wedding moments ✨ The golden hour light was absolutely perfect for capturing these intimate moments.',
                'likes_count': 1247,
                'comments_count': 89,
                'views_count': 15420,
                'order': 1
            },
            {
                'title': 'First Dance Romance',
                'video_url': 'https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4',
                'caption': 'First dance magic 💕 Every couple has their own unique rhythm and this moment was pure poetry.',
                'likes_count': 856,
                'comments_count': 67,
                'views_count': 12340,
                'order': 2
            },
            {
                'title': 'Engagement Session Vibes',
                'video_url': 'https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4',
                'caption': 'Engagement session vibes 📸 Natural moments, genuine smiles, and lots of love in the air.',
                'likes_count': 2103,
                'comments_count': 134,
                'views_count': 18760,
                'order': 3
            },
            {
                'title': 'Behind the Scenes',
                'video_url': 'https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4',
                'caption': 'Wedding prep behind the scenes 🎬 The moments before the magic happens are just as special.',
                'likes_count': 1542,
                'comments_count': 98,
                'views_count': 14230,
                'order': 4
            }
        ]

        # Create Instagram reels
        for reel_data in sample_reels:
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
            self.style.SUCCESS('Sample Instagram reels have been added successfully!')
        ) 