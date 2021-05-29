![pokemontcglogo](pkmn_images/pokemontcgbiglogo.png)

Este projeto foi criado para ajudar os jogadores de Pokémon TCG a **escolherem as melhores cartas com base nas suas estratégias e conectar as metodologias em ciência de dados dentro do Pokémon**.

O objetivo deste trabalho é tornar o cenário de pokémon um pouco mais inserido no mundo de tecnologia e aumentar a competitividade do jogo, onde as decisões e as táticas de jogo serão baseadas em dados ao invés de raciocínio lógico invidividual e pura experiência.

Encontramos pouca aplicação de dados na tomada de decisão dentro do cenário de E-Sports que este projeto está surgindo justamente pra preencher esta lacuna e estimular um pouco mais o uso de ciência de dados dentro de segmentos como este de jogos em geral (alguns exemplos já aparecem dentro do esporte convecional mas também são pouco relevantes na dia-a-dia) 

A ideia principal é facilitar a tomada de decisão do jogador antes de preparar seu baralho e está com as seguintes dificuldades:

    Como saber se determinada carta é boa em comparação com as demais ?
    Aquele pokémon é a melhor escolha pra estratégia do meu baralho ?
    Há muitas cartas para pesquisar e analisar (dificuldade para os iniciantes e menos experientes)
    Preciso saber quais estão neste formato antes de tomar uma decisão

Com o modelo, estas dificuldades em determinar aquela carta que atendará suas necessidades será reduzida.

Usando dados provenientes de uma API, o modelo otimiza algumas características das cartas para trazer a melhor seleção de acordo com o que o jogador estiver buscando para montar seu baralho.

API: [Pokémon TCG Developers](https://pokemontcg.io/)


### IMPORTANTE : Por enquanto não temos as estatísticas de jogo pra estimar a eficácia de uma carta contra diversas estratégias, por isso a ideia é dar a melhor carta para uma determinada estratégia. Não podemos presumir que aquela carta fará parte de um baralho vitorioso em campeonatos porque não há dados disponíveis ainda para tal modelagem.

 
Vou explicar o passo-a-passo da metodologia utilizada:

1. Os dados extraídos da API
2. As transformções feitas para chegar na tabela com os dados puros de cada carta
3. Premisssas do projeto
4. Modelo de otimização linear com PuLP
5. Próximos passos...

