# Generated by Django 4.2.2 on 2023-06-29 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(upload_to='images/advertisements/%Y/%m/%d/odtlVRknDgrlWf2yBbtCczMSgrsXcr.jpg', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='images/articles/%Y/%m/%d/2xYwXIb78EDRpPTM4XufXtaJndg384.jpg', verbose_name='Изображение'),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(verbose_name='Оценка')),
                ('evaluated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluated', to=settings.AUTH_USER_MODEL, verbose_name='Оцениваемый')),
                ('evaluating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluating', to=settings.AUTH_USER_MODEL, verbose_name='Оценивающий')),
            ],
            options={
                'verbose_name': 'Оценку',
                'verbose_name_plural': 'Оценки авторов объявлений',
            },
        ),
    ]