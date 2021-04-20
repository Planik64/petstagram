# Generated by Django 3.1.5 on 2021-04-04 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat'), ('parrot', 'Parrot'), ('unknown', 'Unknown')], default='unknown', max_length=7)),
                ('name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='public/pets')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.pet')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='no name', max_length=30)),
                ('text', models.TextField()),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.pet')),
            ],
        ),
    ]
