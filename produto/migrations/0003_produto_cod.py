# Generated by Django 4.1.7 on 2023-03-06 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_rename_descrição_produto_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='cod',
            field=models.IntegerField(default=6, editable=False),
        ),
    ]
