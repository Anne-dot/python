#yl1
# Kirjuta programm, mis teisendab kasutaja poolt kroonides sisestatud summa eurodesse 
# ja väljastab ümardatud tulemuse. (round)
krones = int(input('Sisesta summa kroonides, täisarvuna: '))
krones_to_euro = round(krones/15.6466)
print(krones, 'kr on', krones_to_euro, '\N{euro sign}')
