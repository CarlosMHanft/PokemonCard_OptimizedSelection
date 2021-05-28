{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python376jvsc74a57bd0b4d048287b625e6b2bf5fd29a7b10154da967647322904e46e9c9197bc80a356",
   "display_name": "Python 3.7.6 64-bit ('base': conda)"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# !pip install requests\n",
    "# !pip install pulp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import requests as req\n",
    "import re as regex\n",
    "from time import sleep"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Fonte : https://docs.pokemontcg.io/#documentationrate_limits\n",
    "\n",
    "###################################################################################################\n",
    "# Code \tName \t                Description\n",
    "###################################################################################################\n",
    "# 400 \tBad Request \t        We could not process that action\n",
    "# 403 \tForbidden \t            You exceeded the rate limit\n",
    "# 404 \tNot Found \t            The requested resource could not be found\n",
    "# 500 \tInternal Server Error \tWe had a problem with our server. Please try again later\n",
    "# 503 \tService Unavailable \tWe are temporarily offline for maintenance. Please try again later\n",
    "###################################################################################################\n",
    "\n",
    "dict_error_code = {\n",
    "    200: 'Success !',\n",
    "    400: 'Bad Request.',\n",
    "    403: 'Forbidden !',\n",
    "    404: 'Not Found.',\n",
    "    500: 'Internal Server Error !',\n",
    "    503: 'Service Unavailable !'\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Definindo a URL da API e os parâmetros/condições a serem incluídas nela\n",
    "url = \"https://api.pokemontcg.io/v2/sets\"\n",
    "\n",
    "# Chamando a API do Pokemon TCG\n",
    "response = req.get(url)\n",
    "\n",
    "# Retornar o resultado do request\n",
    "print(f' Resultado : ' + dict_error_code[response.status_code])\n",
    "\n",
    "# dados de cada set de cartas\n",
    "sets = response.json()['data']\n",
    "\n",
    "# Lista com os IDs de cada set\n",
    "set_names = [sets[i]['id'] for i in np.arange(len(sets))]"
   ]
  },
  {
   "source": [
    "# Aplicando um loop pra retornar dados de pokémons de cada set\n",
    "\n",
    "data = []\n",
    "\n",
    "for s in set_names:\n",
    "\n",
    "    url = \"https://api.pokemontcg.io/v2/cards\"\n",
    "    params = 'q=supertype:pokemon set.id:' + s\n",
    "\n",
    "    # Chamando a API do Pokemon TCG\n",
    "    response = req.get(url,params=params)\n",
    "\n",
    "    # Convertendo o request em arquivo JSON e contando quantos registros este retornou\n",
    "    response_json = response.json()\n",
    "    dataset = response_json['data']\n",
    "    data.extend(dataset)\n",
    "\n",
    "    # Retornar o resultado do request\n",
    "    print(f' Set {s} ( {len(response_json[\"data\"])} linhas ): {dict_error_code[response.status_code]}')\n",
    "    sleep(0.2)"
   ],
   "cell_type": "code",
   "metadata": {},
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(f'O tipo da request da API: {type(response_json)}')\n",
    "print(f'O tipo do elemento dentro da API (\"data\"): {type(data)}')\n",
    "print(f'O tipo de um elemento da lista em data: {type(data[0])}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# O primeiro pokémon do primeiro conjunto de cartas de Pokémon (Base Set)\n",
    "data[0]['name']\n",
    "\n",
    "# Mostrando qual a carta acima\n",
    "\n",
    "# imgurl = data[0]['images']['large']\n",
    "# resp = req.get(imgurl)\n",
    "# img = Image.open(BytesIO(resp.content))\n",
    "# img.show()"
   ]
  },
  {
   "source": [
    "# Campos-chave dentro do dicionário\n",
    "data[0].keys()"
   ],
   "cell_type": "code",
   "metadata": {},
   "execution_count": null,
   "outputs": []
  },
  {
   "source": [
    "df = pd.DataFrame(data=data)\n",
    "\n",
    "# Resumo das colunas do dataframe\n",
    "df.info()"
   ],
   "cell_type": "code",
   "metadata": {},
   "execution_count": null,
   "outputs": []
  },
  {
   "source": [
    "# Funções para auxiliar o tratamento das bases"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Verificar se a carta está no formato standard\n",
    "def is_standard_format(x):\n",
    "\n",
    "    if 'standard' in x:\n",
    "        return 1\n",
    "\n",
    "    else:\n",
    "        return 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Verificar qual o formato da carta, começando do mais barato para o mais caro\n",
    "def get_card_foil_type(x):\n",
    "\n",
    "    foil_list = ['normal','holofoil','reverseHolofoil','1stEditionHolofoil']\n",
    "    foil_valid = ''\n",
    "\n",
    "    for foil in foil_list:\n",
    "\n",
    "        if foil in x['prices']:\n",
    "\n",
    "            foil_valid += foil\n",
    "            break\n",
    "\n",
    "    return foil_valid"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Verificar o preço de mercado (padrão) da carta com base no sua raridade/\"foil\"\n",
    "def get_card_price(x,pricing = 'mid'):\n",
    "\n",
    "    try:\n",
    "        foil = get_card_foil_type(x)\n",
    "        return x['prices'][foil][pricing]\n",
    "\n",
    "    except:\n",
    "        return 0\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Criando função para capturar os elementos arrays/map dentro de cada coluna\n",
    "def get_dict_elements(df,column_name,key,pos=0):\n",
    "\n",
    "        df_e = pd.DataFrame(df[column_name].fillna('').values.tolist(),index=df.index)\n",
    "\n",
    "        e = [] # colocar os valores nesta lista\n",
    "\n",
    "        if type(df[column_name][0]) == list:\n",
    "\n",
    "            for i in np.arange(len(df_e)):\n",
    "\n",
    "                try : \n",
    "                    e.append(df_e[pos][i][key])\n",
    "\n",
    "                except TypeError:\n",
    "\n",
    "                    if key == 'damage' or key == 'convertedEnergyCost':\n",
    "\n",
    "                        e.append('0')\n",
    "                    else:\n",
    "                        e.append('')\n",
    "\n",
    "            return pd.Series(e,name=key+str(pos)).fillna('')\n",
    "\n",
    "        elif type(df[column_name][0]) == dict:\n",
    "            \n",
    "            return df_e[key]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def regex_findsymbol(x,symbol):\n",
    "\n",
    "    pattern = '.*[' + symbol + ']'\n",
    "\n",
    "    # função retorna TRUE se a expressão deu match e FALSE caso contrário\n",
    "    return regex.match(pattern=pattern,string=x) != None"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# A função regex é pra capturar o segundo grupo do padrão abaixo, onde constam apenas os valores do dano\n",
    "def regex_get_added_damage(x):\n",
    "\n",
    "    # Pegar o valor do dano entre os textos \"does\" e \"damage\"\n",
    "    r = regex.search(pattern='(does|plus)\\s([0-9]*)\\s(more|damage).(?!to\\sitself)',string=x)\n",
    "    \n",
    "    if r == None:\n",
    "        return '0'\n",
    "    else: \n",
    "        return r.group(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_dmg_output(df,\n",
    "                    cols = ['damage0','damage1','damage2','damage3'],\n",
    "                    cols_add = ['dmg0plus','dmg1plus','dmg2plus','dmg3plus'],\n",
    "                    cols_total = ['totaldmg0','totaldmg1','totaldmg2','totaldmg3']):\n",
    "\n",
    "    dict_sum_dmg = {}\n",
    "\n",
    "    for col, col_add , col_total in zip(cols,cols_add,cols_total):\n",
    "    \n",
    "        sum_dmg = []\n",
    "\n",
    "        for i in np.arange(len(df)):\n",
    "            \n",
    "            if regex_findsymbol(df[col][i],'+') == True:\n",
    "\n",
    "                d1 = int(df[col][i].replace('+',''))\n",
    "                d2 = int(df[col_add][i])\n",
    "\n",
    "            elif regex_findsymbol(df[col][i],'×') == True:\n",
    "\n",
    "                d1 = int(df[col][i].replace('×',''))*1\n",
    "                d2 = 0\n",
    "\n",
    "            elif regex_findsymbol(df[col][i],'-') == True:\n",
    "\n",
    "                d1 = int(df[col][i].replace('-',''))\n",
    "                d2 = 0\n",
    "\n",
    "            else:\n",
    "\n",
    "                d1 = int(df[col][i])\n",
    "                d2 = int(df[col_add][i])\n",
    "\n",
    "            d = d1 + d2\n",
    "\n",
    "            sum_dmg.append(d)\n",
    "\n",
    "        dict_sum_dmg[col_total] = sum_dmg\n",
    "    \n",
    "    return pd.DataFrame(dict_sum_dmg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def DivideColumns(x,y):\n",
    "\n",
    "    return np.where(y==0,0,x//y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def find_prize_cards(x):\n",
    "    \n",
    "    pattern = 'your\\sopponent\\stakes\\s(\\d*)\\sPrize\\scards'\n",
    "\n",
    "    r = regex.search(pattern=pattern,string=x)\n",
    "\n",
    "    if r == None: \n",
    "        return 1\n",
    "\n",
    "    else:\n",
    "        return r.group(1)"
   ]
  },
  {
   "source": [
    "# Testando as funções criadas !"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "source": [
    "id=0\n",
    "print(f' A carta {df.name[i]} é do tipo {get_card_foil_type(df.tcgplayer[i])}!')\n",
    "print(f' A carta {df.name[i]} custa {get_card_price(df.tcgplayer[i])} dólares!')"
   ],
   "cell_type": "code",
   "metadata": {},
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "get_dict_elements(df,'attacks','text')"
   ]
  },
  {
   "source": [
    "# Preparando a ABT de damage"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Series com os danos de cada ataque\n",
    "dmg0 = get_dict_elements(df,'attacks','damage')\n",
    "dmg1 = get_dict_elements(df,'attacks','damage',pos=1)\n",
    "dmg2 = get_dict_elements(df,'attacks','damage',pos=2)\n",
    "dmg3 = get_dict_elements(df,'attacks','damage',pos=3)\n",
    "\n",
    "# Series com os textos de cada ataque\n",
    "text0 = get_dict_elements(df,'attacks','text')\n",
    "text1 = get_dict_elements(df,'attacks','text',pos=1)\n",
    "text2 = get_dict_elements(df,'attacks','text',pos=2)\n",
    "text3 = get_dict_elements(df,'attacks','text',pos=3)\n",
    "\n",
    "# Series com os danos adicionais de cada ataque escritos nos textos\n",
    "dmg0_plus = text0.apply(lambda row: regex_get_added_damage(row)).rename('dmg0plus')\n",
    "dmg1_plus = text1.apply(lambda row: regex_get_added_damage(row)).rename('dmg1plus')\n",
    "dmg2_plus = text2.apply(lambda row: regex_get_added_damage(row)).rename('dmg2plus')\n",
    "dmg3_plus = text3.apply(lambda row: regex_get_added_damage(row)).rename('dmg3plus')\n",
    "\n",
    "# Series com o custo de energia de cada ataque\n",
    "cost0 = get_dict_elements(df,'attacks','convertedEnergyCost')\n",
    "cost1 = get_dict_elements(df,'attacks','convertedEnergyCost',pos=1)\n",
    "cost2 = get_dict_elements(df,'attacks','convertedEnergyCost',pos=2)\n",
    "cost3 = get_dict_elements(df,'attacks','convertedEnergyCost',pos=3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_atk = pd.concat([text0, dmg0, dmg0_plus,\n",
    "                    text1, dmg1, dmg1_plus,\n",
    "                    text2, dmg2, dmg2_plus,\n",
    "                    text3, dmg3, dmg3_plus],axis=1)\n",
    "\n",
    "df_atk_energycost = pd.concat([cost0,cost1,cost2,cost3],axis=1).astype('int32')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_atk_dmg = (\n",
    "    df_atk\n",
    "    .drop(['text0','text1','text2','text3'],axis=1)\n",
    "    .replace('','0')\n",
    ")\n",
    "\n",
    "df_atk_total_dmg = get_dmg_output(df=df_atk_dmg)\n",
    "\n",
    "df_atk_total_dmg.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_atk_final = (\n",
    "    df_atk_total_dmg\n",
    "    .merge(right = df_atk_energycost,how='left',left_index=True,right_index=True)\n",
    "    .assign(num_attacks      = lambda df : sum(df[col]>0 for col in df_atk_total_dmg.columns))\n",
    "    .assign(total_damage     = lambda df : sum(df[col]   for col in df_atk_total_dmg.columns))\n",
    "    .assign(total_energycost = lambda df : sum(df[col]   for col in df_atk_energycost.columns))\n",
    "    .assign(dmg_per_atk      = lambda df : DivideColumns(\n",
    "                                            DivideColumns(df.totaldmg0, df.convertedEnergyCost0)+\n",
    "                                            DivideColumns(df.totaldmg1, df.convertedEnergyCost1)+\n",
    "                                            DivideColumns(df.totaldmg2, df.convertedEnergyCost2)+\n",
    "                                            DivideColumns(df.totaldmg3, df.convertedEnergyCost3),df.num_attacks))\n",
    ")\n",
    "\n",
    "df_atk_final.head()\n",
    "# df_atk_final.sort_values(by='dmg_per_atk',ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "abt_cols = ['name','subtypes','hp','weaknesses','resistances','convertedRetreatCost','rules','legalities','tcgplayer']\n",
    "\n",
    "df_abt = df[abt_cols].copy()\n",
    "\n",
    "df_abt = (\n",
    "    df_abt\n",
    "    .assign(subtypes    = (df['subtypes'][i][0] for i in range(len(df.subtypes))))\n",
    "    .assign(weaknesses  = lambda df: df['weaknesses'].notnull()*1)\n",
    "    .assign(resistances = lambda df: df['resistances'].notnull()*1)\n",
    "    .assign(rules       = lambda df: df['rules'].fillna('-'))\n",
    "    .assign(prize_cards = lambda df: df['rules'].apply(lambda x: find_prize_cards(x[0])))\n",
    "    .assign(convertedRetreatCost = lambda df : df['convertedRetreatCost'].fillna(0))\n",
    "    .assign(standard_format      = lambda df : df['legalities'].apply(lambda x: is_standard_format(x)))\n",
    "    .assign(card_price           = lambda df : df['tcgplayer'].apply(lambda x : get_card_price(x)))\n",
    "    .drop(['rules','legalities','tcgplayer'], axis=1)\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_abt_final = (\n",
    "    df_abt\n",
    "    .iloc[:,2:]\n",
    "    .merge(df_atk_final.iloc[:,-4:-1], how='left', right_index=True, left_index=True)\n",
    "    .astype('int32')\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_abt_final"
   ]
  },
  {
   "source": [
    "# Definindo algumas variáveis para rodar o modelo de otimização linear\n",
    "\n",
    "# Array com todos os índices da abt\n",
    "pkmn_index = np.arange(len(df_abt_final))\n",
    "\n",
    "# Lista com os valores da pontuação total de cada pokemon\n",
    "total_stats = [df_abt_final.hp[i]+df_abt_final.total_damage[i] for i in pkmn_index]\n",
    "card_price   = [df_abt_final.card_price[i] for i in pkmn_index]\n",
    "\n",
    "# Restrições impostas sobre o modelo\n",
    "constraint1 = df_abt_final[df_abt_final.standard_format==1].index\n",
    "constraint2 = df_abt_final[df_abt_final.convertedRetreatCost<=2].index\n",
    "constraint3 = df_abt_final[df_abt_final.resistances==1].index"
   ],
   "cell_type": "code",
   "metadata": {},
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pulp\n",
    "\n",
    "# Definindo o problema e a variável a ser otimizada (x)\n",
    "prob = pulp.LpProblem('BestPokemonCards',pulp.LpMaximize)\n",
    "x    = pulp.LpVariable.dicts(\"x\", pkmn_index, cat=pulp.LpBinary)\n",
    "\n",
    "# Função Objetivo\n",
    "objective_function = sum(total_stats[pkmn] * x[pkmn] for pkmn in pkmn_index)\n",
    "prob += objective_function\n",
    "\n",
    "# Adicionando no modelo as restrições\n",
    "prob += sum([x[pkmn] for pkmn in pkmn_index]) == 5\n",
    "prob += sum([x[pkmn] for pkmn in constraint1]) == 5\n",
    "prob += sum([x[pkmn] for pkmn in constraint2]) >= 1\n",
    "prob += sum([x[pkmn] for pkmn in constraint3]) >= 1\n",
    "prob += sum([card_price[pkmn] * x[pkmn] for pkmn in pkmn_index]) <= 100\n",
    "\n",
    "# Rodando...\n",
    "prob.solve()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in pkmn_index:\n",
    "\n",
    "    if x[i].value() == 1:\n",
    "\n",
    "        print(data[i]['tcgplayer']['prices'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mostrando qual a carta acima\n",
    "from PIL import Image\n",
    "from io import BytesIO\n",
    "\n",
    "for i in pkmn_index:\n",
    "\n",
    "    if x[i].value() == 1:\n",
    "\n",
    "        imgurl = data[i]['images']['large']\n",
    "        resp = req.get(imgurl)\n",
    "        img = Image.open(BytesIO(resp.content))\n",
    "        img.show()"
   ]
  },
  {
   "source": [
    "# Apenas os ataques com multiplicadores no dano\n",
    "#df_atk[df_atk.damage0.apply(lambda x : regex_findsymbol(x,'×'))].tail(15)"
   ],
   "cell_type": "code",
   "metadata": {},
   "execution_count": null,
   "outputs": []
  },
  {
   "source": [
    "# Ataques cujo dano possui o símbolo de \"-\" e sua descrição\n",
    "# Segunda Opção : df_atk[df_atk.damage0.str.contains('.*[-]')]['text0'].head(20).values\n",
    "\n",
    "#df_atk[~df_atk.damage0.apply(lambda x : regex_findsymbol(x,'+'))]"
   ],
   "cell_type": "code",
   "metadata": {},
   "execution_count": null,
   "outputs": []
  },
  {
   "source": [
    "# Ataques cujo dano possui o símbolo de \"×\" e sua descrição\n",
    "# Condição extra : df_atk.text0.str.contains('Flip [a-z0-9] coin')\n",
    "# df_atk[df_atk.damage0.str.contains('.*[×]')]['text0'].head(20).values"
   ],
   "cell_type": "code",
   "metadata": {},
   "execution_count": null,
   "outputs": []
  }
 ]
}