# Generated by Django 4.1.1 on 2024-06-30 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id_navbar', models.AutoField(db_column='idNavbar', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
    ]
