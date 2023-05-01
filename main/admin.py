from django.contrib import admin
from main import models

admin.site.register([
     models.Question,
     models.Choice,
     models.Answer
])
# Register your models here.
