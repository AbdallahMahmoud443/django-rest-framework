# Generated by Django 4.2.13 on 2024-08-22 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drfproviderapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CountryName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeprtName', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='Country',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='Employee_Country', to='drfproviderapp.countries'),
        ),
        migrations.AddField(
            model_name='employee',
            name='Department',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='Employee_Department', to='drfproviderapp.departments'),
        ),
    ]
