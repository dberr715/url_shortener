# Generated by Django 4.2.6 on 2023-10-23 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('url_short_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urldata',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='url_short_app.userdata'),
        ),
    ]
