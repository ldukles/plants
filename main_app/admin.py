from django.contrib import admin
from .models import Plant, Bloom, Condition, Photo
# Register your models here.
admin.site.register(Plant)
admin.site.register(Bloom)
admin.site.register(Condition)
admin.site.register(Photo)
