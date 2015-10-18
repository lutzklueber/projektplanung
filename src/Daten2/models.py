from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone
from django.contrib.auth.models import User



class Tag(models.Model):
    wochentag = models.CharField(max_length = 2)
    wochentaglang = models.CharField(max_length = 10)
    def __str__(self):
        return '%s' % (self.wochentag)    
    class Meta:
        verbose_name_plural = "Tage"
        ordering = ['id']

class Fachrichtung(models.Model):
    Bezeichnung = models.CharField("Abteilung",max_length = 20)
    
    def __str__(self):
        return '%s' % (self.Bezeichnung)
    class Meta:
        verbose_name_plural = "Fachrichtungen"


class Lehrer(models.Model):
    name = models.CharField("Nachname",max_length = 40)
    vorname = models.CharField("Vorname",max_length = 30)
    kurzel = models.CharField("Lehrerkuerzel",max_length = 5)
    fachrichtung = models.ForeignKey(Fachrichtung,verbose_name="Abteilung")
    stundenkontingent = models.IntegerField()
    bemerkung = models.TextField(default = ' ', blank = True)
   
    
    def getDienstagsProjekte(self):
        pr = Projekt.objects.filter(projektbetreuer__betreuer=self,projektbetreuer__tag= Tag.objects.get(wochentag = 'Di'))
        return pr                                  
    
    def getDienstagsRaum(self):
        pr = Projekt.objects.get(projektbetreuer__betreuer=self,projektbetreuer__tag= Tag.objects.get(wochentag = 'Di')).getDienstagsRaeume()
        return pr
    
    def getMittwochsProjekte(self):
        pr = Projekt.objects.filter(projektbetreuer__betreuer=self,projektbetreuer__tag= Tag.objects.get(wochentag = 'Mi'))
        return pr

    def getMittwochsRaum(self):
        pr = Projekt.objects.get(projektbetreuer__betreuer=self,projektbetreuer__tag= Tag.objects.get(wochentag = 'Mi')).getMittwochsRaeume()
        
        return pr
    def getDonnerstagsProjekte(self):
        pr = Projekt.objects.filter(projektbetreuer__betreuer=self,projektbetreuer__tag= Tag.objects.get(wochentag = 'Do'))
                                                                  
        return pr   
    def getDonnerstagsRaum(self):
        pr = Projekt.objects.get(projektbetreuer__betreuer=self,projektbetreuer__tag= Tag.objects.get(wochentag = 'Do')).getDonnerstagsRaeume()
        
        return pr
    def getFreitagsProjekte(self):
        pr = Projekt.objects.filter(projektbetreuer__betreuer=self,projektbetreuer__tag= Tag.objects.get(wochentag = 'Fr'))
                                                                  
        return pr
    def getFreitagsRaum(self):
        pr = Projekt.objects.get(projektbetreuer__betreuer=self,projektbetreuer__tag= Tag.objects.get(wochentag = 'Fr')).getFreitagsRaeume()
        
        return pr
    def getSamstagsProjekte(self):
        pr = Projekt.objects.filter(projektbetreuer__betreuer=self,projektbetreuer__tag= Tag.objects.get(wochentag = 'Sa'))
                                                                  
        return pr
    def getSamstagsRaum(self):
        pr = Projekt.objects.get(projektbetreuer__betreuer=self,projektbetreuer__tag= Tag.objects.get(wochentag = 'Sa')).getSamstagsRaeume()
        return pr
    
    def getStatus(self):
        p = Projektbetreuer.objects.filter(betreuer = self.pk).exclude(tag = Tag.objects.get(wochentag = 'Sa'))
        tage = self.stundenkontingent
        t = str(tage)
        ta = t.replace(',', '.')
        tn = round(round(float(ta)-2)/6)-p.count()
        if tn < 0:
            tn =0
        return str(tn)
    
    def getTage(self):
        tage = self.stundenkontingent
        t = str(tage)
        ta = t.replace(',', '.')
        wert = round(round(float(ta)-2)/6)
        return str(wert)
    
    def __str__(self):
        return '%s' % (self.kurzel)
    
    
    class Meta:
        ordering = ['kurzel','name']
        verbose_name_plural = "Lehrer"   
        
class Raumtyp(models.Model):
    bezeichnung = models.CharField(max_length=15)
    
    def __str__(self):
        return '%s' % (self.bezeichnung)
    class Meta:
        verbose_name_plural = "Raumtypen"
        ordering = ['bezeichnung']   
        
        
