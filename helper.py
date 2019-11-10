import classes
import datetime

mocz = 10

def drugi_akapit(ppl,time_min=datetime.date(1000,1,1), time_max=datetime.date(2200,1,1)):
    """ 
    Biorę:
    listę pacjętów, ramy czasowe
    Zwracam:
    (ile jest badań (długość listy),ile z nich ma conajmniej jedno badanie, ile pacjętów jest z bakterą, )
    """

    lenght = 0
    lenght_z_badaniem = 0
    lenght_z_bakcylem = 0

    for p in ppl:
        if any( t for t in p.test if time_min <= t.date <= time_max):
                lenght += 1

    for p in ppl:
        if p.test:
            if any( t for t in p.test if time_min <= t.date <= time_max):
                lenght_z_badaniem += 1

    for p in ppl:
        if p.test:
            if any( t for t in p.test if time_min <= t.date <= time_max):
                if any([t.Bacteria for t in p.test]):
                    lenght_z_bakcylem += 1
    
    return (lenght,lenght_z_badaniem,lenght_z_bakcylem)

def trzeci_akapit(ppl,time_min=datetime.date(1000,1,1), time_max=datetime.date(2200,1,1)):
    """ 
    Biorę:
    listę pacjętów
    Zwracam:
    (ile jest badań (długość listy),ile jest badań,ilebadań miało lekowrażliwość)
    """

    lenght = 0
    ilosc_badan = 0
    ilosc_badan_z_antybiotykami = 0

    for p in ppl:
        if any( t for t in p.test if time_min <= t.date <= time_max):
                lenght += 1

    for p in ppl:
        for t in p.test:
            if time_min <= t.date <= time_max:
              ilosc_badan += 1
    
    for p in ppl:
        for t in p.test:
            if time_min <= t.date <= time_max:
                if any([b.DrugSusceptibility for b in t.Bacteria if t.Bacteria]):
                    ilosc_badan_z_antybiotykami+=1
    
    return (lenght,ilosc_badan,ilosc_badan_z_antybiotykami)

def grup1(ppl,time_min=datetime.date(1000,1,1), time_max=datetime.date(2200,1,1)):
    """
    Zwracam uwagę na datę
    Oddaję:
    (ile jest badań na moczu, mocz + drobnoustruj, mocz drobnoustruj + lekowrażliwość)
    """

    mocz = 0
    mocz_drob = 0
    mocz_drob_lek = 0
    for p in ppl:
        for t in p.test:
            if  time_min<t.date and time_max >t.date:
                if t.materialId == mocz:
                    mocz+=1
                    if t.Bacteria:
                        mocz_drob+=1
                        for b in t.Bacteria:
                            if b.DrugSusceptibility:
                                mocz_drob_lek+=1

    return (mocz, mocz_drob, mocz_drob_lek)

def grup3(ppl,time_min=datetime.date(1000,1,1), time_max=datetime.date(2200,1,1)):

    sło = {}
    for p in ppl:
        for t in p.test:
            if  time_min<t.date and time_max >t.date:
                if t.materialId == mocz:
                    for b in t.Bacteria:
                        try:
                            sło[b.idType] = sło[b.idType] + 1
                        except KeyError as e:
                            sło[b.idType] = 1
    return sło

def grup3_2(ppl, bakteriaID,time_min=datetime.date(1000,1,1), time_max=datetime.date(2200,1,1)):
    liczba = 0

    for p in ppl:
        for t in p.test:
            if  time_min<t.date and time_max >t.date:
                if t.materialId == mocz:
                    if bakteriaID in [bakteria.idType for bakteria in t.Bacteria]:
                        liczba+=1
    return liczba


