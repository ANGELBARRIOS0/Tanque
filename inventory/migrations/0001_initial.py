# Generated by Django 3.0.6 on 2020-05-30 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accesorios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchase'), ('SOLD', 'Item Sold'), ('RESTOCKING', 'Item restocking in few days')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Alimentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchase'), ('SOLD', 'Item Sold'), ('RESTOCKING', 'Item restocking in few days')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bebidas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchase'), ('SOLD', 'Item Sold'), ('RESTOCKING', 'Item restocking in few days')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Limpieza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchase'), ('SOLD', 'Item Sold'), ('RESTOCKING', 'Item restocking in few days')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
