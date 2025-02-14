# Generated by Django 4.2.6 on 2023-10-10 09:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("db_email_backend", "0003_auto_20220421_1249"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="email",
            options={"verbose_name": "Email Log", "verbose_name_plural": "Emails Log"},
        ),
        migrations.AlterField(
            model_name="email",
            name="bcc",
            field=models.TextField(blank=True, verbose_name="BCC"),
        ),
        migrations.AlterField(
            model_name="email",
            name="body",
            field=models.TextField(blank=True, verbose_name="Body"),
        ),
        migrations.AlterField(
            model_name="email",
            name="cc",
            field=models.TextField(blank=True, verbose_name="CC"),
        ),
        migrations.AlterField(
            model_name="email",
            name="content_subtype",
            field=models.CharField(max_length=254, verbose_name="content subtype"),
        ),
        migrations.AlterField(
            model_name="email",
            name="create_date",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Creation date"),
        ),
        migrations.AlterField(
            model_name="email",
            name="from_email",
            field=models.CharField(blank=True, max_length=254, verbose_name="From"),
        ),
        migrations.AlterField(
            model_name="email",
            name="headers",
            field=models.TextField(blank=True, verbose_name="Headers"),
        ),
        migrations.AlterField(
            model_name="email",
            name="subject",
            field=models.TextField(blank=True, verbose_name="Subject"),
        ),
        migrations.AlterField(
            model_name="email",
            name="to",
            field=models.TextField(blank=True, verbose_name="To"),
        ),
    ]
