from django.shortcuts import render_to_response
from django.db.models import Sum, Q
from core.models import *
import re

ibge = '280170'
ibge2012 = Popbr.objects.all()
ibge2015 = Poptbr.objects.all()
sia = Pase.objects.all()
sih = Rdse.objects.all()
sim = Dose.objects.all()
sinasc = Dnse.objects.all()
sisprenatal = Pnse.objects.all()


def pop12():
    popse2012 = ibge2012.filter(munic_res=ibge).aggregate(Sum('populacao'))
    populacao2012 = popse2012['populacao__sum']
    return populacao2012


def pop15():
    popse2015 = ibge2015.filter(munic_res=ibge).aggregate(Sum('populacao'))
    populacao2015 = popse2015['populacao__sum']
    return populacao2015


def compsia():
    comp = sia.filter(pa_ufmun=ibge).values_list('pa_mvm').order_by('pa_mvm')
    return comp


def compsih():
    comp = sih.values_list('mes_cmpt', 'ano_cmpt').order_by('mes_cmpt')
    return comp


def compsim():
    comp = sim.values_list('dtcadastro').order_by('numerolote')
    return comp


def compsinasc():
    comp = sinasc.values_list('dtcadastro').order_by('numerolote')
    return comp


def compsisprenatal():
    comp = sisprenatal.values_list('dt_atend').order_by('dt_atend')
    return comp


def indicador01():
    pass


def indicador02():
    pass


def indicador03():
    pass


def indicador04():
    pass


def indicador05():
    numerador = sia.filter(
        Q(pa_munpcn=ibge),
        Q(pa_idade__range=('025', '064')),
        Q(pa_sexo='F'),
        # Procedimentos ambulatoriais selecionados de média complexidade realizados nos ambulatórios
        Q(pa_proc_id='0203010019') | 
        Q(pa_proc_id='0203010086')
    ).aggregate(Sum('pa_qtdpro'))
    denominador = ibge2012.filter(
        Q(munic_res=ibge),
        Q(sexo='2'),
        Q(fxetaria__range=('2529', '6064'))
    ).aggregate(Sum('populacao'))
    resultado = numerador['pa_qtdpro__sum'] / (denominador['populacao__sum'] / 3)
    return resultado


def indicador06():
    numerador = sia.filter(
        Q(pa_munpcn=ibge),
        Q(pa_idade__range=('050', '069')),
        Q(pa_sexo='F'),
        # Procedimentos ambulatoriais selecionados de média complexidade realizados nos ambulatórios
        Q(pa_proc_id='0204030188')
    ).aggregate(Sum('pa_qtdpro'))
    denominador = ibge2012.filter(
        Q(munic_res=ibge),
        Q(sexo='2'),
        Q(fxetaria__range=('5054', '6569'))
    ).aggregate(Sum('populacao'))
    resultado = numerador['pa_qtdpro__sum'] / (denominador['populacao__sum'] / 2)
    return resultado


def indicador07():
    numerador1 = sinasc.filter(
        codmunres=ibge,
        parto='1'
    ).count()
    numerador2 = sinasc.filter(
        codmunres=ibge
    ).count()
    if numerador1 and numerador2 > 0:
        ri7 = (numerador1 / numerador2) * 100
        return ri7


def indicador08():
    pass


def indicador09():
    resultado = sim.filter(
        codmunres=ibge,
        idade__range=('001', '400')
    ).count()
    return resultado


def indicador10():
    numerador = sim.filter(
        codmunres=ibge,
        obitograv='1',
        tppos='S'
    ).count()
    denominador = sim.filter(
        codmunres=ibge,
        obitograv='1'
    ).count()
    if denominador:
        return (numerador / denominador) * 100
    else:
        return 100


def indicador11():
    numerador = sim.filter(
        codmunres=ibge,
        idade__range=('410', '449'),
        sexo='F',
        tppos='S'
    ).count()
    denominador = sim.filter(
        codmunres=ibge,
        idade__range=('410', '449'),
        sexo='F'
    ).count()
    if denominador:
        return (numerador / denominador) * 100
    else:
        return 100


def indicador12():
    pass


def indicador13():
    resultado = sim.filter(
        Q(codmunres=ibge),
        Q(idade__range=('430', '469')),
        Q(causabas__range=('I00', 'I99')) | 
        Q(causabas__range=('C00', 'C97')) | 
        Q(causabas__range=('J30', 'J98')) | 
        Q(causabas__range=('E10', 'E14'))
    ).count()
    return resultado


def indicador14():
    pass


def indicador15():
    pass


def indicador16():
    pass


def indicador17():
    numerador = sim.filter(
        codmunres=ibge,
        tipobito='2'
    ).exclude(
        causabas='R99'
    ).count()
    denominador = sim.filter(
        codmunres=ibge,
        tipobito='2'
    ).count()
    resultado = (numerador / denominador) * 100
    return resultado


def indicador18():
    pass


def indicador19():
    pass


def indicador20():
    pass


def indicador21():
    pass


def indicador22():
    pass


def indicador23():
    pass


def indicador24():
    pass


def indicador25():
    pass

def indicador26():
    numerador1 = sia.filter(
        pa_ufmun=ibge,
        pa_proc_id='0102010072'
    ).exists()
    numerador2 = sia.filter(
        pa_ufmun=ibge,
        pa_proc_id='0102010528'
    ).exists()
    numerador3 = sia.filter(
        pa_ufmun=ibge,
        pa_proc_id='0102010170'
    ).exists()
    numerador4 = sia.filter(
        pa_ufmun=ibge,
        pa_proc_id='0102010226'
    ).exists()
    numerador5 = sia.filter(
        pa_ufmun=ibge,
        pa_proc_id='0102010056'
    ).exists()
    numerador6 = sia.filter(
        pa_ufmun=ibge,
        pa_proc_id='0102010234'
    ).exists()
    numerador7 = sia.filter(
        pa_ufmun=ibge,
        pa_proc_id='0102010242'
    ).exists()
    resultado = ((numerador1 + numerador2 + numerador3 + numerador4 + numerador5 + numerador6 + numerador7) / 7) * 100
    return resultado


def indicador27():
    pass


def indicador28():
    pass


def indicador29():
    pass


def count():
    dic = {
        'compsiafirst': compsia()[0][0][4:] + compsia()[0][0][:4],
        'compsiaend': compsia().reverse()[0][0][4:] + compsia().reverse()[0][0][:4],
        'compsihfirst': compsih()[0][0] + compsih()[0][1],
        'compsihend': compsih().reverse()[0][0] + compsih().reverse()[0][1],
        'compsimfirst': compsim()[0][0][2:],
        'compsimend': compsim().reverse()[0][0][2:],
        'compsinascfirst': compsinasc()[0][0][2:],
        'compsinascend': compsinasc().reverse()[0][0][2:],
        'compsisprenatalfirst': compsisprenatal()[0][0][4:] + compsisprenatal()[0][0][:4],
        'compsisprenatalend': compsisprenatal().reverse()[0][0][4:] + compsisprenatal().reverse()[0][0][:4],
        'populacao2012': pop12(),
        'populacao2015': pop15(),
    }
    for v in range(1, 30):
        r = "ri%s" % v
        i = eval("indicador%.2d()" % v)
        dic[r] = i
    return dic


def metas(request):
    return render_to_response('core/metas.html', count())
