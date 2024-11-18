from django.contrib import admin
from .models import Contact, Service, Review


admin.site.register(Service)


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display =['first_name', 'email', 'subject', 'phone']


@admin.register(Review)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'msg', 'on_list']
