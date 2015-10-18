from django.shortcuts import render, get_object_or_404


from django.http import HttpResponse

from django.views.decorators.csrf import csrf_protect

from django.http import HttpResponseRedirect
from Daten2.models import Projekt, Klasse, Lehrer, Tag, Raum,\
    Projektbetreuer, Projektraum
from django.http.response import Http404


from django.utils import timezone
from django.contrib.auth.views import logout, login


from reportlab.pdfgen import canvas






def ProjektDruckversion(request, nummer):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Projekt.pdf"'
    p = canvas.Canvas(response)
    pr = Projekt.objects.get(pk = nummer)
    zeile = u"\xdcbersichtsplan f\xfcr das Projekt der Klasse " + pr.klasse.bezeichnung
    p.drawString(1, 820, zeile)
    p.line(1, 800, 590, 800)
    l = pr.projektthema
    li = l.splitlines()
    zeile = 780
    for i in range(len(li)):
        if i ==0:
            p.drawString(1, zeile, "Thema")
            
        
            
        for j in range(round(len(li[i])/90)+1):
            ze = li[i][j*90:(j+1)*90]
            if j == 0 and i == 0:
                p.drawString(85, zeile, ": " + ze)
            else:
                p.drawString(85, zeile, "  " + ze)
            zeile =zeile -5
        zeile =zeile -10
        
          
        
    zeile = zeile -20    
    l = pr.bemerkung
    li = l.splitlines()
    for i in range(len(li)):
        if i ==0:
            p.drawString(1, zeile, "Beschreibung")
            
        
            
        for j in range(round(len(li[i])/85)+1):
            ze = li[i][j*85:(j+1)*85]
            if j==0 and i== 0:
                p.drawString(85, zeile, ": " + ze)
            else:
                p.drawString(85, zeile, "  " + ze)
            zeile =zeile -5
        zeile =zeile -10
        
        
        
    zeile = zeile -20    
    p.drawString(1, zeile, "Wochenplan:")
    now = timezone.localtime(timezone.now())
    datum = now.strftime("%d-%m-%Y  %H:%M:%S")
    p.drawString(200, zeile,"Stand: "+datum)
    if pr.status != 'g':
        p.drawString(400, zeile, "(vorl\xe4ufige Version)")
    p.line(1, zeile-5, 590, zeile-5)
    p.line(1, zeile-5, 1, zeile-25)
    p.line(118, zeile-5, 118, zeile-25)
    p.line(236, zeile-5, 236, zeile-25)
    p.line(354, zeile-5, 354, zeile-25)
    p.line(472, zeile-5, 472, zeile-25)
    p.line(590, zeile-5, 590, zeile-25)
    p.line(1, zeile-25, 590, zeile-25)
    p.drawString(5, zeile-20, "Dienstag")
    p.drawString(123, zeile-20, "Mittwoch")
    p.drawString(240, zeile-20, "Donnerstag")
    p.drawString(358, zeile-20, "Freitag")
    p.drawString(476, zeile-20, "Samstag")
    zeile = zeile-25
    
    di = 0
    mi = 0
    do = 0
    fr = 0
    sa = 0
    z = 0
    for i in pr.projektraeume.all():
        if i.tag== Tag.objects.get(wochentag = 'Di'):
            di =di+1
            if di > z:
                z = di
            p.drawString(5, zeile-di*20, i.raum.bezeichnung)
            p.line(1, zeile-((di-1)*20), 1, zeile-(di*20+5))
            p.line(118, zeile-((di-1)*20), 118, zeile-(di*20+5))
            p.line(236, zeile-((di-1)*20), 236, zeile-(di*20+5))
            p.line(354, zeile-((di-1)*20), 354, zeile-(di*20+5))
            p.line(472, zeile-((di-1)*20), 472, zeile-(di*20+5))
            p.line(590, zeile-((di-1)*20), 590, zeile-(di*20+5))
        if i.tag== Tag.objects.get(wochentag = 'Mi'):
            mi =mi+1
            if mi > z:
                z = mi
            
            p.line(1, zeile-((mi-1)*20), 1, zeile-(mi*20+5))
            p.line(118, zeile-((mi-1)*20), 118, zeile-(mi*20+5))
            p.line(236, zeile-((mi-1)*20), 236, zeile-(mi*20+5))
            p.line(354, zeile-((mi-1)*20), 354, zeile-(mi*20+5))
            p.line(472, zeile-((mi-1)*20), 472, zeile-(mi*20+5))
            p.line(590, zeile-((mi-1)*20), 590, zeile-(mi*20+5))
            p.drawString(123, zeile-mi*20, i.raum.bezeichnung)
        if i.tag== Tag.objects.get(wochentag = 'Do'):
            do =do+1
            if do > z:
                z = do
            
            p.line(1, zeile-((do-1)*20), 1, zeile-(do*20+5))
            p.line(118, zeile-((do-1)*20), 118, zeile-(do*20+5))
            p.line(236, zeile-((do-1)*20), 236, zeile-(do*20+5))
            p.line(354, zeile-((do-1)*20), 354, zeile-(do*20+5))
            p.line(472, zeile-((do-1)*20), 472, zeile-(do*20+5))
            p.line(590, zeile-((do-1)*20), 590, zeile-(do*20+5)) 
            p.drawString(240, zeile-do*20, i.raum.bezeichnung)
        if i.tag== Tag.objects.get(wochentag = 'Fr'):
            fr =fr+1
            if fr > z:
                z = fr
            
            p.line(1, zeile-((fr-1)*20), 1, zeile-(fr*20+5))
            p.line(118, zeile-((fr-1)*20), 118, zeile-(fr*20+5))
            p.line(236, zeile-((fr-1)*20), 236, zeile-(fr*20+5))
            p.line(354, zeile-((fr-1)*20), 354, zeile-(fr*20+5))
            p.line(472, zeile-((fr-1)*20), 472, zeile-(fr*20+5))
            p.line(590, zeile-((fr-1)*20), 590, zeile-(fr*20+5))
            p.drawString(358, zeile-fr*20, i.raum.bezeichnung)
        if i.tag== Tag.objects.get(wochentag = 'Sa'):
            sa =sa+1
            if sa > z:
                z = sa
            
            p.line(1, zeile-((sa-1)*20), 1, zeile-(sa*20+5))
            p.line(118, zeile-((sa-1)*20), 118, zeile-(sa*20+5))
            p.line(236, zeile-((sa-1)*20), 236, zeile-(sa*20+5))
            p.line(354, zeile-((sa-1)*20), 354, zeile-(sa*20+5))
            p.line(472, zeile-((sa-1)*20), 472, zeile-(sa*20+5))
            p.line(590, zeile-((sa-1)*20), 590, zeile-(sa*20+5))
            p.drawString(476, zeile-sa*20, i.raum.bezeichnung)
    
    p.line(1,zeile-(z*20+5),590,zeile-(z*20+5))
    zeile = zeile-((z)*20+5)
    di = 0
    mi = 0
    do = 0
    fr = 0
    sa = 0
    z = 0
    
    for i in pr.projektbetreuer.all():
        if i.tag== Tag.objects.get(wochentag = 'Di'):
            di =di+1
            if di > z:
                z = di
            p.drawString(5, zeile-di*20, i.betreuer.kurzel)
            p.line(1, zeile-((di-1)*20), 1, zeile-(di*20+5))
            p.line(118, zeile-((di-1)*20), 118, zeile-(di*20+5))
            p.line(236, zeile-((di-1)*20), 236, zeile-(di*20+5))
            p.line(354, zeile-((di-1)*20), 354, zeile-(di*20+5))
            p.line(472, zeile-((di-1)*20), 472, zeile-(di*20+5))
            p.line(590, zeile-((di-1)*20), 590, zeile-(di*20+5))
        if i.tag== Tag.objects.get(wochentag = 'Mi'):
            mi =mi+1
            if mi > z:
                z = mi
            
            p.line(1, zeile-((mi-1)*20), 1, zeile-(mi*20+5))
            p.line(118, zeile-((mi-1)*20), 118, zeile-(mi*20+5))
            p.line(236, zeile-((mi-1)*20), 236, zeile-(mi*20+5))
            p.line(354, zeile-((mi-1)*20), 354, zeile-(mi*20+5))
            p.line(472, zeile-((mi-1)*20), 472, zeile-(mi*20+5))
            p.line(590, zeile-((mi-1)*20), 590, zeile-(mi*20+5))
            p.drawString(123, zeile-mi*20, i.betreuer.kurzel)
        if i.tag== Tag.objects.get(wochentag = 'Do'):
            do =do+1
            if do > z:
                z = do
            
            p.line(1, zeile-((do-1)*20), 1, zeile-(do*20+5))
            p.line(118, zeile-((do-1)*20), 118, zeile-(do*20+5))
            p.line(236, zeile-((do-1)*20), 236, zeile-(do*20+5))
            p.line(354, zeile-((do-1)*20), 354, zeile-(do*20+5))
            p.line(472, zeile-((do-1)*20), 472, zeile-(do*20+5))
            p.line(590, zeile-((do-1)*20), 590, zeile-(do*20+5)) 
            p.drawString(240, zeile-do*20, i.betreuer.kurzel)
        if i.tag== Tag.objects.get(wochentag = 'Fr'):
            fr =fr+1
            if fr > z:
                z = fr
            p.line(1, zeile-((fr-1)*20), 1, zeile-(fr*20+5))
            p.line(118, zeile-((fr-1)*20), 118, zeile-(fr*20+5))
            p.line(236, zeile-((fr-1)*20), 236, zeile-(fr*20+5))
            p.line(354, zeile-((fr-1)*20), 354, zeile-(fr*20+5))
            p.line(472, zeile-((fr-1)*20), 472, zeile-(fr*20+5))
            p.line(590, zeile-((fr-1)*20), 590, zeile-(fr*20+5))
            p.drawString(358, zeile-fr*20, i.betreuer.kurzel)
        if i.tag== Tag.objects.get(wochentag = 'Sa'):
            sa =sa+1
            if sa > z:
                z = sa
            
            p.line(1, zeile-((sa-1)*20), 1, zeile-(sa*20+5))
            p.line(118, zeile-((sa-1)*20), 118, zeile-(sa*20+5))
            p.line(236, zeile-((sa-1)*20), 236, zeile-(sa*20+5))
            p.line(354, zeile-((sa-1)*20), 354, zeile-(sa*20+5))
            p.line(472, zeile-((sa-1)*20), 472, zeile-(sa*20+5))
            p.line(590, zeile-((sa-1)*20), 590, zeile-(sa*20+5))
            p.drawString(476, zeile-sa*20, i.betreuer.kurzel)
    
    p.line(1,zeile-(z*20+5),590,zeile-(z*20+5))
    zeile = zeile-((z+1)*20+5)
    p.drawString(1, zeile,"Das Projektteam w\xfcnscht allen Beteiligten ein optimales Projekt!!!!!")
    p.showPage()
    p.save()
    return response

