from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import Package, Review, UserProfile, VillaReport, Comment
from django.utils import timezone


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        # Create sample packages
        packages_data = [
            {
                'name': 'Essential Care',
                'package_type': 'weekly',
                'description': 'Basic maintenance and care services for your luxury villa.',
                'price': 299.00,
                'features': 'Weekly maintenance check\nGarden care\nPool maintenance\nBasic security monitoring',
                'is_featured': False
            },
            {
                'name': 'Premium Care',
                'package_type': 'monthly',
                'description': 'Comprehensive care package with enhanced services and priority support.',
                'price': 1199.00,
                'features': 'Daily maintenance check\nPremium landscaping\nPool & spa maintenance\n24/7 security monitoring\nConcierge services\nPriority emergency response',
                'is_featured': True
            },
            {
                'name': 'Luxury Care',
                'package_type': 'yearly',
                'description': 'Ultimate luxury villa care with white-glove service and exclusive benefits.',
                'price': 12999.00,
                'features': '24/7 on-site maintenance\nPremium landscaping & design\nPool & spa management\nAdvanced security systems\nFull concierge services\nEvent planning & management\nProperty management\nExclusive member benefits',
                'is_featured': True
            }
        ]

        for package_data in packages_data:
            package, created = Package.objects.get_or_create(
                name=package_data['name'],
                defaults=package_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created package: {package.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Package already exists: {package.name}')
                )

        # Create sample reviews
        reviews_data = [
            {
                'name': 'Sarah Johnson',
                'rating': 5,
                'comment': 'VillaCare has transformed our property management experience. Their attention to detail and professionalism is unmatched.',
                'is_approved': True
            },
            {
                'name': 'Michael Chen',
                'rating': 5,
                'comment': 'The luxury care package exceeded all our expectations. Our villa has never looked better!',
                'is_approved': True
            },
            {
                'name': 'Emma Williams',
                'rating': 5,
                'comment': 'Outstanding service and reliability. VillaCare has become an essential part of our villa ownership experience.',
                'is_approved': True
            },
            {
                'name': 'David Rodriguez',
                'rating': 4,
                'comment': 'Excellent service with professional staff. The premium package is worth every penny.',
                'is_approved': True
            },
            {
                'name': 'Lisa Thompson',
                'rating': 5,
                'comment': 'VillaCare made our villa management effortless. Highly recommend their services!',
                'is_approved': True
            },
            {
                'name': 'Robert Kim',
                'rating': 5,
                'comment': 'The best villa care service we have ever used. Professional, reliable, and luxurious.',
                'is_approved': True
            }
        ]

        for review_data in reviews_data:
            review, created = Review.objects.get_or_create(
                name=review_data['name'],
                comment=review_data['comment'],
                defaults=review_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created review: {review.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Review already exists: {review.name}')
                )

        # Create sample user and villa reports
        try:
            # Create a test user if it doesn't exist
            test_user, created = User.objects.get_or_create(
                username='testuser',
                defaults={
                    'email': 'test@villacare.com',
                    'first_name': 'John',
                    'last_name': 'Doe'
                }
            )
            if created:
                test_user.set_password('testpass123')
                test_user.save()
                self.stdout.write(
                    self.style.SUCCESS('Created test user: testuser (password: testpass123)')
                )
            
            # Create user profile
            user_profile, created = UserProfile.objects.get_or_create(
                user=test_user,
                defaults={
                    'phone': '+1 (555) 123-4567',
                    'address': '123 Luxury Lane, Premium District',
                    'villa_address': '456 Villa Road, Exclusive Area',
                    'villa_type': 'Modern Beachfront Villa',
                    'subscription_package': Package.objects.filter(name='Premium Care').first()
                }
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS('Created user profile for test user')
                )
            
            # Create sample villa reports
            villa_reports_data = [
                {
                    'user': test_user,
                    'report_type': 'maintenance',
                    'priority': 'high',
                    'title': 'Air Conditioning Not Working',
                    'description': 'The AC unit in the master bedroom is not cooling properly. It makes strange noises and only blows warm air.',
                    'location': 'Master Bedroom',
                    'status': 'in_progress'
                },
                {
                    'user': test_user,
                    'report_type': 'cleaning',
                    'priority': 'medium',
                    'title': 'Deep Clean Request',
                    'description': 'Need a deep cleaning service for the entire villa, especially the kitchen and bathrooms.',
                    'location': 'Entire Villa',
                    'status': 'pending'
                },
                {
                    'user': test_user,
                    'report_type': 'pool',
                    'priority': 'low',
                    'title': 'Pool Maintenance',
                    'description': 'Regular pool maintenance and chemical balance check needed.',
                    'location': 'Pool Area',
                    'status': 'completed'
                }
            ]
            
            for report_data in villa_reports_data:
                report, created = VillaReport.objects.get_or_create(
                    user=report_data['user'],
                    title=report_data['title'],
                    defaults=report_data
                )
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f'Created villa report: {report.title}')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'Villa report already exists: {report.title}')
                    )
            
            # Create sample comments
            comments_data = [
                {
                    'villa_report': VillaReport.objects.filter(title='Air Conditioning Not Working').first(),
                    'user': test_user,
                    'comment': 'Thank you for creating this report. The AC has been making strange noises for a few days now.',
                    'is_admin_comment': False
                },
                {
                    'villa_report': VillaReport.objects.filter(title='Air Conditioning Not Working').first(),
                    'user': User.objects.filter(is_staff=True).first(),
                    'comment': 'We have scheduled a technician to visit tomorrow at 10 AM. They will check the AC unit and provide a solution.',
                    'is_admin_comment': True
                },
                {
                    'villa_report': VillaReport.objects.filter(title='Deep Clean Request').first(),
                    'user': test_user,
                    'comment': 'The villa needs a thorough cleaning, especially the kitchen and bathrooms.',
                    'is_admin_comment': False
                }
            ]
            
            for comment_data in comments_data:
                if comment_data['villa_report'] and comment_data['user']:
                    comment, created = Comment.objects.get_or_create(
                        villa_report=comment_data['villa_report'],
                        user=comment_data['user'],
                        comment=comment_data['comment'],
                        defaults=comment_data
                    )
                    if created:
                        self.stdout.write(
                            self.style.SUCCESS(f'Created comment for: {comment.villa_report.title}')
                        )
                    else:
                        self.stdout.write(
                            self.style.WARNING(f'Comment already exists for: {comment.villa_report.title}')
                        )
                    
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating sample user data: {e}')
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample data!')
        )
