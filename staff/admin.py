from django.contrib import admin
from .models import Staff,AttendanceLogs,MoneyLogs

admin.site.register(AttendanceLogs)
admin.site.register(Staff)
admin.site.register(MoneyLogs)