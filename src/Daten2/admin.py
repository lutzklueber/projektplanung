from django.contrib import admin
from Daten2.models import Fachrichtung, Lehrer, Klasse, Raum, Projekt, Tag,Klassentyp, Raumtyp, Projektraum, Projektbetreuer



class LehrerAdmin(admin.ModelAdmin):
    
    edit_display = ('kurzel', 'name', 'vorname', 'fachrichtung', 'stundenkontingent','bemerkung')  


class TagesdatenInline(admin.StackedInline):
    model = Projektbetreuer
    fields = ('tag','raum','betreuer','bemerkung',)
    extra = 5
     
class ProjektAdmin(admin.ModelAdmin):
    
    fields = ('projektthema','bemerkung','mitglieder','projektraeume','projektbetreuer', 'besitzer')  
    
    

class RaumAdmin(admin.ModelAdmin):
    
    fields= ('bezeichnung','fachrichtung', 'maxschueler','bemerkung')  
    

class KlassenAdmin(admin.ModelAdmin):
    
    list_display = ('bezeichnung','klassenlehrer', 'klassenstaerke', 'fachrichtung','bemerkung')  
    

     
admin.site.register(Fachrichtung)
admin.site.register(Lehrer,LehrerAdmin)
admin.site.register(Klasse,KlassenAdmin)
admin.site.register(Raum,RaumAdmin)
admin.site.register(Projekt,ProjektAdmin)
admin.site.register(Tag)
admin.site.register(Projektraum)
admin.site.register(Projektbetreuer)
admin.site.register(Klassentyp)
admin.site.register(Raumtyp)
