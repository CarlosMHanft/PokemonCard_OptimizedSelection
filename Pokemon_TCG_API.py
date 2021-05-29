#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# !pip install requests
# !pip install pulp


# In[ ]:


import pandas as pd
import numpy as np
import requests as req
import re as regex
from time import sleep


# In[ ]:


# Fonte : https://docs.pokemontcg.io/#documentationrate_limits

###################################################################################################
# Code 	Name 	                Description
###################################################################################################
# 400 	Bad Request 	        We could not process that action
# 403 	Forbidden 	            You exceeded the rate limit
# 404 	Not Found 	            The requested resource could not be found
# 500 	Internal Server Error 	We had a problem with our server. Please try again later
# 503 	Service Unavailable 	We are temporarily offline for maintenance. Please try again later
###################################################################################################

dict_error_code = {
    200: 'Success !',
    400: 'Bad Request.',
    403: 'Forbidden !',
    404: 'Not Found.',
    500: 'Internal Server Error !',
    503: 'Service Unavailable !'
}


# In[ ]:


# Definindo a URL da API e os parâmetros/condições a serem incluídas nela
url = "https://api.pokemontcg.io/v2/sets"

# Chamando a API do Pokemon TCG
response = req.get(url)

# Retornar o resultado do request
print(f' Resultado : ' + dict_error_code[response.status_code])

# dados de cada set de cartas
sets = response.json()['data']

# Lista com os IDs de cada set
set_names = [sets[i]['id'] for i in np.arange(len(sets))]


# In[ ]:


# Aplicando um loop pra retornar dados de pokémons de cada set

data = []

for s in set_names:

    url = "https://api.pokemontcg.io/v2/cards"
    params = 'q=supertype:pokemon set.id:' + s

    # Chamando a API do Pokemon TCG
    response = req.get(url,params=params)

    # Convertendo o request em arquivo JSON e contando quantos registros este retornou
    response_json = response.json()
    dataset = response_json['data']
    data.extend(dataset)

    # Retornar o resultado do request
    print(f' Set {s} ( {len(response_json["data"])} linhas ): {dict_error_code[response.status_code]}')
    sleep(0.2)


# In[ ]:


print(f'O tipo da request da API: {type(response_json)}')
print(f'O tipo do elemento dentro da API ("data"): {type(data)}')
print(f'O tipo de um elemento da lista em data: {type(data[0])}')


# In[ ]:


# O primeiro pokémon do primeiro conjunto de cartas de Pokémon (Base Set)
data[0]['name']

# Mostrando qual a carta acima

# imgurl = data[0]['images']['large']
# resp = req.get(imgurl)
# img = Image.open(BytesIO(resp.content))
# img.show()


# In[ ]:


# Campos-chave dentro do dicionário
data[0].keys()


# In[ ]:


df = pd.DataFrame(data=data)

# Resumo das colunas do dataframe
df.info()


# # Funções para auxiliar o tratamento das bases

# In[ ]:


# Verificar se a carta está no formato standard
def is_standard_format(x):

    if 'standard' in x:
        return 1

    else:
        return 0


# In[ ]:


# Verificar qual o formato da carta, começando do mais barato para o mais caro
def get_card_foil_type(x):

    foil_list = ['normal','holofoil','reverseHolofoil','1stEditionHolofoil']
    foil_valid = ''

    for foil in foil_list:

        if foil in x['prices']:

            foil_valid += foil
            break

    return foil_valid


# In[ ]:


# Verificar o preço de mercado (padrão) da carta com base no sua raridade/"foil"
def get_card_price(x,pricing = 'mid'):

    try:
        foil = get_card_foil_type(x)
        return x['prices'][foil][pricing]

    except:
        return 0


# In[ ]:


# Criando função para capturar os elementos arrays/map dentro de cada coluna
def get_dict_elements(df,column_name,key,pos=0):

        df_e = pd.DataFrame(df[column_name].fillna('').values.tolist(),index=df.index)

        e = [] # colocar os valores nesta lista

        if type(df[column_name][0]) == list:

            for i in np.arange(len(df_e)):

                try : 
                    e.append(df_e[pos][i][key])

                except TypeError:

                    if key == 'damage' or key == 'convertedEnergyCost':

                        e.append('0')
                    else:
                        e.append('')

            return pd.Series(e,name=key+str(pos)).fillna('')

        elif type(df[column_name][0]) == dict:
            
            return df_e[key]


# In[ ]:


def regex_findsymbol(x,symbol):

    pattern = '.*[' + symbol + ']'

    # função retorna TRUE se a expressão deu match e FALSE caso contrário
    return regex.match(pattern=pattern,string=x) != None


# In[ ]:


