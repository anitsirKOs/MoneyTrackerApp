# Generated by Django 3.1.7 on 2021-03-07 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('expenses', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('income', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('expenses_type', models.CharField(choices=[('Food', 'Food'), ('House', 'House'), ('Car', 'Car'), ('Health', 'Health'), ('Clothes', 'Clothes')], default='', max_length=25)),
                ('income_type', models.CharField(choices=[('Salary', 'Salary'), ('Savings', 'Savings')], default='', max_length=25)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
