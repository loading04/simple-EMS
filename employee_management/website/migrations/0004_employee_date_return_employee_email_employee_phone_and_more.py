# Generated by Django 4.2.2 on 2023-06-13 20:23

from django.db import migrations, models
import django_enumfield.db.fields
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_rename_name_employee_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='date_return',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.CharField(default=''),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='employee',
            name='status',
            field=django_enumfield.db.fields.EnumField(default=0, enum=website.models.status),
        ),
    ]