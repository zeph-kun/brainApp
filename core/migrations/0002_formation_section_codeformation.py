# Generated by Django 4.1.5 on 2023-01-12 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=300)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('price', models.FloatField()),
                ('status', models.BooleanField()),
                ('tag', models.CharField(max_length=50)),
                ('id_catalogue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.catalogue')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.CharField(max_length=250)),
                ('is_active', models.BooleanField()),
                ('id_formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.formation')),
            ],
        ),
        migrations.CreateModel(
            name='CodeFormation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True)),
                ('id_formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.formation')),
            ],
        ),
    ]