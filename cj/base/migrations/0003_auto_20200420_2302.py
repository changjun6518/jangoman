# Generated by Django 3.0.5 on 2020-04-20 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20200419_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='books', to='base.Language'),
        ),
        migrations.AlterField(
            model_name='language',
            name='language',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='page',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='base.Book'),
        ),
    ]