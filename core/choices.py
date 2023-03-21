from django.db import models

class UnidadeFederativa(models.TextChoices):
    # Região Sudeste
    RJ = 'RJ'
    ES = 'ES'
    MG = 'MG'
    SP = 'SP'
    # Região Sul
    RS = 'RS'
    SC = 'SC'
    PR = 'PR'
    # Região Centro-Oeste
    DF = 'DF'
    GO = 'GO'
    MT = 'MT'
    MS = 'MS'
    # Região Norte
    TO = 'TO'
    AM = 'AM'
    PA = 'PA'
    AC = 'AC'
    RR = 'RR'
    RO = 'RO'
    AP = 'AP'
    # Região Nordeste
    MA = 'MA'
    PI = 'PI'
    CE = 'CE'
    RN = 'RN'
    PB = 'PB'
    PE = 'PE'
    AL = 'AL'
    SE = 'SE'
    BA = 'BA'
    
class Sexo(models.TextChoices):
    Macho = 'Macho'
    Fêmea = 'Fêmea'
