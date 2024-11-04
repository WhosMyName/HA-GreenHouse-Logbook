"""_summary_
"""

# https://developers.home-assistant.io/docs/core/entity

from homeassistant.components.camera import CameraEntity
from homeassistant.components.sensor import SensorEntity
from homeassistant.components.datetime import DateTimeEntity
from homeassistant.components.text import TextEntity, TextEntityDescription
from homeassistant.components.todo import TodoListEntity, TodoItem, TodoItemStatus
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity, AlarmControlPanelEntityDescription, AlarmControlPanelEntityFeature, AlarmControlPanelState


# thoughts:

# CameraEntity:
# to select a image-capturing input device
# and use some whacky bounding box to select specific plants and zoom into bbox
# daily/hourly images of plants ->
# maybe timelapses

# SensorEntity:
# for Humidity, AirQuality, Temperature, Pressure, EC, pH, ....

# DateTimeEntity
# to set dates (????)

# TextEntity:
# [in hopes MD can be used]
# to enter extra info, e.g. fertilizer usage/type, pest control, plant changes, etc....

# TodoListEntity:
# checkboxes for watering, fertilizing, pest control, trimming

# some calendar entity -> calndar button -> popup calendar
# for displaying a calendar

# AlarmControlPanelEntity:
# set timeframe and alarm the user if plant hasn't been watered within of the timeframe
# plant state on time schedule -> Seed -> Seedling -> Young plant -> Flower -> Fruits


class Plant(CameraEntity, ):

    def __init__(self) -> None:
        super().__init__()
        self.should_poll = False
        self.device_class = str()
        self.has_entity_name = True
        self.name = ""
        self.supported_features = int()

    @property
    def icon(self) -> str | None:
        """Icon of the entity."""
        return "mdi:pine-tree"