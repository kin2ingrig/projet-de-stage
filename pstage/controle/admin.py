from django.contrib import admin
from controle.models import *
# from django.contrib.admin.widgets import AdminDateWidget


# admin.site.register(Agence)
admin.site.register(Agent)
admin.site.register(Client)

@admin.register(BordereauOp)
class BordereauOp(admin.ModelAdmin):
    list_display=('date_format','date', 'idtransfer', 'id_six',  'msisdn', 'number', 'statement','num','amount', 'credit', 'debit', 'fees', 'post', 'operateur', 'agence')
    list_per_page = 10
    list_filter = ('idtransfer','date')
    # odering = ('date',)
    # formfield_overrides = {
    #     models.DateField: {'widget': AdminDateWidget(attrs={'type': 'date'})},
    # }
    # search_fields = ('idtransfer','date', 'operateur', 'agence',)
    def id_six(self, obj):
        # Assurez-vous de remplacer 'my_field' par le nom du champ contenant la chaîne complète
        full_string = obj.idtransfer
        return full_string[-6:] if full_string else ''  # Récupère les 6 derniers caractères
    id_six.short_description = 'identifianttrans'
    
    def date_format(self, obj):
        return obj.date.strftime("%d/%m/%Y")

    date_format.short_description = 'date'
    
    def num(self, n):
        full_string = n.statement
        return full_string[-8:] if full_string else ''
    num.short_description = 'telephone'
# admin.site.register(Operation)
@admin.register(Operation)
class Operation(admin.ModelAdmin):
    list_display=('date', 'montant', 'refOp', 'service', 'agence', 'typeOp', 'client', 'operateur', 'agent', 'caisse')
    list_filter= ('refOp', 'date')
    
admin.site.register(Operateur)
admin.site.register(Approvisionnement)
admin.site.register(Nature)
admin.site.register(Orion)
admin.site.register(Direction)
admin.site.register(CompteOp)
# admin.site.register(Consolidation)
admin.site.register(TypeOperation)
admin.site.register(Caisse)
admin.site.register(Service)
admin.site.register(Fonction)
@admin.register(Consolidation)
class Consolidation(admin.ModelAdmin):
    list_display=('operation', 'bordereauOp', 'nature', 'date', 'reglement','datereglement')
    search_fields=('date', )
    
class Agence(admin.ModelAdmin):
    list_display=('NoAgence','nom', 'tel', 'mail', 'localisation')
    search_fields=('NoAgence','nom' )
    
# Register your models here.

