# Generated by Django 5.0.6 on 2024-07-03 11:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_message"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="otp",
            name="User",
        ),
        migrations.AddField(
            model_name="otp",
            name="is_verified",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="otp",
            name="otp",
            field=models.CharField(max_length=6),
        ),
        migrations.AddField(
            model_name="otp",
            name="user",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
