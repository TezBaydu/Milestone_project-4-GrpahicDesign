# Generated by Django 3.2.9 on 2021-12-01 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0004_companydetails_logo_request_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companydetails',
            name='sku',
        ),
        migrations.AlterField(
            model_name='companydetails',
            name='company_name',
            field=models.CharField(default=0, editable=False, max_length=100),
        ),
    ]
