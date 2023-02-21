from django.contrib import admin
from .models import Category, OilType, Compound, Viscosity, Fuel, Transmission, Product


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class OilTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(OilType, OilTypeAdmin)


class CompoundAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Compound, CompoundAdmin)


class ViscosityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Viscosity, ViscosityAdmin)


class FuelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Fuel, FuelAdmin)


class TransmissionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Transmission, TransmissionAdmin)

admin.site.register(Product)