# A função regex é pra capturar o segundo grupo do padrão abaixo, onde constam apenas os valores do dano
def regex_get_added_damage(x):

    # Pegar o valor do dano entre os textos "does" e "damage"
    r = regex.search(pattern='(does|plus)\s([0-9]*)\s(more|damage).(?!to\sitself)',string=x)
    
    if r == None:
        return '0'
    else: 
        return r.group(2)


# In[ ]:


def get_dmg_output(df,
                    cols = ['damage0','damage1','damage2','damage3'],
                    cols_add = ['dmg0plus','dmg1plus','dmg2plus','dmg3plus'],
                    cols_total = ['totaldmg0','totaldmg1','totaldmg2','totaldmg3']):

    dict_sum_dmg = {}

    for col, col_add , col_total in zip(cols,cols_add,cols_total):
    
        sum_dmg = []

        for i in np.arange(len(df)):
            
            if regex_findsymbol(df[col][i],'+') == True:

                d1 = int(df[col][i].replace('+',''))
                d2 = int(df[col_add][i])

            elif regex_findsymbol(df[col][i],'×') == True:

                d1 = int(df[col][i].replace('×',''))*1
                d2 = 0

            elif regex_findsymbol(df[col][i],'-') == True:

                d1 = int(df[col][i].replace('-',''))
                d2 = 0

            else:

                d1 = int(df[col][i])
                d2 = int(df[col_add][i])

            d = d1 + d2

            sum_dmg.append(d)

        dict_sum_dmg[col_total] = sum_dmg
    
    return pd.DataFrame(dict_sum_dmg)


# In[ ]:


