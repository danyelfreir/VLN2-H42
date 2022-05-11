from django.contrib import admin
from .models import *

admin.site.register(User_info)
admin.site.register(Payment_info)
admin.site.register(Address_info)
admin.site.register(User_rating)
admin.site.register(Notification)