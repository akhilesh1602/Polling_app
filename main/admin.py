from django.contrib import admin
from main import models

admin.site.register([
     models.Question,
     models.Choice
])
# Register your models here.
