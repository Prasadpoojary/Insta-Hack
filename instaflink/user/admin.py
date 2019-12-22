from django.contrib import admin
from.models import Account,Feadback

admin.site.site_header='Prasad Poojary'
# Register your models here.
admin.site.register(Account)
admin.site.register(Feadback)
