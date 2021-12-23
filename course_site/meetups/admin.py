from django.contrib import admin
from .models import Meetup,Location
# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display = ['title','location']
    list_filter = ['location',]
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title','description']


admin.site.register(Meetup,MeetupAdmin)
admin.site.register(Location)