# Generated by Django 4.2 on 2023-06-22 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_student_university'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.university'),
        ),
    ]