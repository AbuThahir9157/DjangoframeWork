from django.contrib import admin
from .models import Department,Doctors,Bokking
admin.site.register(Department)
admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','p_name','p_phone','p_phone','p_email','doc_name','booking_date','booked_on')
admin.site.register(Bokking,BookingAdmin)


# Register your models here.
