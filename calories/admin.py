from django.contrib import admin

from .models import *


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)


admin.site.register(Food)
admin.site.register(Profile)
admin.site.register(PostFood)
