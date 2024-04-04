# Generated by Django 4.2.3 on 2024-03-27 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0012_alter_owner_back_image_alter_owner_chassis_no_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='transport_office',
        ),
        migrations.AlterField(
            model_name='owner',
            name='back_image',
            field=models.ImageField(null=True, upload_to='vehicle_images/'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='chassis_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='engine_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='front_image',
            field=models.ImageField(null=True, upload_to='vehicle_images/'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='left_image',
            field=models.ImageField(null=True, upload_to='vehicle_images/'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='rc_image',
            field=models.ImageField(null=True, upload_to='vehicle_images/'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='right_image',
            field=models.ImageField(null=True, upload_to='vehicle_images/'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='vehicle_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='year_of_registration',
            field=models.IntegerField(null=True),
        ),
    ]