class Raum(models.Model):
    bezeichnung = models.CharField("Raum",max_length = 20)
    fachrichtung = models.ForeignKey(Fachrichtung)
    maxschueler = models.IntegerField("Anzahl Schueler")
    bemerkung = models.TextField('Bemerkung',blank = True)
    raumtyp = models.ForeignKey(Raumtyp,blank = True, default = 1)
    
    def getDienstagsProjekt(self):
        p = Projekt.objects.get(projektraeume__raum=self.pk,projektraeume__tag= Tag.objects.get(wochentag = 'Di') )
        return p.klasse
    
    def getMittwochsProjekt(self):
        p = Projekt.objects.get(projektraeume__raum=self.pk,projektraeume__tag= Tag.objects.get(wochentag = 'Mi') )
        return p.klasse

    def getDonnerstagsProjekt(self):
        p = Projekt.objects.get(projektraeume__raum=self.pk,projektraeume__tag= Tag.objects.get(wochentag = 'Do') )
        return p.klasse

    def getFreitagsProjekt(self):
        p = Projekt.objects.get(projektraeume__raum=self.pk,projektraeume__tag= Tag.objects.get(wochentag = 'Fr') )
        return p.klasse

    def getSamstagsProjekt(self):
        p = Projekt.objects.get(projektraeume__raum=self.pk,projektraeume__tag= Tag.objects.get(wochentag = 'Sa') )
        return p.klasse
    
    
    def getDienstagsBetreuer(self):
        p = Projekt.objects.get(projektraeume__raum=self.pk,projektraeume__tag= Tag.objects.get(wochentag = 'Di') )
        p2 = p.projektbetreuer.filter(tag =Tag.objects.get(wochentag = 'Di'))
        return p2
    
    def getMittwochsBetreuer(self):
        p = Projekt.objects.get(projektraeume__raum=self.pk,projektraeume__tag= Tag.objects.get(wochentag = 'Mi') )
        p2 = p.projektbetreuer.filter(tag =Tag.objects.get(wochentag = 'Mi'))
        return p2
    
    def getDonnerstagsBetreuer(self):
        p = Projekt.objects.get(projektraeume__raum=self.pk,projektraeume__tag= Tag.objects.get(wochentag = 'Do') )
        p2 = p.projektbetreuer.filter(tag =Tag.objects.get(wochentag = 'Do'))
        return p2
    
    def getFreitagsBetreuer(self):
        p = Projekt.objects.get(projektraeume__raum=self.pk,projektraeume__tag= Tag.objects.get(wochentag = 'Fr') )
        p2 = p.projektbetreuer.filter(tag =Tag.objects.get(wochentag = 'Fr'))
        return p2
    
    def getSamstagsBetreuer(self):
        p = Projekt.objects.get(projektraeume__raum=self.pk,projektraeume__tag= Tag.objects.get(wochentag = 'Sa') )
        p2 = p.projektbetreuer.filter(tag =Tag.objects.get(wochentag = 'Sa'))
        return p2
    
    
    def __str__(self):
        return '%s' % (self.bezeichnung)

    class Meta:
        verbose_name_plural = "Raeume"
        ordering = ['bezeichnung']        

        

class Klassentyp(models.Model):
    bezeichnung = models.CharField(max_length = 10)
    def __str__(self):
        return '%s' % (self.bezeichnung)    

