# Generated by Django 4.0.5 on 2022-07-18 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0005_deleterequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
