# Generated by Django 5.0 on 2023-12-18 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(choices=[('Manager', 'Manager'), ('Supervisor', 'Supervisor'), ('Staff', 'Staff')], max_length=20)),
                ('basic_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bonus', models.BooleanField(default=False)),
            ],
        ),
    ]