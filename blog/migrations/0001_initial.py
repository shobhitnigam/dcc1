# Generated by Django 3.2.3 on 2021-05-30 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gametype', models.CharField(max_length=100)),
                ('team1', models.CharField(max_length=100)),
                ('team2', models.CharField(max_length=100)),
                ('mdate', models.DateTimeField(auto_now=False, auto_now_add=False)),
                ('cfee', models.DecimalField(decimal_places=10, max_digits=20)),
            ],
        ),
    ]