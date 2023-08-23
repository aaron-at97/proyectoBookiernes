# Generated by Django 3.0.14 on 2021-06-01 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eBook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('Writer', 'Writer'), ('Editor', 'Editor'), ('Editor in chief', 'Editor in chief'), ('Chief designer', 'Chief designer'), ('Designer', 'Designer'), ('CTO', 'CTO'), ('Developer', 'Developer'), ('Client', 'Client')], max_length=25, verbose_name='Role')),
                ('nombre', models.CharField(max_length=64)),
                ('apellido', models.CharField(max_length=64)),
                ('telefon', models.IntegerField()),
                ('codi_postal', models.IntegerField()),
                ('correo', models.CharField(max_length=64)),
                ('direccion', models.CharField(max_length=64)),
                ('notification', models.ManyToManyField(blank=True, to='eBook.Notification')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
