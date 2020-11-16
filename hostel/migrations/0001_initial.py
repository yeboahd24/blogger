# Generated by Django 3.1.2 on 2020-11-11 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(help_text='name', max_length=100)),
                ('Gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], help_text='gender', max_length=100)),
                ('Email', models.EmailField(help_text='email', max_length=254)),
                ('Program', models.CharField(help_text='program', max_length=100)),
                ('Room', models.CharField(help_text='room number', max_length=100)),
                ('Image', models.ImageField(upload_to='images', verbose_name='image')),
            ],
        ),
    ]
