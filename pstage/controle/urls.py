from django.urls import path
from . import views

urlpatterns = [
    path('administrateur', views.administrateur, name='administrateur'),
    path('ccco', views.ccco, name='ccco'),
    path('importer', views.importer, name='importer'),
    path('agent', views.agent, name='agent'),
    path('dpf', views.dpf, name='dpf'),
    path('ajouterAgence', views.ajouterAgence, name='ajouterAgence'),
    path('EditAgence', views.EditAgence, name='EditAgence'),
    path('admindjango', views.admindjango, name='admindjango'),
    path('ajouterAgent', views.ajouterAgent, name='ajouterAgent'),
    path('ajouterAppro', views.ajouterAppro, name='ajouterAppro'),
    path('ajouterCaisse', views.ajouterCaisse, name='ajouterCaisse'),
    path('ajouterClient', views.ajouterClient, name='ajouterClient'),
    path('ajouterCompteOp', views.ajouterCompteOp, name='ajouterCompteOp'),
    path('ajouterDirection', views.ajouterDirection, name='ajouterDirection'),
    path('ajouterFonction', views.ajouterFonction, name='ajouterFonction'),
    path('ajouterNature', views.ajouterNature, name='ajouterNature'),
    path('ajouterOperation', views.ajouterOperation, name='ajouterOperation'),
    path('ajouterOperateur', views.ajouterOperateur, name='ajouterOperateur'),
    path('ajouterService', views.ajouterService, name='ajouterService'),
    path('ajouterTypeOp', views.ajouterTypeOp, name='ajouterTypeOp'),
    path('listeAgence', views.listeAgence, name='listeAgence'),
    path('listeAgent', views.listeAgent, name='listeAgent'),
    path('listeAppro', views.listeAppro, name='listeAppro'),
    path('listeCaisse', views.listeCaisse, name='listeCaisse'),
    path('listeClient', views.listeClient, name='listeClient'),
    path('listeCompteOp', views.listeCompteOp, name='listeCompteOp'),
    path('listeDirection', views.listeDirection, name='listeDirection'),
    path('listeFonction', views.listeFonction, name='listeFonction'),
    path('listeNature', views.listeNature, name='listeNature'),
    path('listeOperation', views.listeOperation, name='listeOperation'),
    path('listeOperateur', views.listeOperateur, name='listeOperateur'),
    path('listeService', views.listeService, name='listeService'),
    path('listeTypeOp', views.listeTypeOp, name='listeTypeOp'),
    path('consolidation', views.consolidation, name='consolidation'),
    path('search_consolidations', views.search_consolidations, name='search_consolidations'),
    # path('detail', views.detail, name='detail'),
    
    
]
   