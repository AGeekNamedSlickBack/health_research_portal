from django.contrib import admin

from .models import (
    Discussion,
    DiscussionReply,
    Recommends,
    Research,
    Review,
    ReviewChecklist,
)

admin.site.register(Research)
admin.site.register(Discussion)
admin.site.register(DiscussionReply)
admin.site.register(Recommends)
admin.site.register(Review)
admin.site.register(ReviewChecklist)
