# Generated by Django 2.1.2 on 2018-11-02 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20181102_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='genero',
            field=models.CharField(choices=[('', '---'), ('M', 'masculino'), ('F', 'feminino')], default='', max_length=1),
        ),
    ]
