from django.contrib import admin
from contact_us.models import ContactModel
# Register your models here.
class ContactModelAdmin(admin.ModelAdmin):
    list_display=['name','phone','phone']
admin.site.register(ContactModel,ContactModelAdmin)