# Generated by Django 4.1.7 on 2023-02-27 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('descrição', models.TextField()),
                ('quantidade', models.IntegerField(default=0)),
            ],
        ),
    ]