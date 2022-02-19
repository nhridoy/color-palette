# Generated by Django 4.0.2 on 2022-02-19 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaletteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('palette_name', models.CharField(max_length=255)),
                ('primary_one', models.CharField(max_length=255)),
                ('primary_two', models.CharField(max_length=255)),
                ('secondary_one', models.CharField(max_length=255)),
                ('secondary_two', models.CharField(max_length=255)),
                ('secondary_three', models.CharField(max_length=255)),
                ('secondary_four', models.CharField(max_length=255)),
            ],
        ),
    ]