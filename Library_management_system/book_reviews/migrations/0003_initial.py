# Generated by Django 4.1.7 on 2024-08-27 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("book_reviews", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="reviews",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_review",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
