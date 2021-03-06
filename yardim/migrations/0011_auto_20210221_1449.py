# Generated by Django 3.1.2 on 2021-02-21 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yardim', '0010_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='status',
            field=models.CharField(choices=[('deleted', 'Silindi'), ('published', 'Yayinlandi'), ('draft', 'Taslak')], default='draft', max_length=10),
        ),
        migrations.CreateModel(
            name='Arsiv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
                ('sehir', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('username', models.CharField(max_length=15)),
                ('tutar', models.FloatField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
