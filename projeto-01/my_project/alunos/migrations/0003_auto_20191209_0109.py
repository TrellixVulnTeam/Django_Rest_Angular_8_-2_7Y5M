# Generated by Django 3.0 on 2019-12-09 04:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0002_auto_20191209_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='ano_nasc',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1970), django.core.validators.MaxValueValidator(2019)]),
        ),
    ]