@csrf_protect

def start(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/?next=%s' % request.path)
    else:
        p = Projekt.objects.all()
        k1 = Klasse.objects.all()
        return render(request,'Daten2/Hauptseite.html/' ,
                      {
                            'Projektset': p,
                            'Klassen'   :k1,
                       }
                      
                      )
def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/?next=%s' % request.path)
    else:
        p = Projekt.objects.all()
        k1 = Klasse.objects.all()
        print(k1)
        return render(request,'Daten2/show.html/' ,
                      {
                            'Projektset': p,
                            'Klassen'   :k1,
                      }
                      
                      )
def indexleiste(request):
    p = Projekt.objects.all()
    return render(request,'Daten2/Indexleiste.html',
                    {
                          'Projektset': p
                    }
                    
                    )

def show_Hauptseite(request,Projektset ):
   # projektwahl = get_object_or_404(Projekt,pk = Projektname)
    
   
    p2 =  Projekt.objects.all()
    p2.order_by('projekt')
    k1 = Klasse.objects.all()
    
    return render(
                    request,
                    'Daten2/Hauptseite.html',
                    {
                        'Projektset': p2,
                        'Klassen'   : k1,
                    }
                  )
    
def showlehrer(request, sortierung):
   # projektwahl = get_object_or_404(Projekt,pk = Projektname)
    
   
    p2 =  Lehrer.objects.all()
    
    s = sortierung
   
    if sortierung == 'a':
        s= 'n'    
        p3 = Lehrer.objects.all().order_by('vorname').order_by('name').order_by('fachrichtung')
    else:
        s= 'a' 
        p3 = Lehrer.objects.all().order_by('vorname').order_by('name')
    
    return render(
                    request,
                    'Daten2/show_lehrer.html',
                    {
                        'Projektset': p3,
                        'Sortierung': s,
                    }
                  )
def showraum(request):
   # projektwahl = get_object_or_404(Projekt,pk = Projektname)
    
   
    p2 =  Raum.objects.all()
    p2.order_by('bezeichnung')
    
    
    return render(
                    request,
                    'Daten2/show_raum.html',
                    {
                        'Projektset': p2,
                    }
                  )   
    

def neues_Projekt(request,klasseid):
    try:
        p = Projekt.objects.get(klasse = klasseid)
    except Projekt.DoesNotExist:
        Projekt.objects.create(klasse = Klasse.objects.get(pk=klasseid),besitzer = Lehrer.objects.get(kurzel = request.user.username))
        p = Projekt.objects.get(klasse = klasseid)
    text = '/projekt/'+str(p.pk)
    return HttpResponseRedirect(text)
    

def edit_Projekt(request, nummer ):
    try: 
        p = get_object_or_404(Projekt,pk= nummer)
        k = p.klasse
    except Projekt.DoesNotExist:
        raise Http404
    
    if request.method== 'POST':
        test = request.POST
        t = test.get('frd', default=None)
        
        if t:
            
            p.projektraeume.create(tag= Tag.objects.get(wochentag = 'Di'),raum = Raum.objects.get(bezeichnung = t) )
            now = timezone.localtime(timezone.now())
            datum = now.strftime("%d-%m-%Y  %H:%M:%S")
            text = p.agenda+request.user.username +': '
            text = text + datum +  ': Raum '+ t +' am Di hinzugefuegt\n'
            p.agenda = text
            p.save()
            
        t = test.get('rd', default=None)
        
        if t:
            p2 = Projektraum.objects.get(tag= Tag.objects.get(wochentag = 'Di'),raum = Raum.objects.get(bezeichnung = t))
            p2.delete()
            now = timezone.localtime(timezone.now())
            datum = now.strftime("%d-%m-%Y  %H:%M:%S")
            text = p.agenda+request.user.username +': '
            text = text + datum +  ': Raum '+ t +' am  Di geloescht \n'
            p.agenda = text
            p.save()
        
        t = test.get('frm', default=None)
        
        if t:
            
            p.projektraeume.create(tag= Tag.objects.get(wochentag = 'Mi'),raum = Raum.objects.get(bezeichnung = t) )
            now = timezone.localtime(timezone.now())
            datum = now.strftime("%d-%m-%Y  %H:%M:%S")
            text = p.agenda+request.user.username +': '
            text = text + datum +  ': Raum '+ t +' am Mi hinzugefuegt\n'
            p.agenda = text
            p.save()
            
        t = test.get('rm', default=None)
        
        if t:
            p2 = Projektraum.objects.get(tag= Tag.objects.get(wochentag = 'Mi'),raum = Raum.objects.get(bezeichnung = t))
            p2.delete()
            now = timezone.localtime(timezone.now())
            datum = now.strftime("%d-%m-%Y  %H:%M:%S")
            text = p.agenda+request.user.username +': '
            text = text + datum +  ': Raum '+ t +' am  Mi geloescht \n'
            p.agenda = text
            p.save()
            
            
        t = test.get('frdo', default=None)
        
        if t:
            
            p.projektraeume.create(tag= Tag.objects.get(wochentag = 'Do'),raum = Raum.objects.get(bezeichnung = t) )
            now = timezone.localtime(timezone.now())
            datum = now.strftime("%d-%m-%Y  %H:%M:%S")
            text = p.agenda+request.user.username +': '
            text = text + datum +  ': Raum '+ t +' am Do hinzugefuegt\n'
            p.agenda = text
            p.save()
            
        t = test.get('rdo', default=None)
        
        if t:
            p2 = Projektraum.objects.get(tag= Tag.objects.get(wochentag = 'Do'),raum = Raum.objects.get(bezeichnung = t))
            p2.delete()
            now = timezone.localtime(timezone.now())
            datum = now.strftime("%d-%m-%Y  %H:%M:%S")
            text = p.agenda+request.user.username +': '
            text = text + datum +  ': Raum '+ t +' am  Do geloescht \n'
            p.agenda = text
            p.save()    
            
        t = test.get('frf', default=None)
        
        if t:
            
            p.projektraeume.create(tag= Tag.objects.get(wochentag = 'Fr'),raum = Raum.objects.get(bezeichnung = t) )
            now = timezone.localtime(timezone.now())
            datum = now.strftime("%d-%m-%Y  %H:%M:%S")
            text = p.agenda+request.user.username +': '
            text = text + datum +  ': Raum '+ t +' am Fr hinzugefuegt\n'
            p.agenda = text
            p.save()
            
        t = test.get('rf', default=None)
        
        if t:
            p2 = Projektraum.objects.get(tag= Tag.objects.get(wochentag = 'Fr'),raum = Raum.objects.get(bezeichnung = t))
            p2.delete()
            now = timezone.localtime(timezone.now())
            datum = now.strftime("%d-%m-%Y  %H:%M:%S")
            text = p.agenda+request.user.username +': '
            text = text + datum +  ': Raum '+ t +' am  Fr geloescht \n'
            p.agenda = text
            p.save()
            
        t = test.get('frs', default=None)
        
        if t:
            
            p.projektraeume.create(tag= Tag.objects.get(wochentag = 'Sa'),raum = Raum.objects.get(bezeichnung = t) )
            now = timezone.localtime(timezone.now())
            datum = now.strftime("%d-%m-%Y  %H:%M:%S")
            text = p.agenda+request.user.username +': '
            text = text + datum +  ': Raum '+ t +' am Sa hinzugefuegt\n'
            p.agenda = text
            p.save()
            
        t = test.get('rs', default=None)
        
        if t:
            p2 = Projektraum.objects.get(tag= Tag.objects.get(wochentag = 'Sa'),raum = Raum.objects.get(bezeichnung = t))
            p2.delete()
            now = timezone.localtime(timezone.now())
            datum = now.strftime("%d-%m-%Y  %H:%M:%S")
            text = p.agenda+request.user.username +': '
            text = text + datum +  ': Raum '+ t +' am  Sa geloescht \n'
            p.agenda = text
            p.save()
            
        t = test.get('befd', default=None)    
            
        if t:
            
            p.projektbetreuer.create(tag= Tag.objects.get(wochentag = 'Di'),betreuer = Lehrer.objects.get(kurzel = t) )
            now = timezone.localtime(timezone.now())
            datum = now.strftime("%d-%m-%Y  %H:%M:%S")
            text = p.agenda+request.user.username +': '
            text = text + datum +  ': Kollege '+ t +' am Di hinzugefuegt\n'
            p.agenda = text
            p.save()
            
        t = test.get('bed', default=None)
        
        if t:
            p2 = Projektbetreuer.objects.get(tag= Tag.objects.get(wochentag = 'Di'),betreuer = Lehrer.objects.get(kurzel = t))
            p2.delete()
            now = timezone.localtime(timezone.now())
            datum = now.strftime("%d-%m-%Y  %H:%M:%S")
            text = p.agenda+request.user.username +': '
            text = text + datum +  ': Kollege '+ t +' am  Di geloescht \n'
            p.agenda = text
            p.save()
            
        t = test.get('befm', default=None)    
            
        if t:
            
            p.projektbetreuer.create(tag= Tag.objects.get(wochentag = 'Mi'),betreuer = Lehrer.objects.get(kurzel = t) )
            now = timezone.localtime(timezone.now())
            datum = now.strftime("%d-%m-%Y  %H:%M:%S")
            text = p.agenda+request.user.username +': '
            text = text + datum +  ': Kollege '+ t +' am Mi hinzugefuegt\n'
            p.agenda = text
            p.save()
            
        t = test.get('bem', default=None)
        if t:
            
            p2 = Projektbetreuer.objects.get(tag= Tag.objects.get(wochentag = 'Mi'),betreuer = Lehrer.objects.get(kurzel = t))
            p2.delete()
            now = timezone.localtime(timezone.now())
            datum = now.strftime("%d-%m-%Y  %H:%M:%S")
            text = p.agenda+request.user.username +': '
            text = text + datum +  ': Kollege '+ t +' am  Mi geloescht \n'
            p.agenda = text
            p.save()
            
        t = test.get('befdo', default=None)    
            
        if t:
            
            p.projektbetreuer.create(tag= Tag.objects.get(wochentag = 'Do'),betreuer = Lehrer.objects.get(kurzel = t) )
            now = timezone.localtime(timezone.now())
            datum = now.strftime("%d-%m-%Y  %H:%M:%S")
            text = p.agenda+request.user.username +': '
            text = text + datum +  ': Kollege '+ t +' am Do hinzugefuegt\n'
            p.agenda = text
            p.save()
            
        t = test.get('bedo', default=None)
        
        if t:
            p2 = Projektbetreuer.objects.get(tag= Tag.objects.get(wochentag = 'Do'),betreuer = Lehrer.objects.get(kurzel = t))
            p2.delete()
            now = timezone.localtime(timezone.now())
            datum = now.strftime("%d-%m-%Y  %H:%M:%S")
            text = p.agenda+request.user.username +': '
            text = text + datum +  ': Kollege '+ t +' am  Do geloescht \n'
            p.agenda = text
            p.save()    
            
        t = test.get('beff', default=None)    
            
        if t:
            
            p.projektbetreuer.create(tag= Tag.objects.get(wochentag = 'Fr'),betreuer = Lehrer.objects.get(kurzel = t) )
            now = timezone.localtime(timezone.now())
            datum = now.strftime("%d-%m-%Y  %H:%M:%S")
            text = p.agenda+request.user.username +': '
            text = text + datum +  ': Kollege '+ t +' am Fr hinzugefuegt\n'
            p.agenda = text
            p.save()
            
        t = test.get('bef', default=None)
        
        if t:
            p2 = Projektbetreuer.objects.get(tag= Tag.objects.get(wochentag = 'Fr'),betreuer = Lehrer.objects.get(kurzel = t))
            p2.delete()
            now = timezone.localtime(timezone.now())
            datum = now.strftime("%d-%m-%Y  %H:%M:%S")
            text = p.agenda+request.user.username +': '
            text = text + datum +  ': Kollege '+ t +' am  Fr geloescht \n'
            p.agenda = text
            p.save()
            
        t = test.get('befs', default=None)    
            
        if t:
            
            p.projektbetreuer.create(tag= Tag.objects.get(wochentag = 'Sa'),betreuer = Lehrer.objects.get(kurzel = t) )
            now = timezone.localtime(timezone.now())
            datum = now.strftime("%d-%m-%Y  %H:%M:%S")
            text = p.agenda+request.user.username +': '
            text = text + datum +  ': Kollege '+ t +' am Sa hinzugefuegt\n'
            p.agenda = text
            p.save()
            
        t = test.get('bes', default=None)
        
        if t:
            p2 = Projektbetreuer.objects.get(tag= Tag.objects.get(wochentag = 'Sa'),betreuer = Lehrer.objects.get(kurzel = t))
            p2.delete()
            now = timezone.localtime(timezone.now())
            datum = now.strftime("%d-%m-%Y  %H:%M:%S")
            text = p.agenda+request.user.username +': '
            text = text + datum +  ': Kollege '+ t +' am  Sa geloescht \n'
            p.agenda = text
            p.save()

        t = test.get('Thema', default=None)

        if t:
            now = timezone.localtime(timezone.now())
            p.projektthema = t
            p.agenda = p.agenda+request.user.username +': '
            p.save()   
             
        t = test.get('Bemerkung', default=None)    
        if t:
            now = timezone.localtime(timezone.now())
            p.bemerkung = t
            p.agenda = p.agenda+request.user.username +': '
            p.save()   
             
             
        t = test.get('wahl', default=None)    
        if t:
            now = timezone.localtime(timezone.now())
            p.status = t
            p.agenda = p.agenda+request.user.username +': '
            p.save()        
            
            
    fdi = Projektbetreuer.objects.all().filter(tag= Tag.objects.get(wochentag = 'Di')).distinct().values_list('betreuer',flat = True)
    fmi = Projektbetreuer.objects.all().filter(tag= Tag.objects.get(wochentag = 'Mi')).distinct().values_list('betreuer',flat = True)   
    fdo = Projektbetreuer.objects.all().filter(tag= Tag.objects.get(wochentag = 'Do')).distinct().values_list('betreuer',flat = True) 
    ffr = Projektbetreuer.objects.all().filter(tag= Tag.objects.get(wochentag = 'Fr')).distinct().values_list('betreuer',flat = True)     
    fsa = Projektbetreuer.objects.all().filter(tag= Tag.objects.get(wochentag = 'Sa')).distinct().values_list('betreuer',flat = True)   
    freieLehrerdi = Lehrer.objects.all().exclude(pk__in=fdi)
    freieLehrermi = Lehrer.objects.all().exclude(pk__in=fmi)
    freieLehrerdo = Lehrer.objects.all().exclude(pk__in=fdo)
    freieLehrerfr = Lehrer.objects.all().exclude(pk__in=ffr)
    freieLehrersa = Lehrer.objects.all().exclude(pk__in=fsa)
    
    frdi = Projektraum.objects.all().filter(tag= Tag.objects.get(wochentag = 'Di')).values_list('raum',flat = True)
    frmi = Projektraum.objects.all().filter(tag= Tag.objects.get(wochentag = 'Mi')).values_list('raum',flat = True)   
    frdo = Projektraum.objects.all().filter(tag= Tag.objects.get(wochentag = 'Do')).values_list('raum',flat = True) 
    frfr = Projektraum.objects.all().filter(tag= Tag.objects.get(wochentag = 'Fr')).values_list('raum',flat = True)     
    frsa = Projektraum.objects.all().filter(tag= Tag.objects.get(wochentag = 'Sa')).values_list('raum',flat = True)   
    freierRaumdi = Raum.objects.all().exclude(pk__in=frdi).values_list('bezeichnung', flat = True)
    freierRaummi = Raum.objects.all().exclude(pk__in=frmi)
    freierRaumdo = Raum.objects.all().exclude(pk__in=frdo)
    freierRaumfr = Raum.objects.all().exclude(pk__in=frfr)
    freierRaumsa = Raum.objects.all().exclude(pk__in=frsa)
    print(freieLehrerdi)
    p3 = 'Namen'
    
    return render(
                    request,
                    'Daten2/Eingabe_Projekte.html',
                    {
                        'Projektset': p,
                        'Gruppe': k,
                        'freiDi' : freieLehrerdi,
                        'freiMi' : freieLehrermi,
                        'freiDo' : freieLehrerdo,
                        'freiFr' : freieLehrerfr,
                        'freiSa' : freieLehrersa,
                        'freiRDi' :freierRaumdi,
                        'freiRMi' :freierRaummi,
                        'freiRDo' :freierRaumdo,
                        'freiRFr' :freierRaumfr,
                        'freiRSa' :freierRaumsa,
                         
                    }
                  )

def show_Projekt(request, Projektset):
        
    p =  Projektraum.objects.all()
    
    return render(
                    request,
                    'Daten2/show.html',
                    {
                        'Projektset': p
                    }
                  )

                
def logout_view(request):
    logout(request)
    
    return HttpResponseRedirect('/' % request.path)


def login_view(request):
    login(request)
    
    return HttpResponseRedirect('/' % request.path)    