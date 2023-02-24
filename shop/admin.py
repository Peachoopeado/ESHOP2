from django.contrib import admin
from .models import Category, VehicleType, OilType, Compound, Viscosity, Fuel, Transmission, Product, Filter, Purpose, Params


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['filt']


admin.site.register(Category, CategoryAdmin)


class VehicleTypeAdmin(admin.ModelAdmin):
    filter_horizontal = ['pars']

admin.site.register(VehicleType, VehicleTypeAdmin)


class OilTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['pars']


admin.site.register(OilType, OilTypeAdmin)


class CompoundAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['pars']


admin.site.register(Compound, CompoundAdmin)


class ViscosityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['pars']


admin.site.register(Viscosity, ViscosityAdmin)


class FuelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['pars']

admin.site.register(Fuel, FuelAdmin)


class TransmissionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['pars']

admin.site.register(Transmission, TransmissionAdmin)
class PurposeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    filter_horizontal = ['pars']
admin.site.register(Purpose, PurposeAdmin)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'vehicle_type', 'oiltype','transmission', 'viscosity', 'compound', 'fuel','price', 'stock', 'available']
    list_editable = ['price']


admin.site.register(Product, ProductAdmin)
class FilterAdmin(admin.ModelAdmin):
    filter_horizontal = ['pars']
admin.site.register(Filter, FilterAdmin)
admin.site.register(Params)