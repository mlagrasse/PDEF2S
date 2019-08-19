# Generated by Django 2.1.7 on 2019-08-05 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pde', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pde',
            old_name='ip',
            new_name='destination_ip',
        ),
        migrations.RemoveField(
            model_name='pde',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='pde',
            name='exe',
        ),
        migrations.RemoveField(
            model_name='pde',
            name='machine',
        ),
        migrations.AddField(
            model_name='pde',
            name='destination_mac',
            field=models.CharField(default='0.0.0.0', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pde',
            name='source_ip',
            field=models.CharField(default='0.0.0.0', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pde',
            name='source_mac',
            field=models.CharField(default='aa:aa:aa:aa:aa:aa', max_length=16),
            preserve_default=False,
        ),
    ]