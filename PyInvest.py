import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
#ENTRADAS
capital = float(input('Capital Inicial: '))
aporte  = float(input('Aporte Mensal: '))
meses   = int(input('Prazo (meses): '))
cdi_anual= float(input('CDI anual (%)')) / 100
perc_cdb = float(input('Percentual do CDI (%)')) / 100
perc_lci = float(input('Percentual do LCI (%)')) / 100
taxa_fii = float(input('Rentabilidade mensal do FII (%)'))/100
meta=float(input('Meta financeira (R$) '))
#PROCESSAMENTO
cdi_mesal=math.pow((1+cdi_anual), 1/12) -1
total_investido=capital+(aporte*meses)
#CDB
taxa_cdb=cdi_mesal*perc_cdb
montante_cdb=(capital*math.pow((1+taxa_cdb), meses)+(aporte*meses))
lucro_cdb=montante_cdb-total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

#LCI
taxa_lci = cdi_mesal * perc_lci
montante_lci = (capital * math.pow((1+taxa_lci), meses) + (aporte * meses))

#POUPANÇA 
taxa_poupanca = 0.005
montante_poupanca = (capital*math((1+taxa_poupanca), meses) + (aporte*meses))

#FII - SIMULAÇÕES
