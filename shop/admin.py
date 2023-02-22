from django.contrib import admin
from .models import Category, VehicleType, OilType, Compound, Viscosity, Fuel, Transmission, Product


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['vehicle_type', 'oiltype', 'transmission', 'viscosity', 'compound', 'fuel']


admin.site.register(Category, CategoryAdmin)


class VehicleTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(VehicleType)


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


class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'vehicle_type', 'oiltype','transmission', 'viscosity', 'compound', 'fuel','price', 'stock', 'available']
    list_editable = ['price']


admin.site.register(Product, ProductAdmin)
