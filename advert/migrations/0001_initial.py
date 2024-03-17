# Generated by Django 5.0.3 on 2024-03-16 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier', models.CharField(choices=[('Basic', 'Basic'), ('Recommended', 'Recommended'), ('Premium', 'Premium')], max_length=20)),
                ('brand_name', models.CharField(max_length=100)),
                ('display_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='advertisements/')),
            ],
        ),
    ]
