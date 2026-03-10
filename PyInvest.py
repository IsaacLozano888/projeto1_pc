import math
import random
import datetime
import statistics as st
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
cdi_mensal=math.pow((1+cdi_anual), 1/12) -1
total_investido=capital+(aporte*meses)
#CDB
taxa_cdb=cdi_mensal*perc_cdb
montante_cdb=(capital*math.pow((1+taxa_cdb), meses)+(aporte*meses))
lucro_cdb=montante_cdb-total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

#LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1+taxa_lci), meses) + (aporte * meses))

#POUPANÇA 
taxa_poupanca = 0.005
montante_poupanca = (capital*math.pow((1+taxa_poupanca), meses) + (aporte*meses))

#FII - SIMULAÇÕES
montante_fii = (capital*math.pow((1 + taxa_fii), meses) + ( aporte * meses))

vari1= random.uniform(-0.03, 0.03)
vari2= random.uniform(-0.03, 0.03)
vari3= random.uniform(-0.03, 0.03)
vari4= random.uniform(-0.03, 0.03)
vari5= random.uniform(-0.03, 0.03)

simu1= montante_fii +(montante_fii * vari1)
simu2= montante_fii +(montante_fii * vari2)
simu3= montante_fii +(montante_fii * vari3)
simu4= montante_fii +(montante_fii * vari4)
simu5= montante_fii +(montante_fii * vari5)

media_fii = st.mean( (simu1,simu2,simu3,simu4,simu5))
mediana_fii = st.median((simu1,simu2,simu3,simu4,simu5))
dp_fii = st.stdev((simu1,simu2,simu3,simu4,simu5))

#FORMATAÇÃO MONETÁRIA
data_simulacao = datetime.date.today()
data_resgate = data_simulacao + datetime.timedelta(days = meses * 30)

# META
meta_atingida = media_fii >= meta

#saidas
print("\n===== RELATÓRIO DE INVESTIMENTO =====\n")

print(f'Data da simulação: {data_simulacao.strftime('%d/%m/%Y')}')
print(f'Data de resgate: {data_resgate.strftime('%d/%m/%Y')} ')
print(f'Valor investido: {locale.currency(total_investido, grouping=True)}')
print(f'CDB: {locale.currency(montante_cdb_liquido, grouping=True)}')
print(f'LCI: {locale.currency(montante_lci, grouping=True)}')
print(f'Poupança: {locale.currency(montante_poupanca, grouping=True)}')
print(f'FII (Média): {locale.currency(media_fii, grouping=True)}')
print(f'Mediana: {locale.currency(mediana_fii, grouping=True)}')
print(f'Desvio padrão: {locale.currency(dp_fii, grouping=True)}')
print(f'Meta atingida? {media_fii >= meta}')