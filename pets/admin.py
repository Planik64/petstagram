from django.contrib import admin

from pets.models import Pet, Like



class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'age')
    list_filter = ('type', 'age')


admin.site.register(Pet, PetAdmin)
admin.site.register(Like)