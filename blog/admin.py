from django.contrib import admin
from .models import Post, Bebidas, Alimentos, Accesorios, Limpieza
from import_export.admin import ImportExportModelAdmin

admin.site.register(Post)
admin.site.register(Bebidas)
admin.site.register(Alimentos)
admin.site.register(Accesorios)
admin.site.register(Limpieza)


class ViewAdmin(ImportExportModelAdmin):
    pass
