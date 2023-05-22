# Generated by Django 4.1.7 on 2023-05-15 01:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='cod',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='chamado',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]