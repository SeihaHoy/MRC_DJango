from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from asgiref.sync import async_to_sync
import json
from channels.layers import get_channel_layer

from .models import Sensors, SensorData

@receiver(post_save, sender=Sensors)
def device_created(sender, instance, created, **kwargs):
    if created:
        # print("Device is created")
        # Device created signal
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"{instance.device_id}",
            {
                "type": "device.created",
                "device_id": instance.device_id,
            }
        )

@receiver(post_save, sender=SensorData)
def sensor_data_created(sender, instance, created, **kwargs):
    if created:
        # print("created Device data update", instance.device.device_id)
        # sensor_data created signal
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"{instance.device.device_id}",
            {
                "type": "sensor_data.created",
                "device_id": instance.device.device_id,
                "value": instance.value,
            }
        )

@receiver(pre_delete, sender=Sensors)
def device_deleted(sender, instance, **kwargs):
    # Device deleted signal
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"{instance.device_id}",
        {
            "type": "device.deleted",
            "device_id": instance.device_id,
        }
    )
