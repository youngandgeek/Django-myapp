from django.contrib import admin

from .models import DrinksCategory
from .models import Drinks
from .models import Booking
from .models import Employee
from .models import Menu

 #Register your models here.pass the model name to admin.site.register after importing it

admin.site.register(DrinksCategory)
admin.site.register(Drinks)
admin.site.register(Booking)
admin.site.register(Employee)
admin.site.register(Menu)