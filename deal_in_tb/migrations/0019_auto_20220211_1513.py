# Generated by Django 3.1.7 on 2022-02-11 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal_in_tb', '0018_auto_20211203_2331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbltransaction',
            name='status',
        ),
        migrations.RemoveField(
            model_name='tbltransaction',
            name='token',
        ),
        migrations.AlterField(
            model_name='tblstore',
            name='api_key',
            field=models.CharField(default='yEA8MDez8Bc9ETPeNaglMGtXJ49FnKQjqgKB3iyU8XVmyWz6nu', max_length=50),
        ),
    ]
