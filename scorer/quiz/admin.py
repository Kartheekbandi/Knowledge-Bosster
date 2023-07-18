from django.contrib import admin
from .models import Questions,MATQuestions,GKQuestions

# Register your models here.

admin.site.register(Questions)
admin.site.register(MATQuestions)
admin.site.register(GKQuestions)
