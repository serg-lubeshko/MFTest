from django.contrib import admin

from loan import models

admin.site.register(models.Product)
admin.site.register(models.Contract)
admin.site.register(models.Manufacturer)
admin.site.register(models.CreditApplication)
admin.site.register(models.CreditApplicationProduct)