from django.contrib import admin
from .models import Staff,AttendanceLogs

admin.site.register(AttendanceLogs)
admin.site.register(Staff)