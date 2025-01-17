from django.contrib import admin
from .models import MyTypingTestRecord, Contact

# Register your models here.

# Admin customization for ImageUploaderUser
class MyTypingTestRecordAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_login') # Display username and last login in the admin list

# Register ImageUploaderUser model
admin.site.register(MyTypingTestRecord, MyTypingTestRecordAdmin)

# Register the Contact model
admin.site.register(Contact)