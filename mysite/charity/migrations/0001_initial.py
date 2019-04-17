# Generated by Django 2.1.7 on 2019-04-16 05:16

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('organization', models.CharField(default='deargoodpeople', max_length=100)),
                ('hours', models.FloatField(default=0)),
                ('date', models.CharField(default='2019-04-16', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('charity_list', models.CharField(default='Volunteers_Home', max_length=100)),
                ('number_hours', models.FloatField(default=0)),
            ],
            options={
                'ordering': ['last_name'],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
