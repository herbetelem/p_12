# Generated by Django 4.2.2 on 2023-06-27 06:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contract', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('attendees', models.IntegerField()),
                ('event_date', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField()),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contract.client')),
                ('event_status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.eventstatus')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