class Klasse(models.Model):
    bezeichnung = models.CharField(max_length = 20)
    klassenlehrer = models.ForeignKey(Lehrer)
    fachrichtung = models.ForeignKey(Fachrichtung)
    klassenstaerke = models.IntegerField(verbose_name = "Staerke")
    klassentyp = models.ForeignKey(Klassentyp, blank = True)
    bemerkung = models.TextField('Bemerkung',blank = True)
    
    def getProjekt(self):
        w= Projekt.objects.get(klasse = self.pk)
        w2 = w.projektthema
        return w2
    def returnStatus(self):
        w= Projekt.objects.get(klasse = self.pk)
        w2 = w.status
        return w2
         
    def getProjektid(self):
        w= Projekt.objects.get(klasse = self.pk)
        w2 = w.pk
        return w2
    
    def getDienstagsRaeume(self):
        w= Projekt.objects.get(klasse = self.pk)
        w2 = w.projektraeume.filter(tag =Tag.objects.get(wochentag = 'Di'))
    
        return w2
    def getMittwochsRaeume(self):
        w= Projekt.objects.get(klasse = self.pk)
        w2 = w.projektraeume.filter(tag =Tag.objects.get(wochentag = 'Mi'))
    
        return w2
    def getDonnerstagsRaeume(self):
        w= Projekt.objects.get(klasse = self.pk)
        w2 = w.projektraeume.filter(tag =Tag.objects.get(wochentag = 'Do'))
        print(w2)
        return w2
    def getFreitagsRaeume(self):
        w= Projekt.objects.get(klasse = self.pk)
        w2 = w.projektraeume.filter(tag =Tag.objects.get(wochentag = 'Fr'))
    
        return w2
    def getSamstagsRaeume(self):
        w= Projekt.objects.get(klasse = self.pk)
        w2 = w.projektraeume.filter(tag =Tag.objects.get(wochentag = 'Sa'))
    
        return w2
    
    def getDienstagsBetreuer(self):
        w= Projekt.objects.get(klasse = self.pk)
        w2 = w.projektbetreuer.filter(tag =Tag.objects.get(wochentag = 'Di'))
    
        return w2
    
    def getMittwochsBetreuer(self):
        w= Projekt.objects.get(klasse = self.pk)
        w2 = w.projektbetreuer.filter(tag =Tag.objects.get(wochentag = 'Mi'))
    
        return w2
    def getDonnerstagsBetreuer(self):
        w= Projekt.objects.get(klasse = self.pk)
        w2 = w.projektbetreuer.filter(tag =Tag.objects.get(wochentag = 'Do'))
    
        return w2
    def getFreitagsBetreuer(self):
        w= Projekt.objects.get(klasse = self.pk)
        w2 = w.projektbetreuer.filter(tag =Tag.objects.get(wochentag = 'Fr'))
    
        return w2
    def getSamstagsBetreuer(self):
        w= Projekt.objects.get(klasse = self.pk)
        w2 = w.projektbetreuer.filter(tag =Tag.objects.get(wochentag = 'Sa'))
    
        return w2
    def istvollstaendig(self):
        w= Projekt.objects.get(klasse = self.pk)
        wert = 'u'
        if w.klasse.klassentyp != Klassentyp.objects.get(bezeichnung = 'BS'):
            if self.getDienstagsRaeume()and self.getMittwochsRaeume()and self.getDienstagsRaeume()and self.getFreitagsRaeume() and self.getSamstagsRaeume() and self.getDienstagsBetreuer() and self.getMittwochsBetreuer() and self.getDonnerstagsBetreuer() and self.getFreitagsBetreuer()and self.getSamstagsBetreuer():
                wert='w'
        else:
            if (self.getDienstagsBetreuer() and self.getDienstagsRaeume()) or (self.getMittwochsBetreuer()and self.getMittwochsRaeume()) or (self.getDonnerstagsBetreuer() and self.getDonnerstagsRaeume()) or (self.getFreitagsBetreuer() and self.getFreitagsRaeume()):
                wert='w'
        return wert
        
    def __str__(self):
        return '%s' % (self.bezeichnung)
    
    class Meta:
        verbose_name_plural = "Klassen"
        ordering = ['bezeichnung']


class Projektbetreuer(models.Model):
    tag      = models.ForeignKey(Tag)  
    betreuer = models.ForeignKey(Lehrer,related_name ="betreuer")
    
     
    def save(self, *args, **kwargs):
       
        now = timezone.localtime(timezone.now())
        datum = now.strftime("%d-%m-%Y  %H:%M:%S")
      
    
      
        super(Projektbetreuer, self).save(*args, **kwargs)
    
    def getBetreuer(self):
        w= self.betreuer
        return w
    
     
    def __str__(self):
        
        return "%s,%s  " % (self.tag, self.betreuer )
     
    class Meta:
        verbose_name_plural = "Projektbetreuer"
        
class Projektraum(models.Model):
    tag      = models.ForeignKey(Tag)  
    raum     = models.ForeignKey(Raum,related_name ="raum")
    
     
    def save(self, *args, **kwargs):
       
        now = timezone.localtime(timezone.now())
        datum = now.strftime("%d-%m-%Y  %H:%M:%S")
        super(Projektraum, self).save(*args, **kwargs)
        
      
    
      
        

    
    def getRaeume(self):
        w= self.raum
        return w
    
    
     
    def __str__(self):
        
        return "%s" % (self.raum )
     
    class Meta:
        verbose_name_plural = "Projektraeume"
        
        