def DivideColumns(x,y):

    return np.where(y==0,0,x//y)


# In[ ]:


def find_prize_cards(x):
    
    pattern = 'your\sopponent\stakes\s(\d*)\sPrize\scards'

    r = regex.search(pattern=pattern,string=x)

    if r == None: 
        return 1

    else:
        return r.group(1)


# # Testando as funções criadas !

# In[ ]:


id=0
print(f' A carta {df.name[id]} é do tipo {get_card_foil_type(df.tcgplayer[id])}!')
print(f' A carta {df.name[id]} custa {get_card_price(df.tcgplayer[id])} dólares!')


# In[ ]:


get_dict_elements(df,'attacks','text')


# # Preparando a ABT de damage

# In[ ]:


# Series com os danos de cada ataque
dmg0 = get_dict_elements(df,'attacks','damage')
dmg1 = get_dict_elements(df,'attacks','damage',pos=1)
dmg2 = get_dict_elements(df,'attacks','damage',pos=2)
dmg3 = get_dict_elements(df,'attacks','damage',pos=3)

# Series com os textos de cada ataque
text0 = get_dict_elements(df,'attacks','text')
text1 = get_dict_elements(df,'attacks','text',pos=1)
text2 = get_dict_elements(df,'attacks','text',pos=2)
text3 = get_dict_elements(df,'attacks','text',pos=3)

# Series com os danos adicionais de cada ataque escritos nos textos
dmg0_plus = text0.apply(lambda row: regex_get_added_damage(row)).rename('dmg0plus')
dmg1_plus = text1.apply(lambda row: regex_get_added_damage(row)).rename('dmg1plus')
dmg2_plus = text2.apply(lambda row: regex_get_added_damage(row)).rename('dmg2plus')
dmg3_plus = text3.apply(lambda row: regex_get_added_damage(row)).rename('dmg3plus')

# Series com o custo de energia de cada ataque
cost0 = get_dict_elements(df,'attacks','convertedEnergyCost')
cost1 = get_dict_elements(df,'attacks','convertedEnergyCost',pos=1)
cost2 = get_dict_elements(df,'attacks','convertedEnergyCost',pos=2)
cost3 = get_dict_elements(df,'attacks','convertedEnergyCost',pos=3)


# In[ ]:


df_atk = pd.concat([text0, dmg0, dmg0_plus,
                    text1, dmg1, dmg1_plus,
                    text2, dmg2, dmg2_plus,
                    text3, dmg3, dmg3_plus],axis=1)

df_atk_energycost = pd.concat([cost0,cost1,cost2,cost3],axis=1).astype('int32')


# In[ ]:


df_atk_dmg = (
    df_atk
    .drop(['text0','text1','text2','text3'],axis=1)
    .replace('','0')
)

df_atk_total_dmg = get_dmg_output(df=df_atk_dmg)

df_atk_total_dmg.head()


# In[ ]:


df_atk_final = (
    df_atk_total_dmg
    .merge(right = df_atk_energycost,how='left',left_index=True,right_index=True)
    .assign(num_attacks      = lambda df : sum(df[col]>0 for col in df_atk_total_dmg.columns))
    .assign(total_damage     = lambda df : sum(df[col]   for col in df_atk_total_dmg.columns))
    .assign(total_energycost = lambda df : sum(df[col]   for col in df_atk_energycost.columns))
    .assign(dmg_per_atk      = lambda df : DivideColumns(
                                            DivideColumns(df.totaldmg0, df.convertedEnergyCost0)+
                                            DivideColumns(df.totaldmg1, df.convertedEnergyCost1)+
                                            DivideColumns(df.totaldmg2, df.convertedEnergyCost2)+
                                            DivideColumns(df.totaldmg3, df.convertedEnergyCost3),df.num_attacks))
)

df_atk_final.head()
# df_atk_final.sort_values(by='dmg_per_atk',ascending=False).head(10)


# In[ ]:


abt_cols = ['name','subtypes','hp','weaknesses','resistances','convertedRetreatCost','rules','legalities','tcgplayer']

df_abt = df[abt_cols].copy()

df_abt = (
    df_abt
    .assign(subtypes    = (df['subtypes'][i][0] for i in range(len(df.subtypes))))
    .assign(weaknesses  = lambda df: df['weaknesses'].notnull()*1)
    .assign(resistances = lambda df: df['resistances'].notnull()*1)
    .assign(rules       = lambda df: df['rules'].fillna('-'))
    .assign(prize_cards = lambda df: df['rules'].apply(lambda x: find_prize_cards(x[0])))
    .assign(convertedRetreatCost = lambda df : df['convertedRetreatCost'].fillna(0))
    .assign(standard_format      = lambda df : df['legalities'].apply(lambda x: is_standard_format(x)))
    .assign(card_price           = lambda df : df['tcgplayer'].apply(lambda x : get_card_price(x)))
    .drop(['rules','legalities','tcgplayer'], axis=1)
)


# In[ ]:


df_abt_final = (
    df_abt
    .iloc[:,2:]
    .merge(df_atk_final.iloc[:,-4:-1], how='left', right_index=True, left_index=True)
    .astype('int32')
)


# In[ ]:


df_abt_final


# In[ ]:


# Definindo algumas variáveis para rodar o modelo de otimização linear

# Array com todos os índices da abt
pkmn_index = np.arange(len(df_abt_final))

# Lista com os valores da pontuação total de cada pokemon
total_stats = [df_abt_final.hp[i]+df_abt_final.total_damage[i] for i in pkmn_index]
card_price   = [df_abt_final.card_price[i] for i in pkmn_index]

# Restrições impostas sobre o modelo
constraint1 = df_abt_final[df_abt_final.standard_format==1].index
constraint2 = df_abt_final[df_abt_final.convertedRetreatCost<=2].index
constraint3 = df_abt_final[df_abt_final.resistances==1].index


# In[ ]:


import pulp

# Definindo o problema e a variável a ser otimizada (x)
prob = pulp.LpProblem('BestPokemonCards',pulp.LpMaximize)
x    = pulp.LpVariable.dicts("x", pkmn_index, cat=pulp.LpBinary)

# Função Objetivo
objective_function = sum(total_stats[pkmn] * x[pkmn] for pkmn in pkmn_index)
prob += objective_function

# Adicionando no modelo as restrições
prob += sum([x[pkmn] for pkmn in pkmn_index]) == 5
prob += sum([x[pkmn] for pkmn in constraint1]) == 5
prob += sum([x[pkmn] for pkmn in constraint2]) >= 1
prob += sum([x[pkmn] for pkmn in constraint3]) >= 1
prob += sum([card_price[pkmn] * x[pkmn] for pkmn in pkmn_index]) <= 100

# Rodando...
prob.solve()


# In[ ]:


for i in pkmn_index:

    if x[i].value() == 1:

        print(data[i]['tcgplayer']['prices'])


# In[ ]:


# Mostrando qual a carta acima
from PIL import Image
from io import BytesIO

for i in pkmn_index:

    if x[i].value() == 1:

        imgurl = data[i]['images']['large']
        resp = req.get(imgurl)
        img = Image.open(BytesIO(resp.content))
        img.show()


# In[ ]:


# Apenas os ataques com multiplicadores no dano
#df_atk[df_atk.damage0.apply(lambda x : regex_findsymbol(x,'×'))].tail(15)


# In[ ]:


# Ataques cujo dano possui o símbolo de "-" e sua descrição
# Segunda Opção : df_atk[df_atk.damage0.str.contains('.*[-]')]['text0'].head(20).values

#df_atk[~df_atk.damage0.apply(lambda x : regex_findsymbol(x,'+'))]


# In[ ]:


# Ataques cujo dano possui o símbolo de "×" e sua descrição
# Condição extra : df_atk.text0.str.contains('Flip [a-z0-9] coin')
# df_atk[df_atk.damage0.str.contains('.*[×]')]['text0'].head(20).values

