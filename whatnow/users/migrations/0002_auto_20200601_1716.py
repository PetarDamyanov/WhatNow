# Generated by Django 3.0.6 on 2020-06-01 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.UsersType'),
        ),
    ]
