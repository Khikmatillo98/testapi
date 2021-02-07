from django.contrib import admin
from .models import Poll, Choice, Vote 

# Register your models here.


class PollAdmin(admin.ModelAdmin):
    list_display = ['question', 'created_by', 'pub_date']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)