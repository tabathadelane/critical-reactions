# Generated by Django 3.0.3 on 2020-02-14 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('who', models.TextField(blank=True, default='', max_length=300, null=True)),
                ('what', models.TextField(blank=True, default='', max_length=300, null=True)),
                ('why', models.TextField(blank=True, default='', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('race', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('dndclass', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('specialty', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('title', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('interests', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('bio', models.TextField(blank=True, default='', max_length=300, null=True)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p', to='crit_app.Party')),
            ],
        ),
    ]
