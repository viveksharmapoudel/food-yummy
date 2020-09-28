from django.contrib import admin
from .models import UserModel,Category,Tag,Food,OurContact, MessageUs
# Register your models here.


admin.site.register([UserModel,Category,Tag,Food,OurContact,MessageUs])
