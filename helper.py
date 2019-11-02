import classes
import datetime

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
