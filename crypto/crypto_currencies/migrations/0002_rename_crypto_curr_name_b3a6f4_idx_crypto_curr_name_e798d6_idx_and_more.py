# Generated by Django 4.2.3 on 2023-07-18 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_currencies', '0001_initial'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='crypto',
            new_name='crypto_curr_name_e798d6_idx',
            old_name='crypto_curr_name_b3a6f4_idx',
        ),
        migrations.AlterModelTable(
            name='crypto',
            table='crypto_currencies',
        ),
    ]