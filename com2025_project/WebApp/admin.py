from django.contrib import admin
from .models import courses,users,modules,user_modules
# Register your models here.


admin.site.register(courses)
admin.site.register(users)
admin.site.register(modules)
admin.site.register(user_modules)