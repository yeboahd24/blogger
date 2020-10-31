# Generated by Django 3.1.2 on 2020-10-30 00:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(blank=True, max_length=60)),
                ('company', models.CharField(blank=True, max_length=60)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('web', models.URLField(blank=True)),
                ('description', models.TextField()),
                ('sitestatus', models.CharField(choices=[('NEW', 'New Site'), ('EX', 'Existing Site')], max_length=20)),
                ('priority', models.CharField(choices=[('U', 'Urgent - 1 week or less'), ('N', 'Normal - 2 to 4 weeks'), ('L', 'Low - Still Researching')], max_length=40)),
                ('jobfile', models.FileField(blank=True, upload_to='uploads/')),
                ('submitted', models.DateField(auto_now_add=True)),
                ('quotedate', models.DateField(blank=True, null=True)),
                ('quoteprice', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7)),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
