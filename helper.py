import classes
import datetime

mocz = 10
naj_bak =18

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

def grup4_1(ppl):
    """ 
    Najczęściej stosowane leki
    """
    sło = {}
    for p in ppl:
        for t in p.test:
            for b in t.Bacteria:
                if b.idType == naj_bak:
                    for d in b.DrugSusceptibility:
                        try:
                            sło[d.bacteriaId] = sło[d.bacteriaId] + 1
                        except KeyError as e:
                            sło[d.bacteriaId] = 1
    return sło

def grup4_2(ppl, drugId,time_min=datetime.date(1000,1,1), time_max=datetime.date(2200,1,1)):
    """
    still fuk up with bacteria id -> drug id
    """
    liczba = 0

    for p in ppl:
        for t in p.test:
            if  time_min<t.date and time_max >t.date:
                if t.materialId == mocz:
                    l = [bakt.DrugSusceptibility for bakt in [bakteria for bakteria in t.Bacteria] if bakt.idType == naj_bak ]
                    flat_list = [item.bacteriaId for sublist in l for item in sublist]
                    if drugId in flat_list:
                        liczba+=1
    return liczba

def grup4_3(ppl):
    #znaleść parę leków
    sło = {}
    for p in ppl:
        for t in p.test:
            for b in t.Bacteria:
                if b.idType == naj_bak:
                    for d in b.DrugSusceptibility:  
                        sło.setdefault(d.bacteriaId,{})                        
                        for d2 in b.DrugSusceptibility:
                            if d.bacteriaId != d2.bacteriaId:
                                try:
                                    sło[d.bacteriaId][d2.bacteriaId] += 1
                                except KeyError as e:
                                    sło[d.bacteriaId][d2.bacteriaId] = 1
    return sło 

def grup4_4(ppl,time_min=datetime.date(1000,1,1), time_max=datetime.date(2200,1,1)):
    #para leków MOCZ DROBNOUSTUJ 
    lek_naj = 12
    lek_dru = 27
    liczba = 0
    for p in ppl:
        for t in p.test:
            if  time_min<t.date and time_max >t.date:
                if t.materialId == mocz:
                    l = [bakt.DrugSusceptibility for bakt in [bakteria for bakteria in t.Bacteria] if bakt.idType == naj_bak ]
                    flat_list = [item.bacteriaId for sublist in l for item in sublist]
                    if lek_naj in flat_list and lek_dru in flat_list:
                        liczba+=1
    return liczba