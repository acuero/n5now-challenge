from django.contrib import admin
from core.models.configuracion import Configuracion
from core.models.persona import Persona
from core.models.marca import Marca
from core.models.vehiculo import Vehiculo
from core.models.oficial import Oficial
from core.models.infraccion import Infraccion
from core.forms import OficialCreationForm
from django.utils.html import format_html


class ConfiguracionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha_creacion', 'ultima_modificacion']
    fieldsets = (
        ('Información básica', {
            'fields': (
                ('nombre',),
            )
        }),
        ('Infracciones', {
            'fields': (
                ('dias_antiguedad_infraccion',),
            )
        }),
        ('General', {
            'fields': (
                ('observaciones',),
            )
        })
    )


class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'fecha_creacion', 'ultima_modificacion']
    fieldsets = (
        ('Información básica', {
            'fields': (
                ('nombre',),
                ('email',)
            )
        }),
        ('General', {
            'fields': (
                ('observaciones',),
            )
        })
    )


class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha_creacion', 'ultima_modificacion']
    fieldsets = (
        ('Información básica', {
            'fields': (
                ('nombre',),
            )
        }),
        ('General', {
            'fields': (
                ('observaciones',),
            )
        })
    )


class VehiculoAdmin(admin.ModelAdmin):
    list_display = ['placa_patente', 'marca', 'color_html', 'propietario', 'fecha_creacion', 'ultima_modificacion']
    fieldsets = (
        ('Información básica', {
            'fields': (
                ('placa_patente',),
                ('marca',),
                ('color',),
                ('propietario',)
            )
        }),
        ('General', {
            'fields': (
                ('observaciones',),
            )
        })
    )
    
    def color_html(self, obj):
        html = f'<div style="width: 25px; height: 25px; background-color: {obj.color};"></div>'
        return format_html(html)
    color_html.short_description = "Color"


class OficialAdmin(admin.ModelAdmin):
    #form = OficialCreationForm
    list_display = ['nombre', 'nui', 'fecha_creacion', 'ultima_modificacion']
    fieldsets = (
        ('Información básica', {
            'fields': (
                ('nombre',),
                ('nui',),
                #('password1',),
                #('password2',)
            )
        }),
        ('General', {
            'fields': (
                ('observaciones',),
            )
        })
    )

class InfraccionAdmin(admin.ModelAdmin):
    list_display = ['vehiculo', 'fecha_infraccion', 'oficial', 'fecha_creacion', 'ultima_modificacion']
    fieldsets = (
        ('Información básica', {
            'fields': (
                ('vehiculo',),
                ('fecha_infraccion',),
                ('oficial',),
            )
        }),
        ('General', {
            'fields': (
                ('observaciones',),
            )
        })
    )


# Register your models here.
admin.site.register(Configuracion, ConfiguracionAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Oficial, OficialAdmin)
admin.site.register(Infraccion, InfraccionAdmin)
