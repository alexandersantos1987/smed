# Generated by Django 3.1.7 on 2021-03-15 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tematica', models.CharField(max_length=255)),
                ('responsavel', models.CharField(max_length=255)),
                ('data', models.DateTimeField()),
                ('carga', models.IntegerField(default=4)),
                ('ativa', models.BooleanField(default=True)),
                ('img_url', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('presenca', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Formações',
            },
        ),
    ]
