# Generated by Django 2.1.8 on 2019-05-07 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameinfo', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=20)),
                ('num', models.CharField(max_length=20)),
                ('tel', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('wechat', models.CharField(max_length=30)),
                ('addr', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=20)),
                ('sport', models.CharField(max_length=20)),
                ('food', models.CharField(max_length=20)),
            ],
        ),
    ]
