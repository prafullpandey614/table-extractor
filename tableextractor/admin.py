from msilib.schema import Font
from django.contrib import admin

# Register your models here.
from .models import File

admin.site.register(File)
