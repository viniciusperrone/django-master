from django.contrib import admin
from ai.models import AIResult


class AIResultAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'result')


admin.site.register(AIResult, AIResultAdmin)
