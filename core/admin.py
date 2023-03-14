from django.contrib import admin
from .models import Testimonial


# Register your models here.
class TestimonialAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Testimonial, TestimonialAdmin)
