from django.db import models

class Advertisement(models.Model):
    TIER_CHOICES = (
        ('Basic', 'Basic'),
        ('Recommended', 'Recommended'),
        ('Premium', 'Premium'),
    )
    tier = models.CharField(max_length=20, choices=TIER_CHOICES)
    brand_name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='advertisements/', null=True, blank=True)
    # Add more fields as needed
