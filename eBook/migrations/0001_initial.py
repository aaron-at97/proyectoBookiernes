# Generated by Django 3.0.14 on 2021-06-01 12:21

import datetime
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
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_book', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=64)),
                ('genere', models.CharField(max_length=64, null=True)),
                ('body', models.TextField()),
                ('deleted', models.BooleanField(default=False)),
                ('date', models.DateField(default=datetime.date.today)),
                ('state', models.PositiveIntegerField(choices=[(0, 'Presented'), (1, 'Accepted'), (2, 'Denied'), (3, 'Revision'), (4, 'Pending images'), (5, 'Images accepted'), (6, 'Images denied'), (7, 'Pending layout'), (8, 'Layout accepted'), (9, 'Layout denied'), (10, 'Translate'), (11, 'Published')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concept', models.TextField(max_length=100)),
                ('seen', models.BooleanField(default=False)),
                ('date', models.DateField(default=datetime.date.today)),
                ('book_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eBook.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('Writer', 'Writer'), ('Editor', 'Editor'), ('Editor in chief', 'Editor in chief'), ('Chief designer', 'Chief designer'), ('Designer', 'Designer'), ('CTO', 'CTO'), ('Developer', 'Developer'), ('Client', 'Client')], max_length=25, verbose_name='Role')),
                ('books', models.ManyToManyField(blank=True, to='eBook.Book')),
                ('notification', models.ManyToManyField(blank=True, to='eBook.Notification')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EditorChief',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('Writer', 'Writer'), ('Editor', 'Editor'), ('Editor in chief', 'Editor in chief'), ('Chief designer', 'Chief designer'), ('Designer', 'Designer'), ('CTO', 'CTO'), ('Developer', 'Developer'), ('Client', 'Client')], max_length=25, verbose_name='Role')),
                ('notification', models.ManyToManyField(blank=True, to='eBook.Notification')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('Writer', 'Writer'), ('Editor', 'Editor'), ('Editor in chief', 'Editor in chief'), ('Chief designer', 'Chief designer'), ('Designer', 'Designer'), ('CTO', 'CTO'), ('Developer', 'Developer'), ('Client', 'Client')], max_length=25, verbose_name='Role')),
                ('assigned', models.ManyToManyField(blank=True, to='eBook.Book')),
                ('notification', models.ManyToManyField(blank=True, to='eBook.Notification')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('Writer', 'Writer'), ('Editor', 'Editor'), ('Editor in chief', 'Editor in chief'), ('Chief designer', 'Chief designer'), ('Designer', 'Designer'), ('CTO', 'CTO'), ('Developer', 'Developer'), ('Client', 'Client')], max_length=25, verbose_name='Role')),
                ('notification', models.ManyToManyField(blank=True, to='eBook.Notification')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('Writer', 'Writer'), ('Editor', 'Editor'), ('Editor in chief', 'Editor in chief'), ('Chief designer', 'Chief designer'), ('Designer', 'Designer'), ('CTO', 'CTO'), ('Developer', 'Developer'), ('Client', 'Client')], max_length=25, verbose_name='Role')),
                ('notification', models.ManyToManyField(blank=True, to='eBook.Notification')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CTO',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('Writer', 'Writer'), ('Editor', 'Editor'), ('Editor in chief', 'Editor in chief'), ('Chief designer', 'Chief designer'), ('Designer', 'Designer'), ('CTO', 'CTO'), ('Developer', 'Developer'), ('Client', 'Client')], max_length=25, verbose_name='Role')),
                ('notification', models.ManyToManyField(blank=True, to='eBook.Notification')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChiefDesigner',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('Writer', 'Writer'), ('Editor', 'Editor'), ('Editor in chief', 'Editor in chief'), ('Chief designer', 'Chief designer'), ('Designer', 'Designer'), ('CTO', 'CTO'), ('Developer', 'Developer'), ('Client', 'Client')], max_length=25, verbose_name='Role')),
                ('notification', models.ManyToManyField(blank=True, to='eBook.Notification')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]