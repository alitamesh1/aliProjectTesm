# Generated by Django 4.2 on 2023-06-22 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_suggestions_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.university'),
        ),
    ]
