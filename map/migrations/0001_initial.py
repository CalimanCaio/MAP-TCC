# Generated by Django 4.2.6 on 2023-10-22 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Methodology',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
                migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('methodology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.methodology')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('acitivities', models.ManyToManyField(on_delete=django.db.models.deletion.CASCADE, to='map.activities')),
            ],
        ),
    ]
