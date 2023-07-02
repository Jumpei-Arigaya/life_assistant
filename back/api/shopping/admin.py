from django.contrib import admin
from api.shopping.models import *

# Register your models here.
admin.site.register([Receipt, ReceiptDetail, Shopping])
