# Generated by Django 3.0 on 2021-05-14 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderRequest', '0002_auto_20210512_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='phone_number',
            field=models.IntegerField(blank=True, max_length=100, null=True, verbose_name='total Number Of Phone Lines Needed'),
        ),
    ]