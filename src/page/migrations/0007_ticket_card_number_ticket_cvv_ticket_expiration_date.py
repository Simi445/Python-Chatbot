# Generated by Django 5.1.1 on 2024-10-21 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='card_number',
            field=models.CharField(default='0000000000000000', max_length=16),
        ),
        migrations.AddField(
            model_name='ticket',
            name='cvv',
            field=models.CharField(default='0000', max_length=4),
        ),
        migrations.AddField(
            model_name='ticket',
            name='expiration_date',
            field=models.CharField(default='00/00', max_length=5),
        ),
    ]
