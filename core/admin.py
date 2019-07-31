from django.contrib import admin
from core.models import Room

# Registered Models

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass