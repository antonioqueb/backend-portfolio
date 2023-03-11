from django.contrib import admin

# Register your models here.

@admin.register(DeveloperProfile)
class DeveloperProfileAdmin(admin.ModelAdmin):
    list_display = '__all__'
    list_display_links = '__all__'
    list_filter = '__all__'
    