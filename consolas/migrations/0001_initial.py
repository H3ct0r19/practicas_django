# Generated by Django 5.1.3 on 2024-11-30 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('memoria', models.IntegerField()),
                ('unidad_memoria', models.CharField(choices=[('Mb', 'Mb'), ('Gb', 'Gb'), ('Tb', 'Tb')], max_length=2)),
                ('ram', models.IntegerField()),
                ('unidad_ram', models.CharField(choices=[('Mb', 'Mb'), ('Gb', 'Gb'), ('Tb', 'Tb')], max_length=2)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
