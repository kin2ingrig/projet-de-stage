# Generated by Django 4.1.5 on 2023-10-24 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0002_compteop_agence'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='bordereauop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='controle.bordereauop'),
        ),
    ]
