from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("device_monitoring", "0010_map"),
    ]

    operations = [
        migrations.AddField(
            model_name="wifisession",
            name="hostname",
            field=models.CharField(
                blank=True,
                default="",
                help_text="as reported by the DHCP leases of the device",
                max_length=255,
                verbose_name="hostname",
            ),
        ),
        migrations.AddField(
            model_name="wifisession",
            name="ip_address",
            field=models.GenericIPAddressField(
                blank=True,
                help_text="as reported by the DHCP leases of the device",
                null=True,
                verbose_name="IP address",
            ),
        ),
    ]
