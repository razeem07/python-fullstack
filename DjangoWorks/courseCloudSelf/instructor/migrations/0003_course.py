# Generated by Django 5.1.5 on 2025-01-28 07:00

import django.db.models.deletion
import embed_video.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_free', models.BooleanField(default=False)),
                ('picture', models.ImageField(blank=True, default='courseimages/default.png', null=True, upload_to='courseimages')),
                ('thumbnail', embed_video.fields.EmbedVideoField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_objects', models.ManyToManyField(to='instructor.category')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
