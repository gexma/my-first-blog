# Generated by Django 2.1 on 2018-08-31 09:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='catalogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_macchina', models.CharField(max_length=400)),
                ('tipo_macchina', models.CharField(max_length=200)),
                ('descrizione_macchina', models.TextField()),
                ('data_creazione', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_publicazione', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
