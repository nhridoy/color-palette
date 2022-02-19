# Generated by Django 4.0.2 on 2022-02-19 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('colorApp', '0004_alter_palettemodel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('palette', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite_palette', to='colorApp.palettemodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
