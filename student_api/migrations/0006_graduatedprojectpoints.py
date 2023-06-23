# Generated by Django 4.2 on 2023-06-21 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_api', '0005_delete_suggestions'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraduatedProjectPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro', models.TextField()),
                ('project_defination', models.TextField()),
                ('problems', models.TextField()),
                ('goals', models.TextField()),
                ('obstacles', models.TextField()),
                ('assumptions', models.TextField()),
                ('agile', models.TextField()),
                ('users_char', models.TextField()),
                ('feasibility_study', models.TextField()),
                ('reqiuerments', models.TextField()),
                ('analysis', models.TextField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_api.graduatedgroups')),
            ],
        ),
    ]