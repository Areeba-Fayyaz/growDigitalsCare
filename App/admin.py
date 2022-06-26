from django.contrib import admin
from App.models import portfolioTable
from App.models import customerTable
# Register your models here.
admin.site.register(portfolioTable)
admin.site.register(customerTable)
