# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Dnse(models.Model):
    numerodn = models.TextField(db_column='NUMERODN', blank=True, null=True)  # Field name made lowercase.
    codinst = models.TextField(db_column='CODINST', blank=True, null=True)  # Field name made lowercase.
    origem = models.TextField(db_column='ORIGEM', blank=True, null=True)  # Field name made lowercase.
    numerodv = models.TextField(db_column='NUMERODV', blank=True, null=True)  # Field name made lowercase.
    prefixodn = models.TextField(db_column='PREFIXODN', blank=True, null=True)  # Field name made lowercase.
    codestab = models.TextField(db_column='CODESTAB', blank=True, null=True)  # Field name made lowercase.
    codmunnasc = models.TextField(db_column='CODMUNNASC', blank=True, null=True)  # Field name made lowercase.
    locnasc = models.TextField(db_column='LOCNASC', blank=True, null=True)  # Field name made lowercase.
    idademae = models.TextField(db_column='IDADEMAE', blank=True, null=True)  # Field name made lowercase.
    estcivmae = models.TextField(db_column='ESTCIVMAE', blank=True, null=True)  # Field name made lowercase.
    escmae = models.TextField(db_column='ESCMAE', blank=True, null=True)  # Field name made lowercase.
    codocupmae = models.TextField(db_column='CODOCUPMAE', blank=True, null=True)  # Field name made lowercase.
    qtdfilvivo = models.TextField(db_column='QTDFILVIVO', blank=True, null=True)  # Field name made lowercase.
    qtdfilmort = models.TextField(db_column='QTDFILMORT', blank=True, null=True)  # Field name made lowercase.
    codmunres = models.TextField(db_column='CODMUNRES', blank=True, null=True)  # Field name made lowercase.
    gestacao = models.TextField(db_column='GESTACAO', blank=True, null=True)  # Field name made lowercase.
    gravidez = models.TextField(db_column='GRAVIDEZ', blank=True, null=True)  # Field name made lowercase.
    parto = models.TextField(db_column='PARTO', blank=True, null=True)  # Field name made lowercase.
    consultas = models.TextField(db_column='CONSULTAS', blank=True, null=True)  # Field name made lowercase.
    dtnasc = models.TextField(db_column='DTNASC', blank=True, null=True)  # Field name made lowercase.
    horanasc = models.TextField(db_column='HORANASC', blank=True, null=True)  # Field name made lowercase.
    sexo = models.TextField(db_column='SEXO', blank=True, null=True)  # Field name made lowercase.
    apgar1 = models.TextField(db_column='APGAR1', blank=True, null=True)  # Field name made lowercase.
    apgar5 = models.TextField(db_column='APGAR5', blank=True, null=True)  # Field name made lowercase.
    racacor = models.TextField(db_column='RACACOR', blank=True, null=True)  # Field name made lowercase.
    peso = models.TextField(db_column='PESO', blank=True, null=True)  # Field name made lowercase.
    idanomal = models.TextField(db_column='IDANOMAL', blank=True, null=True)  # Field name made lowercase.
    dtcadastro = models.TextField(db_column='DTCADASTRO', blank=True, null=True)  # Field name made lowercase.
    codanomal = models.TextField(db_column='CODANOMAL', blank=True, null=True)  # Field name made lowercase.
    numerolote = models.TextField(db_column='NUMEROLOTE', blank=True, null=True)  # Field name made lowercase.
    versaosist = models.TextField(db_column='VERSAOSIST', blank=True, null=True)  # Field name made lowercase.
    dtrecebim = models.TextField(db_column='DTRECEBIM', blank=True, null=True)  # Field name made lowercase.
    difdata = models.TextField(db_column='DIFDATA', blank=True, null=True)  # Field name made lowercase.
    dtrecorig = models.TextField(db_column='DTRECORIG', blank=True, null=True)  # Field name made lowercase.
    naturalmae = models.TextField(db_column='NATURALMAE', blank=True, null=True)  # Field name made lowercase.
    codmunnatu = models.TextField(db_column='CODMUNNATU', blank=True, null=True)  # Field name made lowercase.
    codufnatu = models.TextField(db_column='CODUFNATU', blank=True, null=True)  # Field name made lowercase.
    escmae2010 = models.TextField(db_column='ESCMAE2010', blank=True, null=True)  # Field name made lowercase.
    seriescmae = models.TextField(db_column='SERIESCMAE', blank=True, null=True)  # Field name made lowercase.
    dtnascmae = models.TextField(db_column='DTNASCMAE', blank=True, null=True)  # Field name made lowercase.
    racacormae = models.TextField(db_column='RACACORMAE', blank=True, null=True)  # Field name made lowercase.
    qtdgestant = models.TextField(db_column='QTDGESTANT', blank=True, null=True)  # Field name made lowercase.
    qtdpartnor = models.TextField(db_column='QTDPARTNOR', blank=True, null=True)  # Field name made lowercase.
    qtdpartces = models.TextField(db_column='QTDPARTCES', blank=True, null=True)  # Field name made lowercase.
    idadepai = models.TextField(db_column='IDADEPAI', blank=True, null=True)  # Field name made lowercase.
    dtultmenst = models.TextField(db_column='DTULTMENST', blank=True, null=True)  # Field name made lowercase.
    semagestac = models.TextField(db_column='SEMAGESTAC', blank=True, null=True)  # Field name made lowercase.
    tpmetestim = models.TextField(db_column='TPMETESTIM', blank=True, null=True)  # Field name made lowercase.
    consprenat = models.TextField(db_column='CONSPRENAT', blank=True, null=True)  # Field name made lowercase.
    mesprenat = models.TextField(db_column='MESPRENAT', blank=True, null=True)  # Field name made lowercase.
    tpapresent = models.TextField(db_column='TPAPRESENT', blank=True, null=True)  # Field name made lowercase.
    sttrabpart = models.TextField(db_column='STTRABPART', blank=True, null=True)  # Field name made lowercase.
    stcesparto = models.TextField(db_column='STCESPARTO', blank=True, null=True)  # Field name made lowercase.
    tpnascassi = models.TextField(db_column='TPNASCASSI', blank=True, null=True)  # Field name made lowercase.
    tpfuncresp = models.TextField(db_column='TPFUNCRESP', blank=True, null=True)  # Field name made lowercase.
    tpdocresp = models.TextField(db_column='TPDOCRESP', blank=True, null=True)  # Field name made lowercase.
    dtdeclarac = models.TextField(db_column='DTDECLARAC', blank=True, null=True)  # Field name made lowercase.
    escmaeagr1 = models.TextField(db_column='ESCMAEAGR1', blank=True, null=True)  # Field name made lowercase.
    tprobson = models.TextField(db_column='TPROBSON', blank=True, null=True)  # Field name made lowercase.
    stdnepidem = models.TextField(db_column='STDNEPIDEM', blank=True, null=True)  # Field name made lowercase.
    stdnnova = models.TextField(db_column='STDNNOVA', blank=True, null=True)  # Field name made lowercase.
    codpaisres = models.TextField(db_column='CODPAISRES', blank=True, null=True)  # Field name made lowercase.
    paridade = models.TextField(db_column='PARIDADE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dnse'


class Dose(models.Model):
    numerodo = models.TextField(db_column='NUMERODO', blank=True, null=True)  # Field name made lowercase.
    codinst = models.TextField(db_column='CODINST', blank=True, null=True)  # Field name made lowercase.
    numerodv = models.TextField(db_column='NUMERODV', blank=True, null=True)  # Field name made lowercase.
    origem = models.TextField(db_column='ORIGEM', blank=True, null=True)  # Field name made lowercase.
    tipobito = models.TextField(db_column='TIPOBITO', blank=True, null=True)  # Field name made lowercase.
    dtobito = models.TextField(db_column='DTOBITO', blank=True, null=True)  # Field name made lowercase.
    horaobito = models.TextField(db_column='HORAOBITO', blank=True, null=True)  # Field name made lowercase.
    numsus = models.TextField(db_column='NUMSUS', blank=True, null=True)  # Field name made lowercase.
    natural = models.TextField(db_column='NATURAL', blank=True, null=True)  # Field name made lowercase.
    codmunnatu = models.TextField(db_column='CODMUNNATU', blank=True, null=True)  # Field name made lowercase.
    dtnasc = models.TextField(db_column='DTNASC', blank=True, null=True)  # Field name made lowercase.
    idade = models.TextField(db_column='IDADE', blank=True, null=True)  # Field name made lowercase.
    sexo = models.TextField(db_column='SEXO', blank=True, null=True)  # Field name made lowercase.
    racacor = models.TextField(db_column='RACACOR', blank=True, null=True)  # Field name made lowercase.
    estciv = models.TextField(db_column='ESTCIV', blank=True, null=True)  # Field name made lowercase.
    esc = models.TextField(db_column='ESC', blank=True, null=True)  # Field name made lowercase.
    esc2010 = models.TextField(db_column='ESC2010', blank=True, null=True)  # Field name made lowercase.
    seriescfal = models.TextField(db_column='SERIESCFAL', blank=True, null=True)  # Field name made lowercase.
    ocup = models.TextField(db_column='OCUP', blank=True, null=True)  # Field name made lowercase.
    codmunres = models.TextField(db_column='CODMUNRES', blank=True, null=True)  # Field name made lowercase.
    lococor = models.TextField(db_column='LOCOCOR', blank=True, null=True)  # Field name made lowercase.
    codestab = models.TextField(db_column='CODESTAB', blank=True, null=True)  # Field name made lowercase.
    estabdescr = models.TextField(db_column='ESTABDESCR', blank=True, null=True)  # Field name made lowercase.
    codmunocor = models.TextField(db_column='CODMUNOCOR', blank=True, null=True)  # Field name made lowercase.
    idademae = models.TextField(db_column='IDADEMAE', blank=True, null=True)  # Field name made lowercase.
    escmae = models.TextField(db_column='ESCMAE', blank=True, null=True)  # Field name made lowercase.
    escmae2010 = models.TextField(db_column='ESCMAE2010', blank=True, null=True)  # Field name made lowercase.
    seriescmae = models.TextField(db_column='SERIESCMAE', blank=True, null=True)  # Field name made lowercase.
    ocupmae = models.TextField(db_column='OCUPMAE', blank=True, null=True)  # Field name made lowercase.
    qtdfilvivo = models.TextField(db_column='QTDFILVIVO', blank=True, null=True)  # Field name made lowercase.
    qtdfilmort = models.TextField(db_column='QTDFILMORT', blank=True, null=True)  # Field name made lowercase.
    gravidez = models.TextField(db_column='GRAVIDEZ', blank=True, null=True)  # Field name made lowercase.
    semagestac = models.TextField(db_column='SEMAGESTAC', blank=True, null=True)  # Field name made lowercase.
    gestacao = models.TextField(db_column='GESTACAO', blank=True, null=True)  # Field name made lowercase.
    parto = models.TextField(db_column='PARTO', blank=True, null=True)  # Field name made lowercase.
    obitoparto = models.TextField(db_column='OBITOPARTO', blank=True, null=True)  # Field name made lowercase.
    peso = models.TextField(db_column='PESO', blank=True, null=True)  # Field name made lowercase.
    numerodn = models.TextField(db_column='NUMERODN', blank=True, null=True)  # Field name made lowercase.
    tpmorteoco = models.TextField(db_column='TPMORTEOCO', blank=True, null=True)  # Field name made lowercase.
    obitograv = models.TextField(db_column='OBITOGRAV', blank=True, null=True)  # Field name made lowercase.
    obitopuerp = models.TextField(db_column='OBITOPUERP', blank=True, null=True)  # Field name made lowercase.
    assistmed = models.TextField(db_column='ASSISTMED', blank=True, null=True)  # Field name made lowercase.
    exame = models.TextField(db_column='EXAME', blank=True, null=True)  # Field name made lowercase.
    cirurgia = models.TextField(db_column='CIRURGIA', blank=True, null=True)  # Field name made lowercase.
    necropsia = models.TextField(db_column='NECROPSIA', blank=True, null=True)  # Field name made lowercase.
    linhaa = models.TextField(db_column='LINHAA', blank=True, null=True)  # Field name made lowercase.
    linhab = models.TextField(db_column='LINHAB', blank=True, null=True)  # Field name made lowercase.
    linhac = models.TextField(db_column='LINHAC', blank=True, null=True)  # Field name made lowercase.
    linhad = models.TextField(db_column='LINHAD', blank=True, null=True)  # Field name made lowercase.
    linhaii = models.TextField(db_column='LINHAII', blank=True, null=True)  # Field name made lowercase.
    causabas = models.TextField(db_column='CAUSABAS', blank=True, null=True)  # Field name made lowercase.
    cb_pre = models.TextField(db_column='CB_PRE', blank=True, null=True)  # Field name made lowercase.
    crm = models.TextField(db_column='CRM', blank=True, null=True)  # Field name made lowercase.
    comunsvoim = models.TextField(db_column='COMUNSVOIM', blank=True, null=True)  # Field name made lowercase.
    dtatestado = models.TextField(db_column='DTATESTADO', blank=True, null=True)  # Field name made lowercase.
    circobito = models.TextField(db_column='CIRCOBITO', blank=True, null=True)  # Field name made lowercase.
    acidtrab = models.TextField(db_column='ACIDTRAB', blank=True, null=True)  # Field name made lowercase.
    fonte = models.TextField(db_column='FONTE', blank=True, null=True)  # Field name made lowercase.
    numerolote = models.TextField(db_column='NUMEROLOTE', blank=True, null=True)  # Field name made lowercase.
    tppos = models.TextField(db_column='TPPOS', blank=True, null=True)  # Field name made lowercase.
    dtinvestig = models.TextField(db_column='DTINVESTIG', blank=True, null=True)  # Field name made lowercase.
    causabas_o = models.TextField(db_column='CAUSABAS_O', blank=True, null=True)  # Field name made lowercase.
    dtcadastro = models.TextField(db_column='DTCADASTRO', blank=True, null=True)  # Field name made lowercase.
    atestante = models.TextField(db_column='ATESTANTE', blank=True, null=True)  # Field name made lowercase.
    stcodifica = models.TextField(db_column='STCODIFICA', blank=True, null=True)  # Field name made lowercase.
    codificado = models.TextField(db_column='CODIFICADO', blank=True, null=True)  # Field name made lowercase.
    versaosist = models.TextField(db_column='VERSAOSIST', blank=True, null=True)  # Field name made lowercase.
    versaoscb = models.TextField(db_column='VERSAOSCB', blank=True, null=True)  # Field name made lowercase.
    fonteinv = models.TextField(db_column='FONTEINV', blank=True, null=True)  # Field name made lowercase.
    dtrecebim = models.TextField(db_column='DTRECEBIM', blank=True, null=True)  # Field name made lowercase.
    atestado = models.TextField(db_column='ATESTADO', blank=True, null=True)  # Field name made lowercase.
    dtrecoriga = models.TextField(db_column='DTRECORIGA', blank=True, null=True)  # Field name made lowercase.
    causamat = models.TextField(db_column='CAUSAMAT', blank=True, null=True)  # Field name made lowercase.
    escmaeagr1 = models.TextField(db_column='ESCMAEAGR1', blank=True, null=True)  # Field name made lowercase.
    escfalagr1 = models.TextField(db_column='ESCFALAGR1', blank=True, null=True)  # Field name made lowercase.
    stdoepidem = models.TextField(db_column='STDOEPIDEM', blank=True, null=True)  # Field name made lowercase.
    stdonova = models.TextField(db_column='STDONOVA', blank=True, null=True)  # Field name made lowercase.
    difdata = models.TextField(db_column='DIFDATA', blank=True, null=True)  # Field name made lowercase.
    nudiasobco = models.TextField(db_column='NUDIASOBCO', blank=True, null=True)  # Field name made lowercase.
    nudiasobin = models.TextField(db_column='NUDIASOBIN', blank=True, null=True)  # Field name made lowercase.
    dtcadinv = models.TextField(db_column='DTCADINV', blank=True, null=True)  # Field name made lowercase.
    tpobitocor = models.TextField(db_column='TPOBITOCOR', blank=True, null=True)  # Field name made lowercase.
    dtconinv = models.TextField(db_column='DTCONINV', blank=True, null=True)  # Field name made lowercase.
    fontes = models.TextField(db_column='FONTES', blank=True, null=True)  # Field name made lowercase.
    tpresginfo = models.TextField(db_column='TPRESGINFO', blank=True, null=True)  # Field name made lowercase.
    tpnivelinv = models.TextField(db_column='TPNIVELINV', blank=True, null=True)  # Field name made lowercase.
    nudiasinf = models.TextField(db_column='NUDIASINF', blank=True, null=True)  # Field name made lowercase.
    dtcadinf = models.TextField(db_column='DTCADINF', blank=True, null=True)  # Field name made lowercase.
    morteparto = models.TextField(db_column='MORTEPARTO', blank=True, null=True)  # Field name made lowercase.
    dtconcaso = models.TextField(db_column='DTCONCASO', blank=True, null=True)  # Field name made lowercase.
    fontesinf = models.TextField(db_column='FONTESINF', blank=True, null=True)  # Field name made lowercase.
    altcausa = models.TextField(db_column='ALTCAUSA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dose'


class Pase(models.Model):
    pa_coduni = models.TextField(db_column='PA_CODUNI', blank=True, null=True)  # Field name made lowercase.
    pa_gestao = models.TextField(db_column='PA_GESTAO', blank=True, null=True)  # Field name made lowercase.
    pa_condic = models.TextField(db_column='PA_CONDIC', blank=True, null=True)  # Field name made lowercase.
    pa_ufmun = models.TextField(db_column='PA_UFMUN', blank=True, null=True)  # Field name made lowercase.
    pa_regct = models.TextField(db_column='PA_REGCT', blank=True, null=True)  # Field name made lowercase.
    pa_incout = models.TextField(db_column='PA_INCOUT', blank=True, null=True)  # Field name made lowercase.
    pa_incurg = models.TextField(db_column='PA_INCURG', blank=True, null=True)  # Field name made lowercase.
    pa_tpups = models.TextField(db_column='PA_TPUPS', blank=True, null=True)  # Field name made lowercase.
    pa_tippre = models.TextField(db_column='PA_TIPPRE', blank=True, null=True)  # Field name made lowercase.
    pa_mn_ind = models.TextField(db_column='PA_MN_IND', blank=True, null=True)  # Field name made lowercase.
    pa_cnpjcpf = models.TextField(db_column='PA_CNPJCPF', blank=True, null=True)  # Field name made lowercase.
    pa_cnpjmnt = models.TextField(db_column='PA_CNPJMNT', blank=True, null=True)  # Field name made lowercase.
    pa_cnpj_cc = models.TextField(db_column='PA_CNPJ_CC', blank=True, null=True)  # Field name made lowercase.
    pa_mvm = models.TextField(db_column='PA_MVM', blank=True, null=True)  # Field name made lowercase.
    pa_cmp = models.TextField(db_column='PA_CMP', blank=True, null=True)  # Field name made lowercase.
    pa_proc_id = models.TextField(db_column='PA_PROC_ID', blank=True, null=True)  # Field name made lowercase.
    pa_tpfin = models.TextField(db_column='PA_TPFIN', blank=True, null=True)  # Field name made lowercase.
    pa_subfin = models.TextField(db_column='PA_SUBFIN', blank=True, null=True)  # Field name made lowercase.
    pa_nivcpl = models.TextField(db_column='PA_NIVCPL', blank=True, null=True)  # Field name made lowercase.
    pa_docorig = models.TextField(db_column='PA_DOCORIG', blank=True, null=True)  # Field name made lowercase.
    pa_autoriz = models.TextField(db_column='PA_AUTORIZ', blank=True, null=True)  # Field name made lowercase.
    pa_cnsmed = models.TextField(db_column='PA_CNSMED', blank=True, null=True)  # Field name made lowercase.
    pa_cbocod = models.TextField(db_column='PA_CBOCOD', blank=True, null=True)  # Field name made lowercase.
    pa_motsai = models.TextField(db_column='PA_MOTSAI', blank=True, null=True)  # Field name made lowercase.
    pa_obito = models.TextField(db_column='PA_OBITO', blank=True, null=True)  # Field name made lowercase.
    pa_encerr = models.TextField(db_column='PA_ENCERR', blank=True, null=True)  # Field name made lowercase.
    pa_perman = models.TextField(db_column='PA_PERMAN', blank=True, null=True)  # Field name made lowercase.
    pa_alta = models.TextField(db_column='PA_ALTA', blank=True, null=True)  # Field name made lowercase.
    pa_transf = models.TextField(db_column='PA_TRANSF', blank=True, null=True)  # Field name made lowercase.
    pa_cidpri = models.TextField(db_column='PA_CIDPRI', blank=True, null=True)  # Field name made lowercase.
    pa_cidsec = models.TextField(db_column='PA_CIDSEC', blank=True, null=True)  # Field name made lowercase.
    pa_cidcas = models.TextField(db_column='PA_CIDCAS', blank=True, null=True)  # Field name made lowercase.
    pa_catend = models.TextField(db_column='PA_CATEND', blank=True, null=True)  # Field name made lowercase.
    pa_idade = models.TextField(db_column='PA_IDADE', blank=True, null=True)  # Field name made lowercase.
    idademin = models.TextField(db_column='IDADEMIN', blank=True, null=True)  # Field name made lowercase.
    idademax = models.TextField(db_column='IDADEMAX', blank=True, null=True)  # Field name made lowercase.
    pa_flidade = models.TextField(db_column='PA_FLIDADE', blank=True, null=True)  # Field name made lowercase.
    pa_sexo = models.TextField(db_column='PA_SEXO', blank=True, null=True)  # Field name made lowercase.
    pa_racacor = models.TextField(db_column='PA_RACACOR', blank=True, null=True)  # Field name made lowercase.
    pa_munpcn = models.TextField(db_column='PA_MUNPCN', blank=True, null=True)  # Field name made lowercase.
    pa_qtdpro = models.BigIntegerField(db_column='PA_QTDPRO', blank=True, null=True)  # Field name made lowercase.
    pa_qtdapr = models.BigIntegerField(db_column='PA_QTDAPR', blank=True, null=True)  # Field name made lowercase.
    pa_valpro = models.FloatField(db_column='PA_VALPRO', blank=True, null=True)  # Field name made lowercase.
    pa_valapr = models.FloatField(db_column='PA_VALAPR', blank=True, null=True)  # Field name made lowercase.
    pa_ufdif = models.TextField(db_column='PA_UFDIF', blank=True, null=True)  # Field name made lowercase.
    pa_mndif = models.TextField(db_column='PA_MNDIF', blank=True, null=True)  # Field name made lowercase.
    pa_dif_val = models.FloatField(db_column='PA_DIF_VAL', blank=True, null=True)  # Field name made lowercase.
    nu_vpa_tot = models.FloatField(db_column='NU_VPA_TOT', blank=True, null=True)  # Field name made lowercase.
    nu_pa_tot = models.FloatField(db_column='NU_PA_TOT', blank=True, null=True)  # Field name made lowercase.
    pa_indica = models.TextField(db_column='PA_INDICA', blank=True, null=True)  # Field name made lowercase.
    pa_codoco = models.TextField(db_column='PA_CODOCO', blank=True, null=True)  # Field name made lowercase.
    pa_flqt = models.TextField(db_column='PA_FLQT', blank=True, null=True)  # Field name made lowercase.
    pa_fler = models.TextField(db_column='PA_FLER', blank=True, null=True)  # Field name made lowercase.
    pa_etnia = models.TextField(db_column='PA_ETNIA', blank=True, null=True)  # Field name made lowercase.
    pa_vl_cf = models.FloatField(db_column='PA_VL_CF', blank=True, null=True)  # Field name made lowercase.
    pa_vl_cl = models.FloatField(db_column='PA_VL_CL', blank=True, null=True)  # Field name made lowercase.
    pa_vl_inc = models.FloatField(db_column='PA_VL_INC', blank=True, null=True)  # Field name made lowercase.
    pa_srv_c = models.TextField(db_column='PA_SRV_C', blank=True, null=True)  # Field name made lowercase.
    pa_ine = models.TextField(db_column='PA_INE', blank=True, null=True)  # Field name made lowercase.
    pa_nat_jur = models.TextField(db_column='PA_NAT_JUR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pase'


class Pnse(models.Model):
    nu_ano_ges = models.TextField(db_column='NU_ANO_GES', blank=True, null=True)  # Field name made lowercase.
    dt_atend = models.TextField(db_column='DT_ATEND', blank=True, null=True)  # Field name made lowercase.
    co_uf_ibge = models.TextField(db_column='CO_UF_IBGE', blank=True, null=True)  # Field name made lowercase.
    nu_gesta = models.TextField(db_column='NU_GESTA', blank=True, null=True)  # Field name made lowercase.
    co_gestant = models.TextField(db_column='CO_GESTANT', blank=True, null=True)  # Field name made lowercase.
    co_pais = models.TextField(db_column='CO_PAIS', blank=True, null=True)  # Field name made lowercase.
    nu_cns = models.TextField(db_column='NU_CNS', blank=True, null=True)  # Field name made lowercase.
    nu_idade = models.TextField(db_column='NU_IDADE', blank=True, null=True)  # Field name made lowercase.
    nu_nis = models.TextField(db_column='NU_NIS', blank=True, null=True)  # Field name made lowercase.
    nu_nis_rep = models.TextField(db_column='NU_NIS_REP', blank=True, null=True)  # Field name made lowercase.
    ds_zona = models.TextField(db_column='DS_ZONA', blank=True, null=True)  # Field name made lowercase.
    qt_ab_ect = models.TextField(db_column='QT_AB_ECT', blank=True, null=True)  # Field name made lowercase.
    qt_ab_ger = models.TextField(db_column='QT_AB_GER', blank=True, null=True)  # Field name made lowercase.
    qt_ab_mol = models.TextField(db_column='QT_AB_MOL', blank=True, null=True)  # Field name made lowercase.
    qt_mor_aps = models.TextField(db_column='QT_MOR_APS', blank=True, null=True)  # Field name made lowercase.
    qt_mor_ps = models.TextField(db_column='QT_MOR_PS', blank=True, null=True)  # Field name made lowercase.
    qt_nsc_mor = models.TextField(db_column='QT_NSC_MOR', blank=True, null=True)  # Field name made lowercase.
    qt_nsc_viv = models.TextField(db_column='QT_NSC_VIV', blank=True, null=True)  # Field name made lowercase.
    qt_prt_cir = models.TextField(db_column='QT_PRT_CIR', blank=True, null=True)  # Field name made lowercase.
    qt_prt_for = models.TextField(db_column='QT_PRT_FOR', blank=True, null=True)  # Field name made lowercase.
    qt_prt_vag = models.TextField(db_column='QT_PRT_VAG', blank=True, null=True)  # Field name made lowercase.
    st_aux_dsl = models.TextField(db_column='ST_AUX_DSL', blank=True, null=True)  # Field name made lowercase.
    st_gra_ant = models.TextField(db_column='ST_GRA_ANT', blank=True, null=True)  # Field name made lowercase.
    st_gra_pla = models.TextField(db_column='ST_GRA_PLA', blank=True, null=True)  # Field name made lowercase.
    dt_dum = models.TextField(db_column='DT_DUM', blank=True, null=True)  # Field name made lowercase.
    dt_dpp = models.TextField(db_column='DT_DPP', blank=True, null=True)  # Field name made lowercase.
    co_tpo_gra = models.TextField(db_column='CO_TPO_GRA', blank=True, null=True)  # Field name made lowercase.
    co_esc_gp = models.TextField(db_column='CO_ESC_GP', blank=True, null=True)  # Field name made lowercase.
    co_rac_gp = models.TextField(db_column='CO_RAC_GP', blank=True, null=True)  # Field name made lowercase.
    co_etn_gp = models.TextField(db_column='CO_ETN_GP', blank=True, null=True)  # Field name made lowercase.
    co_stf_gp = models.TextField(db_column='CO_STF_GP', blank=True, null=True)  # Field name made lowercase.
    co_mun_ubs = models.TextField(db_column='CO_MUN_UBS', blank=True, null=True)  # Field name made lowercase.
    qt_cons = models.BigIntegerField(db_column='QT_CONS', blank=True, null=True)  # Field name made lowercase.
    qt_consult = models.TextField(db_column='QT_CONSULT', blank=True, null=True)  # Field name made lowercase.
    st_gestac = models.TextField(db_column='ST_GESTAC', blank=True, null=True)  # Field name made lowercase.
    dt_inc = models.TextField(db_column='DT_INC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pnse'


class Popbr(models.Model):
    munic_res = models.TextField(db_column='MUNIC_RES', blank=True, null=True)  # Field name made lowercase.
    ano = models.TextField(db_column='ANO', blank=True, null=True)  # Field name made lowercase.
    sexo = models.TextField(db_column='SEXO', blank=True, null=True)  # Field name made lowercase.
    situacao = models.TextField(db_column='SITUACAO', blank=True, null=True)  # Field name made lowercase.
    fxetaria = models.TextField(db_column='FXETARIA', blank=True, null=True)  # Field name made lowercase.
    populacao = models.BigIntegerField(db_column='POPULACAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'popbr'


class Poptbr(models.Model):
    munic_res = models.TextField(db_column='MUNIC_RES', blank=True, null=True)  # Field name made lowercase.
    ano = models.TextField(db_column='ANO', blank=True, null=True)  # Field name made lowercase.
    populacao = models.BigIntegerField(db_column='POPULACAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'poptbr'


class Rdse(models.Model):
    uf_zi = models.TextField(db_column='UF_ZI', blank=True, null=True)  # Field name made lowercase.
    ano_cmpt = models.TextField(db_column='ANO_CMPT', blank=True, null=True)  # Field name made lowercase.
    mes_cmpt = models.TextField(db_column='MES_CMPT', blank=True, null=True)  # Field name made lowercase.
    espec = models.TextField(db_column='ESPEC', blank=True, null=True)  # Field name made lowercase.
    cgc_hosp = models.TextField(db_column='CGC_HOSP', blank=True, null=True)  # Field name made lowercase.
    n_aih = models.TextField(db_column='N_AIH', blank=True, null=True)  # Field name made lowercase.
    ident = models.TextField(db_column='IDENT', blank=True, null=True)  # Field name made lowercase.
    cep = models.TextField(db_column='CEP', blank=True, null=True)  # Field name made lowercase.
    munic_res = models.TextField(db_column='MUNIC_RES', blank=True, null=True)  # Field name made lowercase.
    nasc = models.TextField(db_column='NASC', blank=True, null=True)  # Field name made lowercase.
    sexo = models.TextField(db_column='SEXO', blank=True, null=True)  # Field name made lowercase.
    uti_mes_in = models.BigIntegerField(db_column='UTI_MES_IN', blank=True, null=True)  # Field name made lowercase.
    uti_mes_an = models.BigIntegerField(db_column='UTI_MES_AN', blank=True, null=True)  # Field name made lowercase.
    uti_mes_al = models.BigIntegerField(db_column='UTI_MES_AL', blank=True, null=True)  # Field name made lowercase.
    uti_mes_to = models.BigIntegerField(db_column='UTI_MES_TO', blank=True, null=True)  # Field name made lowercase.
    marca_uti = models.TextField(db_column='MARCA_UTI', blank=True, null=True)  # Field name made lowercase.
    uti_int_in = models.BigIntegerField(db_column='UTI_INT_IN', blank=True, null=True)  # Field name made lowercase.
    uti_int_an = models.BigIntegerField(db_column='UTI_INT_AN', blank=True, null=True)  # Field name made lowercase.
    uti_int_al = models.BigIntegerField(db_column='UTI_INT_AL', blank=True, null=True)  # Field name made lowercase.
    uti_int_to = models.BigIntegerField(db_column='UTI_INT_TO', blank=True, null=True)  # Field name made lowercase.
    diar_acom = models.BigIntegerField(db_column='DIAR_ACOM', blank=True, null=True)  # Field name made lowercase.
    qt_diarias = models.BigIntegerField(db_column='QT_DIARIAS', blank=True, null=True)  # Field name made lowercase.
    proc_solic = models.TextField(db_column='PROC_SOLIC', blank=True, null=True)  # Field name made lowercase.
    proc_rea = models.TextField(db_column='PROC_REA', blank=True, null=True)  # Field name made lowercase.
    val_sh = models.FloatField(db_column='VAL_SH', blank=True, null=True)  # Field name made lowercase.
    val_sp = models.FloatField(db_column='VAL_SP', blank=True, null=True)  # Field name made lowercase.
    val_sadt = models.FloatField(db_column='VAL_SADT', blank=True, null=True)  # Field name made lowercase.
    val_rn = models.FloatField(db_column='VAL_RN', blank=True, null=True)  # Field name made lowercase.
    val_acomp = models.FloatField(db_column='VAL_ACOMP', blank=True, null=True)  # Field name made lowercase.
    val_ortp = models.FloatField(db_column='VAL_ORTP', blank=True, null=True)  # Field name made lowercase.
    val_sangue = models.FloatField(db_column='VAL_SANGUE', blank=True, null=True)  # Field name made lowercase.
    val_sadtsr = models.FloatField(db_column='VAL_SADTSR', blank=True, null=True)  # Field name made lowercase.
    val_transp = models.FloatField(db_column='VAL_TRANSP', blank=True, null=True)  # Field name made lowercase.
    val_obsang = models.FloatField(db_column='VAL_OBSANG', blank=True, null=True)  # Field name made lowercase.
    val_ped1ac = models.FloatField(db_column='VAL_PED1AC', blank=True, null=True)  # Field name made lowercase.
    val_tot = models.FloatField(db_column='VAL_TOT', blank=True, null=True)  # Field name made lowercase.
    val_uti = models.FloatField(db_column='VAL_UTI', blank=True, null=True)  # Field name made lowercase.
    us_tot = models.FloatField(db_column='US_TOT', blank=True, null=True)  # Field name made lowercase.
    dt_inter = models.TextField(db_column='DT_INTER', blank=True, null=True)  # Field name made lowercase.
    dt_saida = models.TextField(db_column='DT_SAIDA', blank=True, null=True)  # Field name made lowercase.
    diag_princ = models.TextField(db_column='DIAG_PRINC', blank=True, null=True)  # Field name made lowercase.
    diag_secun = models.TextField(db_column='DIAG_SECUN', blank=True, null=True)  # Field name made lowercase.
    cobranca = models.TextField(db_column='COBRANCA', blank=True, null=True)  # Field name made lowercase.
    natureza = models.TextField(db_column='NATUREZA', blank=True, null=True)  # Field name made lowercase.
    nat_jur = models.TextField(db_column='NAT_JUR', blank=True, null=True)  # Field name made lowercase.
    gestao = models.TextField(db_column='GESTAO', blank=True, null=True)  # Field name made lowercase.
    rubrica = models.BigIntegerField(db_column='RUBRICA', blank=True, null=True)  # Field name made lowercase.
    ind_vdrl = models.TextField(db_column='IND_VDRL', blank=True, null=True)  # Field name made lowercase.
    munic_mov = models.TextField(db_column='MUNIC_MOV', blank=True, null=True)  # Field name made lowercase.
    cod_idade = models.TextField(db_column='COD_IDADE', blank=True, null=True)  # Field name made lowercase.
    idade = models.BigIntegerField(db_column='IDADE', blank=True, null=True)  # Field name made lowercase.
    dias_perm = models.BigIntegerField(db_column='DIAS_PERM', blank=True, null=True)  # Field name made lowercase.
    morte = models.BigIntegerField(db_column='MORTE', blank=True, null=True)  # Field name made lowercase.
    nacional = models.TextField(db_column='NACIONAL', blank=True, null=True)  # Field name made lowercase.
    num_proc = models.TextField(db_column='NUM_PROC', blank=True, null=True)  # Field name made lowercase.
    car_int = models.TextField(db_column='CAR_INT', blank=True, null=True)  # Field name made lowercase.
    tot_pt_sp = models.BigIntegerField(db_column='TOT_PT_SP', blank=True, null=True)  # Field name made lowercase.
    cpf_aut = models.TextField(db_column='CPF_AUT', blank=True, null=True)  # Field name made lowercase.
    homonimo = models.TextField(db_column='HOMONIMO', blank=True, null=True)  # Field name made lowercase.
    num_filhos = models.BigIntegerField(db_column='NUM_FILHOS', blank=True, null=True)  # Field name made lowercase.
    instru = models.TextField(db_column='INSTRU', blank=True, null=True)  # Field name made lowercase.
    cid_notif = models.TextField(db_column='CID_NOTIF', blank=True, null=True)  # Field name made lowercase.
    contracep1 = models.TextField(db_column='CONTRACEP1', blank=True, null=True)  # Field name made lowercase.
    contracep2 = models.TextField(db_column='CONTRACEP2', blank=True, null=True)  # Field name made lowercase.
    gestrisco = models.TextField(db_column='GESTRISCO', blank=True, null=True)  # Field name made lowercase.
    insc_pn = models.TextField(db_column='INSC_PN', blank=True, null=True)  # Field name made lowercase.
    seq_aih5 = models.TextField(db_column='SEQ_AIH5', blank=True, null=True)  # Field name made lowercase.
    cbor = models.TextField(db_column='CBOR', blank=True, null=True)  # Field name made lowercase.
    cnaer = models.TextField(db_column='CNAER', blank=True, null=True)  # Field name made lowercase.
    vincprev = models.TextField(db_column='VINCPREV', blank=True, null=True)  # Field name made lowercase.
    gestor_cod = models.TextField(db_column='GESTOR_COD', blank=True, null=True)  # Field name made lowercase.
    gestor_tp = models.TextField(db_column='GESTOR_TP', blank=True, null=True)  # Field name made lowercase.
    gestor_cpf = models.TextField(db_column='GESTOR_CPF', blank=True, null=True)  # Field name made lowercase.
    gestor_dt = models.TextField(db_column='GESTOR_DT', blank=True, null=True)  # Field name made lowercase.
    cnes = models.TextField(db_column='CNES', blank=True, null=True)  # Field name made lowercase.
    cnpj_mant = models.TextField(db_column='CNPJ_MANT', blank=True, null=True)  # Field name made lowercase.
    infehosp = models.TextField(db_column='INFEHOSP', blank=True, null=True)  # Field name made lowercase.
    cid_asso = models.TextField(db_column='CID_ASSO', blank=True, null=True)  # Field name made lowercase.
    cid_morte = models.TextField(db_column='CID_MORTE', blank=True, null=True)  # Field name made lowercase.
    complex = models.TextField(db_column='COMPLEX', blank=True, null=True)  # Field name made lowercase.
    financ = models.TextField(db_column='FINANC', blank=True, null=True)  # Field name made lowercase.
    faec_tp = models.TextField(db_column='FAEC_TP', blank=True, null=True)  # Field name made lowercase.
    regct = models.TextField(db_column='REGCT', blank=True, null=True)  # Field name made lowercase.
    raca_cor = models.TextField(db_column='RACA_COR', blank=True, null=True)  # Field name made lowercase.
    etnia = models.TextField(db_column='ETNIA', blank=True, null=True)  # Field name made lowercase.
    sequencia = models.BigIntegerField(db_column='SEQUENCIA', blank=True, null=True)  # Field name made lowercase.
    remessa = models.TextField(db_column='REMESSA', blank=True, null=True)  # Field name made lowercase.
    aud_just = models.TextField(db_column='AUD_JUST', blank=True, null=True)  # Field name made lowercase.
    sis_just = models.TextField(db_column='SIS_JUST', blank=True, null=True)  # Field name made lowercase.
    val_sh_fed = models.FloatField(db_column='VAL_SH_FED', blank=True, null=True)  # Field name made lowercase.
    val_sp_fed = models.FloatField(db_column='VAL_SP_FED', blank=True, null=True)  # Field name made lowercase.
    val_sh_ges = models.FloatField(db_column='VAL_SH_GES', blank=True, null=True)  # Field name made lowercase.
    val_sp_ges = models.FloatField(db_column='VAL_SP_GES', blank=True, null=True)  # Field name made lowercase.
    val_uci = models.FloatField(db_column='VAL_UCI', blank=True, null=True)  # Field name made lowercase.
    marca_uci = models.TextField(db_column='MARCA_UCI', blank=True, null=True)  # Field name made lowercase.
    diagsec1 = models.TextField(db_column='DIAGSEC1', blank=True, null=True)  # Field name made lowercase.
    diagsec2 = models.TextField(db_column='DIAGSEC2', blank=True, null=True)  # Field name made lowercase.
    diagsec3 = models.TextField(db_column='DIAGSEC3', blank=True, null=True)  # Field name made lowercase.
    diagsec4 = models.TextField(db_column='DIAGSEC4', blank=True, null=True)  # Field name made lowercase.
    diagsec5 = models.TextField(db_column='DIAGSEC5', blank=True, null=True)  # Field name made lowercase.
    diagsec6 = models.TextField(db_column='DIAGSEC6', blank=True, null=True)  # Field name made lowercase.
    diagsec7 = models.TextField(db_column='DIAGSEC7', blank=True, null=True)  # Field name made lowercase.
    diagsec8 = models.TextField(db_column='DIAGSEC8', blank=True, null=True)  # Field name made lowercase.
    diagsec9 = models.TextField(db_column='DIAGSEC9', blank=True, null=True)  # Field name made lowercase.
    tpdisec1 = models.TextField(db_column='TPDISEC1', blank=True, null=True)  # Field name made lowercase.
    tpdisec2 = models.TextField(db_column='TPDISEC2', blank=True, null=True)  # Field name made lowercase.
    tpdisec3 = models.TextField(db_column='TPDISEC3', blank=True, null=True)  # Field name made lowercase.
    tpdisec4 = models.TextField(db_column='TPDISEC4', blank=True, null=True)  # Field name made lowercase.
    tpdisec5 = models.TextField(db_column='TPDISEC5', blank=True, null=True)  # Field name made lowercase.
    tpdisec6 = models.TextField(db_column='TPDISEC6', blank=True, null=True)  # Field name made lowercase.
    tpdisec7 = models.TextField(db_column='TPDISEC7', blank=True, null=True)  # Field name made lowercase.
    tpdisec8 = models.TextField(db_column='TPDISEC8', blank=True, null=True)  # Field name made lowercase.
    tpdisec9 = models.TextField(db_column='TPDISEC9', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rdse'
