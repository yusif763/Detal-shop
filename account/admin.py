from django.contrib import admin
from account.models import *

# admin.site.register(Tours)
admin.site.register([User, Rating])

