from django.contrib import admin
# Register your models here.
from .models import Owner, Possession, Car, License, User
admin.site.register(Owner)
admin.site.register(Possession)
admin.site.register(Car)
admin.site.register(License)
admin.site.register(User)