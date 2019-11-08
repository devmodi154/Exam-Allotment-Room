from django.contrib import admin
from input1.models import Student,Faculty,Course,Division,School,Branch,Booking,Department,Room

# Register your models here.
admin.site.register(Student)
admin.site.register(Division)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(School)
admin.site.register(Branch)
admin.site.register(Course)
admin.site.register(Booking)
admin.site.register(Room)