from django.contrib import admin
from .models.user import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'nombres', 'apellidos', 'email', 'tipo_documento', 'documento', 'telefono', 'lic_cond', 'is_staff')
    list_filter = ('documento', 'lic_cond', 'nombres')
    search_fields = ('documento', 'username', 'nombres', 'lic_cond', 'apellidos')


#admin.site.register(User)
