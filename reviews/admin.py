from django.contrib import admin
from .models import Reviews


# Add list items to admin
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'product',
        'user',
        'rating',
        'date_posted'
    )

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"


admin.site.register(Reviews, ReviewAdmin)
