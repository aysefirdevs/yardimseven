# Generated by Django 3.1.2 on 2020-12-26 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yardim', '0004_auto_20201226_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='status',
            field=models.CharField(choices=[('deleted', 'Silindi'), ('published', 'Yayinlandi'), ('draft', 'Taslak')], default='draft', max_length=10),
        ),
    ]
