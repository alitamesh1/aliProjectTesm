# Generated by Django 4.2 on 2023-06-22 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0005_alter_suggestions_user'),
        ('databaseApi', '0003_alter_data_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendStudentsSupervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=255)),
                ('email', models.CharField(max_length=255, null=True)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecommendSpervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=255)),
                ('email', models.CharField(max_length=255, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField()),
                ('serial', models.CharField(blank=True, max_length=255)),
                ('students', models.ManyToManyField(to='accounts.student')),
                ('supervisor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.supervisor')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro', models.TextField()),
                ('project_defination', models.TextField()),
                ('problems', models.TextField()),
                ('goals', models.TextField()),
                ('obstacles', models.TextField()),
                ('assumptions', models.TextField()),
                ('methodology', models.TextField()),
                ('users_char', models.TextField()),
                ('feasibility_study', models.TextField()),
                ('reqiuerments', models.TextField()),
                ('analysis', models.TextField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databaseApi.projectgroup')),
            ],
        ),
    ]
