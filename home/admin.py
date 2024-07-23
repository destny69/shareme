from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Folder)
admin.site.register(Files)
admin.site.register(Textdata)
admin.site.register(PublicFiles)
admin.site.register(PrivateFiles)
admin.site.register(PublicText)
admin.site.register(PrivateText)
