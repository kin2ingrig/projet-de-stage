from django.db import models

class Agence(models.Model):
    NoAgence= models.CharField(max_length=30, primary_key=True)
    nom =models.CharField(max_length=30, null=False)
    tel=models.IntegerField()
    mail=models.EmailField()
    localisation=models.CharField(max_length=30, null=False)
    
    def __str__(self):
        return self.nom
    
class Fonction(models.Model): 
    code= models.CharField(max_length=30, primary_key=True)
    libelle= models.CharField(max_length=30, null=False)
    
    def __str__(self):
        return self.libelle
    
class Agent(models.Model):
    matricule=models.CharField(max_length=20, primary_key=True, null=False, blank=False)
    nom= models.CharField(max_length=30, blank=False)
    prenom= models.CharField(max_length=30, null=False)
    tel=models.CharField(max_length=50, null=False)
    mail=models.EmailField()
    boitePostale=models.CharField(max_length=50, null=False)
    fonction= models.ForeignKey(Fonction, on_delete=models.CASCADE, null=False)
    
    
    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
class Caisse(models.Model):
    noCaisse= models.CharField(max_length=30, primary_key=True, null=False)
    compte= models.CharField(max_length=30, null=False)
    agence= models.ForeignKey(Agence, on_delete=models.CASCADE)
    agent= models.ForeignKey(Agent, on_delete=models.CASCADE)
     
    
    def __str__(self):
        return f"{self.noCaisse} ({self.compte})"
    
class Operateur(models.Model):
    nom= models.CharField(max_length=30, null=False)
    tel= models.CharField(max_length=10, null=False)
    mail=models.EmailField()
    
    def __str__(self):
        return f"{self.nom}"


class CompteOp(models.Model):
    compteop= models.CharField(max_length=30, null=False)  
    operateur= models.ForeignKey(Operateur, on_delete=models.CASCADE)
    agence= models.ForeignKey(Agence, on_delete=models.CASCADE, default='')
    
    
    def __str__(self):
        return f"{self.compteop}"
    
class Direction(models.Model):
    nom= models.CharField(max_length=30, null=False)
    tel= models.IntegerField(null=False)
    mail= models.EmailField()
    agence= models.ForeignKey(Agence, on_delete=models.CASCADE)    
    agent= models.ForeignKey(Agent, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nom} ({self.tel})"    
    
class Approvisionnement(models.Model):
    montant= models.IntegerField()
    date= models.DateTimeField()
    agence= models.ForeignKey(Agence, on_delete=models.CASCADE)    
    direction= models.ForeignKey(Direction, on_delete=models.CASCADE)
    compteOp= models.ForeignKey(CompteOp, on_delete=models.CASCADE)    
    def __str__(self):
        return f"{self.montant}"  
              
class BordereauOp(models.Model):
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE, null=True)
    operateur = models.ForeignKey(Operateur, on_delete=models.CASCADE,  null=True)
    date= models.DateTimeField()
    idtransfer= models.CharField(max_length=255, primary_key=True, null=False) 
    msisdn= models.IntegerField(default=0)
    number= models.IntegerField(null=True)
    statement= models.CharField(max_length=255)
    amount= models.IntegerField(default=0)
    credit= models.IntegerField(default=0)
    debit = models.IntegerField(default=0) 
    fees = models.IntegerField(default=0)
    previous= models.IntegerField()
    post= models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.idtransfer}" 
          
class Orion(models.Model):
    nomoper= models.CharField(max_length=30, null=False)
    date= models.DateTimeField()
    reference= models.CharField(max_length=30, null=False)
    idtransfer= models.ForeignKey(BordereauOp, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nomoper
    
class Service(models.Model):
    noService= models.CharField(max_length=30, primary_key=True, null=False)
    nom= models.CharField(max_length=30, null=False)
    agence= models.ForeignKey(Agence, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nom}" 
    
        
# class BordereauAgence(models.Model):

class Client(models.Model):
    nom= models.CharField(max_length=30, null=False)
    prenom= models.CharField(max_length=30, null=False)
    refCNIB= models.CharField(max_length=30, null=False)
    tel= models.CharField(max_length=30, null=False)  
    
    def __str__(self):
        return f"{self.nom} {self.prenom}"   
    
class TypeOperation(models.Model):
    nom= models.CharField(max_length=30, null=False)
    
    def __str__(self):
        return f"{self.nom}"             
                    
class Operation(models.Model):
    date = models.DateTimeField()
    montant = models.IntegerField()
    refOp = models.CharField(max_length=30, default='')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    typeOp = models.ForeignKey(TypeOperation, on_delete=models.CASCADE)            
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    operateur = models.ForeignKey(Operateur, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    caisse= models.ForeignKey(Caisse, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.refOp}"

class Nature(models.Model): 
    libelle= models.CharField(max_length=30, null=False)
    
    def __str__(self):
        return f"{self.libelle}"   
                     

class Consolidation(models.Model):
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE,  null=True)
    operateur = models.ForeignKey(Operateur, on_delete=models.CASCADE,  null=True)
    # client = models.ForeignKey(Client, on_delete=models.CASCADE)
    operation= models.ForeignKey(Operation, on_delete=models.CASCADE)
    bordereauOp= models.ForeignKey(BordereauOp, on_delete=models.CASCADE)
    nature= models.ForeignKey(Nature, on_delete=models.CASCADE)
    date= models.DateTimeField()
    reglement= models.BooleanField()
    datereglement= models.DateTimeField()
    ###agence et operateur
    
    def __str__(self):
        return f"{self.nature}"  