class Projekt(models.Model):
    projektthema = models.CharField(max_length = 200)
    bemerkung = models.TextField(blank = True)
    agenda = models.TextField(blank = True)
    klasse = models.ForeignKey(Klasse, default = 1)
    mitglieder = models.IntegerField(default = 20)
    besitzer = models.ForeignKey(Lehrer)
    projektbetreuer = models.ManyToManyField(Projektbetreuer)
    projektraeume = models.ManyToManyField(Projektraum)
    status = models.CharField(max_length = 1, 
                              choices =(('w', 'Wunsch'),('a','abgelehnt'),('b','bewilligt'),('u','unvollstaendig'),('r','ruecksprache')),default = 'w')
    
    def save(self, *args, **kwargs):
        
        now = timezone.localtime(timezone.now())
        datum = now.strftime("%d-%m-%Y  %H:%M:%S")
        text = self.agenda
        if self.pk is not None :
            orig = Projekt.objects.get(pk=self.pk)
            if orig.bemerkung != self.bemerkung:
                text = text + datum +  ': Bemerkung geaendert' +'\n'
            if orig.projektthema != self.projektthema:
                text = text + datum +  ' : Thema von '+ orig.projektthema + ' auf ' + self.projektthema + ' geaendert \n'   
            if orig.klasse != self.klasse:
                p = orig.klasse.serializable_value('bezeichnung')
                p2 = smart_text(self.klasse)
                text = text +datum+  ': Klasse von '+ p+' geaendert zu '+ p2+ ' \n'
            if orig.mitglieder != self.mitglieder:
                text = text +datum+  'Klassenstaerke geaendert \n'
            if orig.status != self.status:
                p = orig.get_status_display()
                text = text +datum+  ': Status geaendert von '+ p +' auf '+ self.get_status_display()+' \n'
           
            
            
        else:
            text = text +datum+ ': Projekt neu angelegt '+'\n'  
            
              
        self.agenda = text
        
        super(Projekt, self).save(*args, **kwargs)
    
    def getMontagsBetreuer(self):
        p2 = self.projektbetreuer.filter(tag = Tag.objects.get(wochentag = 'Mo'))
        
        return p2 
    
        
    
    def getMontagsRaeume(self):
        p2 = self.projektraeume.filter(tag = Tag.objects.get(wochentag = 'Mo'))
        
        
        return p2    
    def getDienstagsBetreuer(self):
        p2 = self.projektbetreuer.filter(tag =Tag.objects.get(wochentag = 'Di'))
        
        return p2 
    
    def getDienstagsRaeume(self):
        p2 = self.projektraeume.filter(tag =Tag.objects.get(wochentag = 'Di'))
        
        return p2    
    def getMittwochsBetreuer(self):
        p2 = self.projektbetreuer.filter(tag = Tag.objects.get(wochentag = 'Mi'))
        
        return p2 
    
    def getMittwochsRaeume(self):
        p2 = self.projektraeume.filter(tag = Tag.objects.get(wochentag = 'Mi'))
        
        return p2    
    
    def getDonnerstagsBetreuer(self):
        p2 = self.projektbetreuer.filter(tag = Tag.objects.get(wochentag = 'Do'))
        
        return p2 
    
    def getDonnerstagsRaeume(self):
        p2 = self.projektraeume.filter(tag = Tag.objects.get(wochentag = 'Do'))
        
        return p2    
    
    
    def getFreitagsBetreuer(self):
        p2 = self.projektbetreuer.filter(tag = Tag.objects.get(wochentag = 'Fr'))
        
        return p2 
    
    def getFreitagsRaeume(self):
        p2 = self.projektraeume.filter(tag = Tag.objects.get(wochentag = 'Fr'))
        
        return p2    
    
    def getSamstagsBetreuer(self):
        p2 = self.projektbetreuer.all().filter(tag = Tag.objects.get(wochentag = 'Sa'))
        
        return p2 
    
    def getSamstagsRaeume(self):
        p2 = self.projektraeume.all().filter(tag = Tag.objects.get(wochentag = 'Sa'))
        
        return p2    
    def returnStatus(self):
        return self.status
    
    
    def __str__(self):
        return '%s %s' % (self.klasse, self.projektthema)
   
    class Meta:
        verbose_name_plural = "Projekte"
        ordering = ['klasse']
    
    

