from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(BusinessRegister)
admin.site.register(IndividualRegister)
admin.site.register(AnotherJoinAccountRegister)
admin.site.register(Product)
admin.site.register(SubProduct)
admin.site.register(Contact)
admin.site.register(Subscriber)
admin.site.register(HomeInfoSection)
admin.site.register(AboutInfoSection)
admin.site.register(Quote)

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','ordered_date','updated']
