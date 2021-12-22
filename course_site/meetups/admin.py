from django.contrib import admin
from .models import Meetup
# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display = ['title',]
    # list_filter = ['']
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title','description']


admin.site.register(Meetup,MeetupAdmin)