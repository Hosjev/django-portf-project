# Generated by Django 3.1.4 on 2021-02-07 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('creation_date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='images/blog')),
                ('body', models.TextField()),
            ],
        ),
    ]
