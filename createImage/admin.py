from django.contrib import admin


from .models import Image
from django.utils.safestring import mark_safe
# Register your models here.
    
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["text"]
    
    def view_image(self, image):
        if image:
            return mark_safe(f"<img src = '{image.url}' width = 200px>")
        else:
            return "No image"

        
