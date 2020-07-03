from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import fields, resources
from import_export.formats import base_formats
from import_export.widgets import ForeignKeyWidget, DateTimeWidget
from .models import Shop, Coupon


class ShopResource(resources.ModelResource):
    class Meta:
        model = Shop
        exclude = ('id',)
        import_id_fields = ('title',)


class ShopAdmin(ImportExportModelAdmin):
    resource_class = ShopResource

    def get_export_formats(self):
        """
        Returns available export formats.
        """
        formats = (
            base_formats.CSV,
        )
        return [f for f in formats if f().can_export()]

    def get_import_formats(self):
        """
        Returns available import formats.
        """
        formats = (
            base_formats.CSV,
        )
        return [f for f in formats if f().can_import()]


admin.site.register(Shop, ShopAdmin)


class CouponResource(resources.ModelResource):
    # shop = fields.Field(
    #     widget=ForeignKeyWidget(Shop, 'title'))
    number = fields.Field(
        column_name='number',
        attribute='number')
    deadline = fields.Field(
        column_name='deadline',
        attribute='deadline',
        widget=DateTimeWidget("%d-%m-%Y %H:%M:%S"))
    used = fields.Field(
        column_name='used',
        attribute='used',
        saves_null_values=True,
        default=None,
        widget=DateTimeWidget("%d-%m-%Y %H:%M:%S"))
    shop = fields.Field(
        column_name='shop',
        attribute='shop',
        widget=ForeignKeyWidget(Shop, 'title'))

    class Meta:
        model = Coupon
        exclude = ('id',)
        import_id_fields = ('number', 'deadline', 'used', 'shop',)
        # fields = ('shop',)
        widgets = {
            'deadline': {'format': '%d/%m/%Y'},
            'used': {'format': '%d/%m/%Y'},
        }




class CouponAdmin(ImportExportModelAdmin):
    resource_class = CouponResource

    list_display = ('number', 'deadline', 'used', 'shop')
    list_display_links = ('number',)
    list_editable = ('deadline', 'used', 'shop',)

    def get_export_formats(self):
        """
        Returns available export formats.
        """
        formats = (
            base_formats.CSV,
        )
        return [f for f in formats if f().can_export()]

    def get_import_formats(self):
        """
        Returns available import formats.
        """
        formats = (
            base_formats.CSV,
        )
        return [f for f in formats if f().can_import()]


admin.site.register(Coupon, CouponAdmin)

