from django.contrib import admin

# Register your models here.
from .models import Tag, UserStats, PostStats, TopU

class TagAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tag, TagAdmin)

class UserStatsAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserStats, UserStatsAdmin)

class PostStatsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PostStats, PostStatsAdmin)

class TopUAdmin(admin.ModelAdmin):
    pass
admin.site.register(TopU, TopUAdmin)