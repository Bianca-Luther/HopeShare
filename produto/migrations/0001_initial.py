# Generated by Django 4.2.1 on 2023-05-15 22:50

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
                ('nome', models.CharField(max_length=255)),
                ('descricao_curta', models.TextField(max_length=255)),
                ('descricao_longa', models.TextField()),
                ('imagem', models.ImageField(upload_to='produto_imagens/%Y/%m/')),
                ('slug', models.SlugField(unique=True)),
                ('preco', models.FloatField()),
            ],
        ),
    ]