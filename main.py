import streamlit as st


import streamlit as st
import importlib.util
from pathlib import Path


import streamlit as st
import runpy

# Configuração da página
st.set_page_config(page_title="Guia Conceitual - Algorithmic Trading ", layout="wide")

# Função para exibir imagens
def mostrar_imagem(imagem_path, legenda):
    st.image(imagem_path, caption=legenda, use_column_width=True)

# Sidebar para Modo de Seleção
st.sidebar.title("Seleção de Modo")
mode = st.sidebar.radio("Selecione o Modo:", options=["Navegação", "Chat"], index=0)

st.sidebar.markdown("---")

# Se o modo selecionado for "Navegação", exibe as páginas principais
if mode == "Navegação":
    st.sidebar.title("Seções")
    pagina = st.sidebar.radio(
        "Escolha uma seção", 
        [
            "1 . Introdução", 
            "2 . Backtesting", 
            "3 . Os Fundamentos da Reversão à Média", 
            "4 . Estratégias de Reversão à Média", 
            "5 . Reversão à Média de Ações e ETFs", 
            "6 . Reversão à Média de Moedas e Futuros", 
            "7 . Estratégias de Momentum Interdiário", 
            "8 . Estratégias de Momentum Intradiário", 
            "9 . Gestão de Riscos", 
            "10 . Conclusão", 
            "Referências"
        ]
    )
    # Função para exibir subseções
    def mostrar_subsecoes(pagina_atual):
        subsecoes = {
            "2 . Backtesting": [
                "Introdução",
                "A Importância do Backtesting",
                "Armadilhas Comuns no Backtesting",
                "Significância Estatística do Backtesting: Teste de Hipóteses",
                "Quando não fazer Backtest em uma estratégia",
                "Um Backtest Será Preditivo de Retornos Futuros?",
                "Conclusão"

            ],
            "3 . Os Fundamentos da Reversão à Média": [
                "Introdução",
                "1. Mean Reversion and Stationarity",
                "2. Cointegração",
                "3. Prós e Contras da Reversão a média",
                "4. Resumo"
            ],
            "4 . Estratégias de Reversão à Média": [
                "Introdução",
                "Trading Pairs",
                "Bollinger Bands",
                "Kalman Filter",
                "Erros nos Dados",
                "Conclusão"
            ],
            "5 . Reversão à Média de Ações e ETFs": [
                "Introdução",
                "Desafios na Negociação de Pares de Ações",
                "Buy-on-Gap Model",
                "Arbitragem entre um ETF e suas Ações Componentes",
                "Cross-Sectional Mean Reversion",
                "Conclusão"
            ],
              "6 . Reversão à Média de Moedas e Futuros": [
                  "Introdução",
                  "Negociação de Pares de Moedas",
                  "Taxas Cruzadas de Moedas",
                  "Operando Calendar Spread com Futuros",
                  "Spreads Intermercado com Futuros",
                  "Conclusão"
            ],
            "7 . Estratégias de Momentum Interdiário": [
                  "Introdução",
                  "Testes para Momentum em Séries Temporais",
                  "Estratégias de Séries Temporais",
                  "Extraindo Retornos de Rolagem",
                  "Estratégias Cross-Sectional",
                  "Prós e Contras das Estratégias de Momentum",
                  "Conclusão"
            ],
            "8 . Estratégias de Momentum Intradiário": [
                "Introdução",
                "Opening Gap Strategy",
                "News Sentiment",
                "Leveraged ETF Strategy",
                "Estratégias de Alta Frequência",
                "Conclusão"
            ],
            "9 . Gestão de Riscos": [
                "Introdução",
                "Alavancagem",
                "Indicadores e métricas",
                "Conclusão"
            ]
        }
        if pagina_atual in subsecoes:
            return st.sidebar.radio("Subseções", subsecoes[pagina_atual])
        return None
    # Navegação das subseções
    subsecao = mostrar_subsecoes(pagina)

# ====================================================================================

    # ==================== Introdução 
     
    if pagina == "1 . Introdução":
        st.title("Introdução ao Algoritmo Trading")
        
        st.markdown(r"""
        Este curso oferece um guia prático sobre estratégias de trading que podem ser implementadas tanto por traders individuais quanto institucionais. Diferente de abordagens puramente teóricas, o foco está em estratégias que realmente são usadas no mercado.
                    
        Vamos explorar uma ampla gama de estratégias, divididas em dois grandes grupos: estratégias de reversão à média e estratégias de momentum. Cada categoria será explicada em detalhes, com ênfase tanto nas técnicas padrão de trading quanto nos fundamentos que justificam o funcionamento dessas estratégias.
                    
        ---
        ### Estratégias de Reversão à Média
                    
        No campo das estratégias de reversão à média, cobriremos diversas técnicas estatísticas para detectar a reversão à média em séries temporais. Entre elas estão:

            Teste Dickey-Fuller Aumentado (ADF);
            Exponente de Hurst;
            Teste da Razão de Variância;
            Meia-vida.

        Também discutiremos a cointegração, utilizando testes como:

            Teste Dickey-Fuller Aumentado para Cointegração (CADF);
            Teste de Johansen.

        O foco será explicar de forma intuitiva o que cada um desses testes realmente mede e as equações matemáticas simples por trás deles.

        #### Técnicas de Trading com Reversão à Média

        Abordaremos as técnicas mais simples e eficazes para operar portfólios que seguem a reversão à média, como:
                    
            Linear
            Bandas de Bollinger;
            Filtro de Kalman.

        Discutiremos a melhor forma de usar dados de preços para essas estratégias: preços brutos, logaritmos dos preços ou suas razões. O filtro de Kalman, em especial, será apresentado como uma ferramenta valiosa em diversas estratégias. Também faremos distinção entre reversão à média em séries temporais e reversão à média cross-sectional (entre diferentes ativos).

        #### Exemplos Práticos

        Os exemplos de estratégias de reversão à média incluirão:

            Modelos de ações interdiários e intradiários;
            Pares e triplas de fundos negociados em bolsa (ETFs);
            Spreads de futuros.

        Além disso, vamos discutir como a ascensão dos dark pools e do high-frequency trading tornaram essas estratégias mais desafiadoras nos últimos anos.
                    
        ---           
        ### Estratégias de Momentum

        Por outro lado, as estratégias de momentum são guiadas por quatro principais fatores que impulsionam esse comportamento em ações e futuros. Veremos como extrair momentum a partir de séries temporais e entre diferentes ativos. Novas abordagens, como aquelas baseadas em eventos de notícias, sentimento de mercado, fluxo de ordens e trading de alta frequência, também serão exploradas.
                    
        ---                       
        ### Armadilhas Comuns

        Uma parte importante deste curso será dedicada a discutir as armadilhas comuns que podem fazer com que os resultados do trading divergam significativamente dos backtests. Questões como overfitting e viés de sobrevivência serão abordadas.

        """)
             
    # ==================== Introdução

# ====================================================================================

#  ====================  Chapter 1  Backtesting e Execução Automática ==============

    elif pagina == "2 . Backtesting":
        st.title("Backtesting e Execução Automática")

        if subsecao == "Introdução":
            st.markdown(r"""                      
            Embora o foco deste curso esteja nas categorias específicas de estratégias, é fundamental abordar algumas considerações importantes e armadilhas comuns antes de iniciar o backtesting (teste retroativo). Ignorar essas questões pode tornar o backtest inútil ou, pior, enganoso, resultando em perdas financeiras significativas.

            O backtesting é o processo de testar uma estratégia de trading com dados históricos para avaliar seu desempenho. No entanto, para que esse teste seja válido, é crucial evitar certas armadilhas comuns. Se essas precauções não forem tomadas, o resultado do backtest pode não refletir com precisão o desempenho futuro de uma estratégia.
                                    
            #### Importância da Significância Estatística

            Uma preocupação central no backtesting é a significância estatística dos resultados. Em outras palavras, até que ponto os resultados obtidos durante o teste podem ser considerados estatisticamente confiáveis? Para avaliar isso, utilizamos metodologias de testes de hipótese e simulações de Monte Carlo.

            * Quanto mais operações (trades) de ida e volta forem realizadas no backtest, maior será a confiabilidade estatística.
            * Mesmo que o backtest seja conduzido corretamente e com alta significância estatística, isso não garante que os retornos futuros serão previsíveis.

            #### Mudanças de Regime

            Outro fator importante são as mudanças de regime no mercado. Mesmo uma estratégia que tenha funcionado bem no passado pode ser completamente ineficaz no futuro devido a alterações nas condições de mercado. No curso, vamos discutir alguns exemplos históricos em que essas mudanças de regime prejudicaram estratégias previamente bem-sucedidas.
                                    
            #### Escolha da Plataforma de Software

            A escolha de uma plataforma de software adequada para realizar o backtest é outra consideração essencial que deve ser abordada desde o início. Uma plataforma eficiente pode aumentar significativamente sua produtividade, permitindo testar uma ampla gama de estratégias em diferentes classes de ativos.

            Além disso, uma boa plataforma de backtest ajuda a minimizar ou eliminar as armadilhas comuns, como overfitting (ajuste excessivo) e enviesamento de dados. Muitas vezes, a escolha da plataforma para backtesting está diretamente ligada à escolha de uma boa plataforma de execução automática, já que as melhores plataformas combinam ambas as funções.
                        
            """)

        elif subsecao == "A Importância do Backtesting":
            st.markdown(r"""              
        Backtesting é o processo de aplicar dados históricos a uma estratégia de trading para verificar como ela teria se comportado no passado. A ideia é que, se a estratégia funcionou bem com dados históricos, isso pode ser um indicativo de que ela também funcionará no futuro. A importância desse processo é evidente, especialmente quando desenvolvemos uma estratégia do zero. Queremos saber como ela teria performado antes de arriscarmos dinheiro real. Mesmo ao usar uma estratégia de uma publicação confiável, ainda é essencial realizar o backtesting por conta própria.
                                
        ### Por que fazer backtesting mesmo com estratégias publicadas?

        Existem várias razões pelas quais realizar seu próprio backtesting, mesmo com uma estratégia publicada, é crucial:

        1. Detalhes de Implementação Importam: Muitas vezes, a lucratividade de uma estratégia depende dos detalhes de sua implementação. Por exemplo:
            * As ordens de compra ou venda devem ser enviadas como ordens de "mercado na abertura" ou como ordens de mercado logo após a abertura?
            * Para contratos futuros, a ordem deve ser enviada antes do fechamento do mercado de ações (às 16h00) ou antes do fechamento do mercado futuro (às 16h15)?
            * Devemos usar o preço de compra, de venda ou o último preço para acionar uma negociação?

        Esses detalhes, frequentemente ignorados em artigos publicados, podem afetar significativamente a lucratividade de uma estratégia quando ela é executada ao vivo. A única forma de garantir que implementamos esses detalhes corretamente em nosso sistema automatizado de execução é através do backtesting.

        2. Transformar Backtesting em Execução Automática: Idealmente, o programa que usamos para backtestar a estratégia pode ser facilmente transformado em um programa de execução automática, garantindo que a estratégia seja implementada exatamente como planejado.

        3. Evitar Armadilhas Comuns: O backtesting nos permite analisar de perto a estratégia e identificar possíveis armadilhas. Alguns exemplos:
            * Em uma estratégia que envolve posições longas e curtas, consideramos o fato de que algumas ações podem ser difíceis de tomar emprestadas para vendas a descoberto?
            * Em uma estratégia de pares entre mercados futuros, certificamos-nos de que os preços de fechamento dos dois mercados são registrados ao mesmo tempo?

        Cada mercado e estratégia tem seu próprio conjunto de armadilhas específicas, e geralmente essas armadilhas inflacionam o desempenho da estratégia no backtest, fazendo parecer mais lucrativa do que realmente foi.

        4. Teste Out-of-Sample (Fora da Amostra): Uma das grandes vantagens de fazer o backtesting de uma estratégia publicada é a possibilidade de realizar um verdadeiro teste fora da amostra. Isso significa testar o desempenho da estratégia em um período de tempo após sua publicação. Se os resultados forem ruins nesse período, é um sinal de que a estratégia pode ter funcionado apenas em um conjunto limitado de dados. Isso é mais importante do que parece. Alguns autores podem ajustar seus modelos para que pareçam bons mesmo com dados fora da amostra.

        5. Refinar e Melhorar a Estratégia: Ao backtestar uma estratégia, podemos encontrar maneiras de refiná-la, tornando-a mais lucrativa ou menos arriscada. O processo de backtesting deve seguir o método científico:
            * Começamos com uma hipótese sobre uma oportunidade de arbitragem (baseada em nossa intuição ou em uma pesquisa).
            * Em seguida, confirmamos ou refutamos essa hipótese com um backtest.
            Se os resultados não forem bons, podemos modificar nossa hipótese e repetir o processo.

        Alterações simples, como ajustar o período de tempo para calcular a média móvel ou mudar o momento de entrada das ordens, podem melhorar significativamente o desempenho da estratégia.
                    """)

        elif subsecao == "Armadilhas Comuns no Backtesting":
            
            st.markdown(r"""
            ### Common Pitfalls of Backtesting

            #### Look-ahead Bias
            Look-ahead bias ocorre quando o programa de backtesting utiliza informações futuras, como os preços de amanhã, para determinar os sinais de negociação de hoje. Um exemplo comum é usar o preço máximo ou mínimo de um dia para definir um sinal de entrada no mesmo dia durante o backtesting, algo impossível de saber antes do fechamento do mercado. Esse viés é essencialmente um erro de programação, afetando apenas o backtesting, pois programas de negociação ao vivo não têm acesso a informações futuras.

            Uma forma eficaz de evitar esse viés é garantir que o programa utilizado para backtesting e negociação ao vivo seja o mesmo, mudando apenas o tipo de dado fornecido (histórico para backtesting e dados ao vivo para negociação). Algumas plataformas permitem essa abordagem, e serão discutidas mais adiante.
                        
            ---                               
            """)

            st.markdown("""
                ### Data-Snooping Bias and the Beauty of Linearity

                ##### Data-Snooping Bias
                Data-snooping bias ocorre quando muitos parâmetros livres são ajustados a padrões de mercado aleatórios do passado, gerando uma performance histórica ilusória e com pouca capacidade preditiva. Para evitar isso, deve-se testar o modelo em dados fora da amostra. Porém, ajustes excessivos nos modelos podem transformar os dados fora da amostra em dados ajustados.

                Uma alternativa é utilizar validação cruzada, dividindo os dados em vários subconjuntos para treinamento e validação. Modelos com alta simplicidade, poucas regras e menor número de parâmetros têm menor risco de viés. Modelos lineares geralmente são preferíveis a modelos não-lineares, pois estes últimos são mais complexos e mais suscetíveis ao viés.

                ##### O Papel dos Modelos Lineares
                Modelos lineares oferecem previsões mais simples e robustas. Por exemplo, fórmulas de capital alocadas linearmente, como no modelo Ornstein-Uhlenbeck, permitem estratégias como “scaling-in” para explorar séries de preços com reversão à média. Exemplos práticos incluem estratégias lineares de arbitragem estatística em ações.

                Um exemplo extremo de modelo linear é aquele com pesos iguais atribuídos a fatores preditivos. Normalizando esses fatores em Z-scores e combinando-os, pode-se prever retornos futuros ou, pelo menos, ranquear ativos de forma eficiente. Estratégias baseadas em rankings, como a "magic formula" de Joel Greenblatt, podem gerar retornos superiores ao mercado.

                Mesmo com precauções, o viés de data-snooping pode infiltrar-se. Por isso, testes finais devem incluir walk-forward testing com operações reais em pequena escala. Um bom resultado em negociação ao vivo é alcançar ao menos metade do Sharpe ratio obtido no backtesting.
                """)
            
            st.divider()
            st.markdown("""
                ### Stock Splits and Dividend Adjustments

                Quando uma empresa realiza um desdobramento de ações (stock split) no formato N-para-1, o preço das ações é dividido por N. Contudo, o número de ações possuídas pelo investidor aumenta proporcionalmente, mantendo o valor total do mercado inalterado. No entanto, durante o backtesting, geralmente analisamos apenas a série de preços, e sem ajustes para refletir o desdobramento, pode ocorrer uma queda abrupta no preço na data de vigência, gerando sinais de negociação incorretos.

                Para corrigir esse problema, é necessário ajustar os preços históricos dividindo-os por N antes da data de vigência. Essa prática também se aplica ao teste, ajustando os dados históricos antes da abertura do mercado na data relevante. Em casos de agrupamento reverso de ações (reverse split), os preços anteriores devem ser multiplicados por N.

                Da mesma forma, quando uma empresa paga dividendos, o preço das ações tende a cair pelo valor do dividendo (ausentes outros movimentos de mercado). Novamente, isso pode causar falsos sinais de negociação se os preços históricos não forem ajustados. Antes da data de pagamento do dividendo, deve-se subtrair o valor do dividendo dos preços históricos para refletir com precisão as mudanças no mercado.

                Esses ajustes também são essenciais para ETFs (fundos negociados em bolsa), embora opções possam exigir métodos mais complexos. Fontes confiáveis, como o site earnings.com, oferecem informações históricas sobre splits e dividendos, permitindo antecipar esses eventos em sistemas de negociação automatizados. Alternativamente, serviços como csidata.com fornecem dados históricos já ajustados para splits e dividendos.
                """)

            st.divider()
            st.markdown("""
                ### Survivorship Bias in Stock Database

                O viés de sobrevivência ocorre quando dados históricos utilizados para backtesting incluem apenas ações que ainda existem, excluindo aquelas que foram deslistadas, geralmente devido à falência. Isso pode gerar resultados distorcidos e excessivamente otimistas.  

                Por exemplo, uma estratégia que compra ações com quedas acentuadas pode parecer lucrativa em um backtest porque inclui apenas empresas que se recuperaram, ignorando as que faliram. Esse viés afeta principalmente estratégias long-only de reversão à média, que dependem de comprar ações depreciadas e vendê-las após a recuperação. Para estratégias short-only, o impacto é oposto: ações que faliram e não aparecem nos dados teriam contribuído positivamente para o retorno.

                Estratégias de momentum, por outro lado, são menos impactadas, pois o viés tende a reduzir os retornos short e aumentar os long, resultando em um efeito compensatório parcial.

                ##### Como Evitar o Viés de Sobrevivência
                1. **Dados Livres de Viés**: Utilize bases de dados que incluam ações deslistadas, como as oferecidas por csidata.com, kibot.com e tickdata.com. Essas bases geralmente listam ações deslistadas e evitam o viés de sobrevivência.
                
                2. **Coleta Própria**: Outra abordagem é armazenar os preços históricos de todas as ações de um índice diariamente, permitindo recriar um histórico livre de viés.

                3. **Backtests Recentes**: Se não for possível acessar dados completos, limite o backtesting aos últimos anos, pois o viés de sobrevivência é menos significativo em períodos curtos.

                Lembre-se de que a precisão dos dados é crucial para estratégias realistas e que resultados inflados devido ao viés de sobrevivência podem levar a decisões de investimento ruins.
            """)

            st.divider()
            st.markdown("""
                ### Primary versus Consolidated Stock Prices**

                Nos mercados de ações dos EUA, as negociações podem ocorrer em múltiplas plataformas, como NYSE, Nasdaq, ECNs e dark pools. Os preços históricos geralmente refletem dados consolidados, ou seja, a soma de todas essas plataformas. Contudo, estratégias que dependem de ordens de mercado no fechamento (MOC) ou na abertura (MOO) devem considerar apenas os preços da bolsa primária.

                ##### Problemas com Preços Consolidados
                1. **Diferenças entre Consolidados e Primários**: Preços consolidados podem incluir negociações atípicas realizadas em volumes baixos ou em horários diferentes dos leilões de abertura/fechamento da bolsa primária. Isso pode distorcer os dados e inflar artificialmente os resultados de backtesting.

                2. **Efeito em Estratégias de Reversão à Média**: O uso de preços consolidados pode superestimar os retornos de estratégias de reversão à média. Por exemplo, um preço atípico fora da bolsa primária pode parecer uma oportunidade de compra, mas não seria acessível no mercado real.

                ##### Soluções
                - **Utilizar Dados da Bolsa Primária**: Estratégias dependentes de MOC ou MOO devem basear-se nos preços históricos das bolsas primárias. Esses preços são mais representativos das condições reais de mercado.
                - **Cuidado com Altos e Baixos Consolidados**: Valores consolidados de máximas e mínimas frequentemente resultam de negociações esporádicas em mercados secundários, tornando-os inadequados para estratégias baseadas nesses indicadores.

                ##### Fontes de Dados
                - Assinaturas do Bloomberg oferecem acesso a preços históricos das bolsas primárias.
                - Alternativamente, é possível coletar dados ao vivo diretamente das bolsas e armazená-los em bases de dados personalizadas. Isso garante precisão e elimina a dependência de consolidados.

                Estratégias eficazes dependem da escolha correta dos dados. Preços consolidados podem ser úteis para algumas análises, mas estratégias específicas exigem a precisão dos preços da bolsa primária para garantir resultados realistas.
                """)

            st.divider()
            st.markdown(r"""
                ### Short-Sale Constraints

                Modelos de negociação que envolvem vendas a descoberto enfrentam restrições significativas, tornando a execução prática mais complexa do que o sugerido pelos backtests. Para realizar uma venda a descoberto, o corretor precisa localizar ações disponíveis para empréstimo, geralmente de instituições ou investidores com posições longas. Quando há grande interesse em shorting ou quando o float da ação é limitado, as ações tornam-se "difíceis de emprestar" (hard to borrow). Isso pode gerar custos adicionais, como juros pagos ao locador, ou até a impossibilidade de executar a venda.  

                Essas limitações foram exacerbadas durante a crise de 2008-2009, quando a SEC proibiu vendas a descoberto de ações financeiras por meses, criando retornos irreais em backtests de estratégias que shortavam ações indisponíveis. As ações de baixa capitalização (small caps) são mais afetadas por essas restrições do que as de grande capitalização (large caps), e até ETFs, como o SPY, podem ser difíceis de emprestar em momentos de estresse.

                Outra limitação é a **regra do uptick**, que esteve em vigor de 1938 a 2007 e foi substituída pela Alternative Uptick Rule em 2010. Esta regra exige que vendas a descoberto só sejam executadas acima do melhor preço de oferta nacional em mercados que sofreram quedas superiores a 10%. Isso limita ainda mais as ordens de mercado de venda a descoberto.

                Para backtests precisos, é crucial considerar se as ações eram emprestáveis ou se as regras do uptick estavam em vigor no período analisado. Ignorar essas restrições pode inflar artificialmente os resultados, comprometendo a validade dos modelos.
                """)

            st.divider()
            st.markdown(r"""
                ### Futures Continuous Contracts

                Contratos futuros possuem datas de vencimento, o que torna uma estratégia de trading focada em contratos futuros, como de petróleo bruto, uma combinação de várias operações em contratos diferentes. O momento de "rollover" (substituir o contrato próximo ao vencimento por um com prazo maior) pode variar: alguns preferem rolar contratos dias antes do vencimento, enquanto outros esperam por eventos como o cruzamento de interesse em aberto. Embora o rollover seja essencial, ele não contribui significativamente para os lucros, exceto pelo efeito do retorno de rolagem, discutido no Capítulo 5.

                ##### Dados de Contratos Contínuos
                A maioria dos fornecedores de dados históricos de futuros oferece séries ajustadas de contratos contínuos, que unem preços de contratos consecutivos. No entanto, essas séries podem introduzir problemas, como lacunas de preço em datas de rollover, resultando em cálculos incorretos de lucro e retorno. Para corrigir:
                1. **Ajuste de Preço**: Elimina lacunas ajustando os preços históricos para refletir mudanças entre contratos.
                2. **Ajuste de Retorno**: Garante que cálculos de retorno estejam corretos, mas pode comprometer os de lucro.

                Infelizmente, ajustar preços para lucros corretos pode tornar os cálculos de retorno imprecisos, e vice-versa. Isso obriga o trader a escolher entre priorizar lucro ou retorno no backtest.

                ##### Considerações sobre Ajustes
                1. **Preços Negativos**: O ajuste de preços pode gerar valores negativos em séries históricas distantes. Para mitigar, adiciona-se uma constante positiva a todos os preços.  
                2. **Estratégias de Spreads**: Para estratégias baseadas em diferenças de preço, o ajuste de preço é essencial para evitar sinais errados devido a erros de rollover. Já para estratégias baseadas em proporções de preços, o ajuste de retorno é mais adequado.

                A escolha do fornecedor de dados é crítica. Alguns, como csidata.com, ajustam apenas preços com a opção de evitar preços negativos. Outros, como tickdata.com, permitem escolher entre ajuste de preço ou retorno, mas não evitam preços negativos. Compreender como os ajustes são aplicados é essencial para garantir a precisão e a relevância do backtest.
                """)

            st.divider()
            st.markdown("""
                ### Futures Close versus Settlement Prices

                Os preços de fechamento diário fornecidos por provedores de dados de contratos futuros geralmente correspondem ao preço de liquidação ("settlement price") determinado pela bolsa, e não ao último preço negociado do dia. Mesmo em dias sem transações, os contratos futuros têm um preço de liquidação definido. 

                ##### Escolha do Preço para Backtests
                - **Preço de Liquidação**: É geralmente preferido, pois reflete melhor os preços próximos ao fechamento real das negociações, especialmente útil em estratégias como pares de futuros. Ele garante que os spreads sejam calculados com preços contemporâneos, desde que os contratos compartilhem o mesmo horário de fechamento.
                - **Último Preço Negociado**: Pode ser enganoso, especialmente se a última transação ocorreu muito antes do fechamento, tornando-o inadequado para estratégias que dependem de spreads, como arbitragem.

                ##### Estratégias Intraday e Spreads
                1. **Dados Intraday**: Para estratégias intraday ou spreads mais sensíveis, é necessário usar dados intraday detalhados com cotações bid-ask ou diretamente os spreads nativos da bolsa. 
                2. **Sincronização de Preços**: Últimos preços de contratos futuros ilíquidos podem não ser contemporâneos, criando spreads irreais que inflacionam os retornos de backtest. Isso é especialmente importante ao negociar contratos com baixa liquidez.

                ##### Considerações para Spreads Intermercados
                - **Horários de Fechamento Diferentes**: Contratos negociados em bolsas distintas podem ter horários de fechamento divergentes, resultando em spreads incorretos.
                - **Alternativas**: Para evitar problemas de sincronização, considere negociar ETFs que refletem futuros. Por exemplo, negocie GLD contra GDX em vez de GC contra GDX, já que ambos compartilham o mesmo horário de fechamento na Arca (4:00 p.m. ET).

                Escolher os dados certos (preço de liquidação, bid-ask intraday ou spreads nativos) é crucial para evitar resultados inflacionados e obter backtests mais realistas. A atenção à sincronização e à liquidez garante uma maior precisão nas estratégias baseadas em futuros.
                """)

        elif subsecao == "Significância Estatística do Backtesting: Teste de Hipóteses":
            st.markdown("""
                ### **Significância Estatística do Backtesting: Teste de Hipóteses**

                Backtests enfrentam o problema de amostras finitas, onde métricas como retornos médios ou drawdowns podem ser influenciadas por sorte. Para lidar com isso, utiliza-se o teste de hipótese, uma metodologia estatística que avalia a significância dos resultados obtidos.

                ##### Passos do Teste de Hipótese
                1. **Cálculo do Teste Estatístico**: Usamos métricas como o retorno médio diário como o teste estatístico do backtest.
                2. **Hipótese Nula**: Supomos que o retorno médio verdadeiro seja zero para a população infinita de dados.
                3. **Distribuição de Probabilidade**: Determinamos a distribuição dos retornos sob a hipótese nula, frequentemente assumindo uma distribuição normal.
                4. **Cálculo do p-valor**: Avaliamos a probabilidade de obter resultados tão extremos quanto os observados no backtest, dada a hipótese nula. Se o p-valor for pequeno (ex.: < 0,01), rejeitamos a hipótese nula, indicando que os resultados são estatisticamente significativos.


                """)
            
            col1, col2 = st.columns(2)
            # Exibir a imagem do primeiro gráfico
            with col1:
                st.image("img/h_test.png", caption='Link: https://miro.medium.com/v2/resize:fit:640/format:webp/1*gSP6jAp8BNOWW7B_lVNnZw.png', use_column_width=True)

            # Exibir a imagem do segundo gráfico
            with col2:
                st.image("img/h_test2.jpg", caption='Link: Este é o gráfico da distribuição dos valores. Link: https://miro.medium.com/v2/resize:fit:1400/format:webp/1*iaCsRW3_kDr6nEX1MrRIRQ.png', use_column_width=True) 

            st.markdown("""                
                ##### Métodos para Estimar a Distribuição Nula
                1. **Método Paramétrico**: Assume-se uma distribuição normal para os retornos, com média zero e desvio padrão baseado nos dados amostrais. O índice Sharpe, ajustado pela raiz quadrada do número de dias, é usado para determinar significância com base em valores críticos.
                2. **Método Monte Carlo**: Gera séries de preços simuladas com as mesmas características estatísticas da série real. A estratégia é aplicada a essas séries simuladas, avaliando a frequência em que o retorno médio supera o retorno do backtest.
                3. **Método de Simulação de Trades**: Cria conjuntos simulados de negociações com o mesmo número e período médio de manutenção que no backtest, mas distribuídos aleatoriamente nos preços reais. Avalia a proporção de retornos que excedem o resultado do backtest.
                        """)    


            code = '''
ticker = 'TU'
start_date = '2004-01-01'
end_date = '2020-01-01'


# 1. Obter os dados do Yahoo Finance
data = yf.download(ticker, start=start_date, end=end_date)
data['returns'] = data['Close'].pct_change()
data.dropna(inplace=True)

# 2. Calcular o retorno de 12 meses
lookback = 252  # ~12 meses de dias úteis
holddays = 20   # 1 mês (~20 dias úteis)
data['12m_returns'] = data['Close'].pct_change(periods=lookback)
data.dropna(inplace=True)

# 3. Criar sinais de compra e venda
data['longs'] = data['12m_returns'] > 0
data['shorts'] = data['12m_returns'] < 0

# 4. Calcular os retornos da estratégia
positions = np.zeros(len(data))
for h in range(holddays):
    long_lag = data['longs'].shift(h).fillna(False).astype(bool)
    short_lag = data['shorts'].shift(h).fillna(False).astype(bool)
    positions[long_lag] += 1
    positions[short_lag] -= 1
data['strategy_returns'] = positions * data['returns'] / holddays

# Teste de hipótese 1: Hipótese Nula Gaussiana
test_stat = data['strategy_returns'].mean() / data['strategy_returns'].std() * np.sqrt(len(data))
p_value_test1 = 1 - norm.cdf(test_stat)
print("\n=========================\n")
print("Teste 1: Estatística do Teste =", test_stat, ", P-Valor =", p_value_test1)

====================== Output ============================
Teste 1: 
Estatística do Teste = 1.788782524762457
P-Valor = 0.03682492317744812
            '''
            st.code(code, language="python")

            colab_link = "https://colab.research.google.com/drive/1Ev3dz4ZXJJcA1-xQ0T6nQq4E-X59T-Ax?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")


            st.markdown("""                
                ##### Limitações do Teste de Hipótese
                O teste de hipótese apresenta limitações, como:
                - **Dependência da Hipótese Nula**: Resultados variam dependendo da definição da hipótese nula, tornando os testes sensíveis às escolhas iniciais.
                - **Probabilidade Condicional**: Os testes avaliam a probabilidade do resultado dado que a hipótese nula é verdadeira, mas não o inverso (probabilidade da hipótese nula ser verdadeira dado o resultado).

                Mesmo com limitações, a falha em rejeitar a hipótese nula pode gerar insights valiosos. Por exemplo, distribuições com alta curtose podem ser favoráveis a estratégias de momentum, indicando padrões ocultos no mercado.""") 



        elif subsecao == "Quando não fazer Backtest em uma estratégia":

            st.markdown(r"""
            ### Quando não fazer Backtest em uma estratégia

            Embora o backtesting seja essencial para avaliar estratégias de trading, nem todas as estratégias merecem ser testadas. Algumas possuem falhas tão óbvias que investir tempo nelas é inútil. A seguir, são apresentados exemplos de estratégias que não devem ser testadas:

            ##### Exemplo 1: Alta Retorno, Baixo Sharpe Ratio  
            Uma estratégia com retorno anualizado de 30%, Sharpe ratio de 0.3 e duração máxima de drawdown de dois anos.  
            - **Problemas**: A baixa consistência (Sharpe ratio baixo) e o longo período de drawdown tornam a estratégia insustentável para a maioria dos traders.  
            - **Conclusão**: Provavelmente é um caso de viés de data-snooping, com pouca chance de sucesso em validação cruzada. Estratégias com altos retornos, mas baixo Sharpe ratio, geralmente não valem o teste.

            ##### Exemplo 2: Estratégia Long-only em Petróleo  
            Uma estratégia que gerou 20% de retorno em 2007, com Sharpe ratio de 1.5.  
            - **Problemas**: O retorno do buy-and-hold no petróleo bruto foi de 47% no mesmo ano, com Sharpe ratio de 1.7.  
            - **Conclusão**: A estratégia não é superior ao benchmark apropriado (buy-and-hold). Sempre compare estratégias com benchmarks relevantes.

            ##### Exemplo 3: "Buy-Low-Sell-High"  
            Escolhe as 10 ações mais baratas no início do ano e as mantém por 12 meses, gerando 388% de retorno no final do periodo.  
            - **Problemas**: Estratégias como essa frequentemente utilizam bancos de dados com viés de sobrevivência, ignorando ações deslistadas. Isso infla os retornos, tornando-os irreais.  
            - **Conclusão**: Se os dados não incluem ações deslistadas, o resultado é suspeito e irrealizável.

            ##### Exemplo 4: Modelo de Redes Neurais com 100 Nós  
            Um modelo de redes neurais com 100 nós gera Sharpe ratio de 6 no backtest.  
            - **Problemas**: Redes neurais com muitos nós têm centenas de parâmetros ajustáveis, permitindo ajustes perfeitos em séries históricas, mas com pouco ou nenhum poder preditivo devido ao viés de data-snooping.  
            - **Conclusão**: Estratégias com modelos excessivamente complexos não devem ser levadas a sério sem justificativas sólidas.

            ##### Exemplo 5: Estratégia de Alta Frequência no E-mini S&P 500  
            Uma estratégia de alta frequência com retorno médio anual de 200%, Sharpe ratio de 6 e período médio de manutenção de 50 segundos.  
            - **Problemas**: A lucratividade depende da estrutura do mercado, do tipo de ordem e da reação de outros participantes, fatores que o backtest não consegue replicar adequadamente.  
            - **Conclusão**: Backtests de estratégias de alta frequência frequentemente falham em capturar a dinâmica do mercado real e devem ser tratados com ceticismo.

            #### Conclusão  
            Nem toda estratégia vale o esforço do backtesting. Reconhecer falhas óbvias economiza tempo e evita falsas expectativas. Use benchmarks adequados, evite viés de sobrevivência, e desconfie de estratégias com complexidade excessiva ou resultados surpreendentes sem justificativa sólida.
            """)

        elif subsecao == "Um Backtest Será Preditivo de Retornos Futuros?":

            st.markdown(r"""
            ### **Um Backtest Será Preditivo de Retornos Futuros?**

            Mesmo evitando erros comuns no backtesting e garantindo significância estatística, a capacidade de prever retornos futuros depende de uma suposição central: que as propriedades estatísticas da série de preços permanecerão inalteradas. Na prática, essa suposição frequentemente é violada devido a mudanças econômicas, gerenciais ou estruturais nos mercados financeiros.  

            ##### Exemplos de Mudanças de Regime nos EUA
            1. **Decimalização (2001)**: A mudança para cotações decimais em ações dos EUA reduziu os spreads bid-ask, mas também diminuiu a liquidez exibida nos melhores preços. Isso reduziu a lucratividade de estratégias de arbitragem estatística, enquanto aumentou a de estratégias de alta frequência.
            
            2. **Crise Financeira de 2008**: 
            - Colapso de 50% nos volumes diários de negociação, afetando especialmente o varejo.
            - Redução na volatilidade média dos mercados, mas aumento na frequência de eventos extremos, como o flash crash (2010) e o rebaixamento da dívida dos EUA (2011). Esses fatores prejudicaram estratégias de reversão à média.
            - Início de um mercado de baixa para estratégias de momentum, que se estendeu por vários anos.

            3. **Regulação NMS (2007)**: Implementada pela SEC, contribuiu para a drástica redução nos tamanhos médios de negociações e a obsolescência de operações de blocos na NYSE.

            4. **Mudanças na Regra de Uptick para Vendas a Descoberto**: A remoção da antiga regra de uptick (2007) e sua substituição pela Alternative Uptick Rule (2010) afetaram estratégias que dependiam dessas regulamentações.

            ##### Impacto das Mudanças
            Estratégias que foram altamente lucrativas antes dessas mudanças podem tornar-se obsoletas ou menos eficazes. Backtests com dados anteriores a essas mudanças ("shifts de regime") podem não refletir condições futuras. Mesmo dados recentes podem ser enganosos se novas mudanças ocorrerem.

            #### Conclusão
            O trading algorítmico vai além de algoritmos, programação e matemática. É essencial considerar fatores econômicos e estruturais para avaliar se um backtest é preditivo e se sua eficácia pode ser mantida em condições futuras. Consciência dessas questões ajuda a mitigar o risco de confiar excessivamente em modelos baseados em dados históricos que podem não se repetir.
            """)

        elif subsecao == "Conclusão":

            st.markdown("""
#### **Importância do Backtest**
- O backtesting é inútil se não for **predicitivo** do desempenho futuro de uma estratégia.
- Evitar armadilhas no backtesting aumenta a **precisão e confiabilidade** dos resultados.

#### **Eliminando Pitfalls no Backtest**
- **Evitar Look-Ahead Bias:** Usar a **mesma plataforma** para backtest e execução ao vivo.
- **Reduzir Data-Snooping Bias:**
  - Teste fora da amostra (**out-of-sample**).
  - Validação cruzada (**cross-validation**).
  - Testes walk-forward (**walk-forward testing**).
  - Modelos **simples** reduzem o risco de sobreajuste.

#### **Perguntas Críticas para um Backtest Robusto**
- **Ajustes de preços históricos:**  
  - O modelo considera **splits** e **dividendos** corretamente?  
- **Viés de sobrevivência:**  
  - A estratégia inclui apenas **ações que ainda existem**?  
- **Uso de dados corretos:**  
  - Os dados de fechamento vêm da **bolsa primária**?  
- **Regulações históricas:**  
  - Em 2008, houve **proibição de short selling** em bancos. O modelo considerou isso?  
- **Execução realista:**  
  - A estratégia high-frequency considera **regras de uptick** para shorts?  
- **Construção correta de spreads:**  
  - Para futuros, o backtest ajusta os preços corretamente **(diferença de preços vs. retorno)**?  
- **Granularidade dos dados:**  
  - Para estratégias intradiárias, o modelo usa **dados de tick** em vez de agregações em barras?  
- **Testes em diferentes períodos:**  
  - Estratégias que funcionaram **antes de 2008** podem não funcionar **depois de 2008**.

#### **Significância Estatística no Backtest**
- **Teste com simulações:**  
  - Se uma estratégia tem **APR esperado de 10%**, validamos isso rodando **10.000 simulações** com os mesmos parâmetros estatísticos do preço original.
  - Se **apenas 100 dessas simulações** atingirem APR **≥ 10%**, então a estratégia tem **significância estatística de 1%**.
- **Teste com permutação aleatória:**  
  - Se randomizarmos **as datas das entradas das operações**, e apenas **1 em 100 permutações** atingir **APR ≥ 10%**, a estratégia tem **significância estatística de 1%**.

#### **Conclusão**
- Um backtest confiável requer **testes rigorosos**, ajuste de **dados históricos**, consideração de **regulações do mercado**, e avaliação da **significância estatística** dos resultados.
""")

#  ====================  Chapter 1  Backtesting e Execução Automática ===============

# ====================================================================================

# ====================== Chapter 2 The Basics of Mean Reversion ===============

    elif pagina == "3 . Os Fundamentos da Reversão à Média":
        st.title("3 . Os Fundamentos da Reversão à Média")


# ==================== Introdução ========================

        if subsecao == "Introdução":
            st.markdown("""
                        
            A reversão à média é um conceito que se manifesta tanto na natureza quanto nas ciências sociais. Esse fenômeno descreve como resultados extremos tendem, naturalmente, a retornar para um valor médio em medições subsequentes. Um exemplo claro pode ser observado no desempenho acadêmico: um aluno que obtém uma nota excepcionalmente alta em uma prova pode, na avaliação seguinte, apresentar um desempenho mais próximo da sua média habitual. Isso não significa que o aluno perdeu capacidade ou se tornou menos talentoso; ao contrário, o resultado extraordinário provavelmente foi influenciado por uma combinação de esforço, condições favoráveis e, até certo ponto, sorte. Compreender a reversão à média nos ajuda a interpretar dados de forma mais realista e a evitar conclusões precipitadas baseadas em eventos isolados.
                        
            ### A Reversão à Média nos Preços dos Ativos Financeiros

            Será que a reversão à média também acontece nas séries de preços de ativos financeiros? Se fosse tão comum, a vida dos traders seria muito mais fácil e lucrativa. Bastaria comprar um ativo quando seu preço estivesse abaixo da média, esperar a reversão para a média e, em seguida, vender a um preço mais alto, repetindo o processo continuamente. No entanto, a maioria das séries de preços não é reversora à média. Em vez disso, seguem o que chamamos de passeio aleatório . Enquanto os retornos (e não os preços) tendem a se distribuir ao redor de uma média próxima de zero, não podemos lucrar diretamente com a reversão à média dos retornos.

            É importante não confundir a reversão à média dos retornos com a anticorrelação serial dos retornos, que é negociável. A anticorrelação serial dos retornos é equivalente à reversão à média dos preços, e esse tipo de comportamento dos preços pode, sim, ser explorado.
                        
            ### Testes de Estacionariedade

            Algumas séries de preços que exibem reversão à média são chamadas de séries estacionárias.  Discutiremos os testes estatísticos usados para identificar a estacionariedade de uma série de preços, como o teste ADF, o expoente de Hurst e o teste de razão de variâncias. No entanto, não existem muitos ativos negociados publicamente que possuam séries de preços naturalmente estacionárias.

            Felizmente, podemos criar mais séries de preços estacionárias combinando dois ou mais ativos que, individualmente, não são reversores à média, mas que juntos podem formar um portfólio cujo valor de mercado total seja estacionário. Essas séries de preços são chamadas de cointegradas, e descreveremos os testes estatísticos usados para verificar a cointegração, como o teste CADF e o teste de Johansen. Como resultado desses testes, também podemos determinar as ponderações exatas de cada ativo para criar um portfólio com reversão à média. Isso abre várias oportunidades para traders que buscam lucrar com a reversão à média.
            
            """)

# ==================== Introdução ========================


# ==================== Mean Reversion ========================

        if subsecao == "1. Mean Reversion and Stationarity":
# ----------------------------------------------  

            latext = r'''
            A reversão à média e a estacionariedade são duas maneiras complementares de analisar o mesmo tipo de série de preços, cada uma com seus respectivos testes estatísticos.

            A descrição matemática de uma série de preços que reverte à média é que a mudança no próximo período é proporcional à diferença entre o preço atual e a média histórica. Isso leva ao teste ADF (Augmented Dickey-Fuller), que testa se podemos rejeitar a hipótese nula de que essa constante de proporcionalidade é zero (ou seja, não há reversão à média).

            Já uma série de preços estacionária é descrita matematicamente como uma série em que a variância dos logs dos preços aumenta mais lentamente do que em um caminho aleatório geométrico (onde a variância aumenta linearmente ao longo do tempo). Essa variação sublinear é geralmente aproximada por uma função do tempo, como $\tau^{2H}$, onde $\tau$ é o intervalo de tempo entre duas medições de preços e $H$ é o expoente de Hurst. Se $H$ for menor que 0,5, a série é estacionária; se for igual a 0,5, a série é um caminho aleatório. O teste de razão de variâncias é utilizado para verificar se podemos rejeitar a hipótese nula de que o expoente de Hurst é 0,5.

            Vale destacar que a estacionariedade não significa que os preços são necessariamente limitados dentro de um intervalo fixo, com variância independente do tempo (que resultaria em um expoente de Hurst igual a zero). Significa apenas que a variância aumenta de forma mais lenta que a difusão normal.

            Esses testes são essenciais para identificar oportunidades de negociação com base na reversão à média, ajudando a distinguir se uma série de preços apresenta características que possam ser exploradas em estratégias de trading quantitativo.
            '''
            st.write(latext)

            st.divider()
            latext = r'''
            ### Augmented Dickey-Fuller Test (ADF)

            A série de preços que apresenta reversão à média fornece informações sobre o movimento futuro dos preços com base no nível atual. Se o preço estiver acima da média, é esperado que haja um movimento de queda; se estiver abaixo da média, um movimento de alta. O teste ADF (Augmented Dickey-Fuller) se baseia nessa premissa para determinar se uma série de preços é ou não um passeio aleatório.

            O modelo linear para as mudanças nos preços é descrito pela seguinte equação:
            $$
            \Delta y(t) = \lambda y(t-1) + \mu + \beta t + \alpha_1 \Delta y(t-1) + \dots + \alpha_k \Delta y(t-k) + \epsilon_t
            $$

            Onde:

            - $\Delta y(t) = y(t) - y(t-1)$, representando a variação do preço.
            - $\lambda$ é o coeficiente que indica se há dependência da variação de preço atual com o nível anterior.
            - O teste ADF avalia se $\lambda = 0$, ou seja, se o próximo movimento $\Delta y(t)$ é independente do nível atual $y(t-1)$, indicando um caminho aleatório.

            O valor do teste estatístico é dado pela razão:
            $$
            \frac{\lambda}{SE(\lambda)}
            $$
            onde $SE(\lambda)$ é o erro padrão do ajuste de regressão. Se essa razão for significativamente negativa, o teste rejeita a hipótese nula de $\lambda = 0$, indicando que a série de preços não segue um caminho aleatório e que há reversão à média.

            A tabulação de valores críticos para esse teste foi feita por Dickey e Fuller, permitindo que os resultados sejam avaliados em níveis de confiança como 95%. Para que a hipótese nula seja rejeitada, o valor de $\frac{\lambda}{SE(\lambda)}$ deve ser negativo e mais negativo do que o valor crítico tabelado.

            **Exemplo 2.1**: Aplicação do teste ADF em uma série de taxas de câmbio, como o par USD/CAD, pode ajudar a determinar se a série de preços reverte à média ou se segue um caminho aleatório, oferecendo insights para estratégias de trading baseadas na reversão à média.
            '''
            st.write(latext)

            code = '''
            # Importando as bibliotecas necessárias
            import yfinance as yf
            import statsmodels.tsa.stattools as adf_test

            # Passo 1: Baixar dados do par de moedas USD/CAD usando o pacote yfinance.
            # Aqui, escolhemos o intervalo de datas entre 22 de junho de 2007 e 28 de março de 2014.
            df_usdcad = yf.download('USDCAD=X', start="2007-06-22", end="2014-03-28")

            # Passo 2: Aplicação do teste de Dickey-Fuller Aumentado (ADF) na série temporal
            # O teste ADF ajuda a verificar se uma série temporal é estacionária ou não.
            # 'Close' refere-se ao preço de fechamento do par de moedas em cada dia de negociação.
            result = adf_test.adfuller(df_usdcad['Close'])

            # Passo 3: Exibir os resultados do teste ADF
            # result[0] contém o valor da estatística do teste ADF.
            # result[1] contém o valor-p, que indica se a hipótese nula (não estacionariedade) é rejeitada ou não.
            # result[4] contém os valores críticos, usados para comparar a estatística do teste.

            print(f'Testatística ADF: {result[0]}')  # Exibe a estatística ADF calculada
            print(f'Valor-p: {result[1]}')  # Exibe o valor-p do teste
            print(f'Valores Críticos: {result[4]}')  # Exibe os valores críticos para diferentes níveis de confiança

            ====================== Output ============================
                Testatística ADF: -1.8310737300524096
                Valor-p: 0.3651471887306743
                Valores Críticos: {'1%': -3.434120287918905, '5%': -2.8632053717943005, '10%': -2.5676565959447415}

            '''
            st.code(code, language="python")

            colab_link = "https://colab.research.google.com/drive/1728THYP3eXkGqXEDo1OjXhPiMRY_erqt?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")

            col1, col2 = st.columns(2)
            # Exibir a imagem do primeiro gráfico
            with col1:
                st.image("img/usd_cad_serie.png", caption='Legenda: Este é o gráfico do par de moedas USD/CAD', use_column_width=True)
            # Exibir a imagem do segundo gráfico
            with col2:
                st.write("")

# ----------------------------------------------  

            st.divider()

            latext = r'''
            ### Hurst Exponent and Variance Ratio Test

            O exponente de Hurst e o Teste de Razão de Variância são ferramentas importantes para caracterizar o comportamento de séries temporais financeiras, especialmente em relação à sua tendência de reversão à média ou de passeio aleatório.

            ### Exponente de Hurst

            Intuitivamente, uma série de preços "estacionária" significa que os preços se difundem a partir de seu valor inicial de forma mais lenta do que em um passeio aleatório geométrico. Isso pode ser descrito pela equação de variância:

            $$
            \text{Var}(\tau) = \langle |z(t+\tau) - z(t)|^2 \rangle
            $$

            Onde $z$ são os logaritmos dos preços $y$, $\tau$ é o intervalo de tempo, e $\langle ... \rangle$ denota uma média sobre todos os $t$. Para um passeio aleatório geométrico, a relação é aproximadamente linear:

            $$
            \langle |z(t+\tau) - z(t)|^2 \rangle \sim \tau
            $$

            No entanto, para séries de preços que são revertidas à média ou têm tendência, essa relação muda para:

            $$
            \langle |z(t+\tau) - z(t)|^2 \rangle \sim \tau^{2H}
            $$

            Aqui, $H$ é o exponente de Hurst, onde:

            - $H = 0,5$ indica um passeio aleatório geométrico.
            - $H < 0,5$ indica uma série de preços revertendo à média.
            - $H > 0,5$ indica uma série de preços com tendência.

            Quanto mais próximo de 0 o valor de $H$, mais forte é a reversão à média. Um valor de $H$ mais próximo de 1 indica uma forte tendência. Semelhante ao **Exemplo 2.1**, ao calcular o exponente de Hurst para o par USD/CAD, o valor de $H = 0,46$ foi obtido, sugerindo uma fraca reversão à média.
            '''
            st.write(latext)

            code_2 = '''

            # Importação de bibliotecas necessárias
            import numpy as np  # Para operações matemáticas e manipulação de arrays
            import yfinance as yf  # Para download de dados financeiros

            # Função para calcular o coeficiente de Hurst
            def hurst_stat(ts, lags=100):

            # Define o intervalo de defasagens para calcular a variância
            rng = range(2, lags)
            
            # Converte a série temporal em logaritmo natural
            ts = np.log(ts)
            
            # Calcula a variância entre os valores com a defasagem especificada
            tau = [np.var(np.subtract(ts[lag:], ts[:-lag])) for lag in rng]
            
            # Ajusta uma linha reta (usando a regressão linear) na escala log-log
            poly = np.polyfit(np.log(rng), np.log(tau), 1)
            
            # Retorna o coeficiente de Hurst, que é o coeficiente angular da reta dividido por 2
            return poly[0] / 2

            # Download de dados históricos do par de moedas USD/CAD usando o Yahoo Finance
            df = yf.download('USDCAD=X', start="2007-06-22", end="2014-03-28")

            # Calcula o coeficiente de Hurst para o fechamento ajustado (Adj Close) da série temporal
            hurst = hurst_stat(df["Adj Close"].dropna().values)

            # Imprime o resultado do coeficiente de Hurst
            print(f"Hurst Coefficient: {hurst}")

            ====================== Output ============================

            Hurst Coefficient: 0.4627476687591544

            '''
            st.code(code_2, language="python")

            colab_link = "https://colab.research.google.com/drive/1728THYP3eXkGqXEDo1OjXhPiMRY_erqt?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")

# ----------------------------------------------  

            st.divider()
            st.write(r"""
            ### Teste de Razão de Variância

            Como o cálculo do exponente de Hurst pode ser sensível ao tamanho da amostra, o Teste de Razão de Variância fornece uma hipótese formal para verificar se a série segue um passeio aleatório. O teste compara a variância de diferentes intervalos de tempo para avaliar se a variância cresce de forma proporcional ao tempo, o que seria esperado em um passeio aleatório. A equação do teste é:

            $$
            \frac{\text{Var}(z(t) - z(t-\tau))}{\text{Var}(z(t-1) - z(t-\tau-1))} = 1
            $$

            Ao aplicar o teste à série USD/CAD, o valor de $p = 0,367$ foi obtido, indicando que há uma probabilidade de 37% de que a série seja um passeio aleatório. Como o valor de $p$ é maior que 10%, a hipótese nula (de que a série é um passeio aleatório) não pode ser rejeitada.

            Esses testes, portanto, fornecem informações importantes sobre a natureza da série de preços e se podem ser explorados para estratégias de negociação baseadas na reversão à média ou em tendências.
            """)


            code_3 = '''
            # Importação da função VarianceRatio da biblioteca arch para realizar o teste de razão de variância
            from arch.unitroot import VarianceRatio

            # Aplicação do teste de Razão de Variância sobre a coluna 'close' do dataframe df, com defasagem (lag) de 5 períodos
            vr = VarianceRatio(df['close'], 5)

            # Exibição do sumário dos resultados do teste em formato de texto
            print(vr.summary().as_text())
            '''
            st.code(code_3, language="python")

            colab_link = "https://colab.research.google.com/drive/1728THYP3eXkGqXEDo1OjXhPiMRY_erqt?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")
            
# ----------------------------------------------  
            
            st.divider()
            st.markdown(r"""
### Half-Life da Reversão à Média

Os testes estatísticos para reversão à média ou estacionaridade são rigorosos, exigindo uma certeza mínima de 90%. No entanto, em trading prático, muitas vezes podemos ser rentáveis com um grau de certeza menor. Nesta seção, vamos explorar uma interpretação alternativa do coeficiente $\lambda$ na 
$$
\Delta y(t) = \lambda y(t - 1) + \mu + \beta t + \alpha_1\Delta y(t - 1) + \dots + \alpha_k\Delta y(t - k) + \epsilon_t,
$$
o que nos ajuda a entender se seu valor negativo é suficiente para tornar uma estratégia de trading prática, mesmo sem rejeitar a hipótese nula de que seu valor real é zero com 90% de certeza no teste ADF.

Esse coeficiente, $\lambda$, é uma medida do tempo que um preço leva para reverter à média. Para entender essa nova interpretação, podemos transformar a série temporal discreta da 
$$
\Delta y(t) = \lambda y(t - 1) + \mu + \beta t + \alpha_1\Delta y(t - 1) + \dots + \alpha_k\Delta y(t - k) + \epsilon_t,
$$
para uma forma diferencial, onde as variações nos preços são consideradas infinitesimais. Se ignorarmos o drift ($\beta t$) e as diferenças defasadas ($\Delta y(t - 1), \dots, \Delta y(t - k)$) na equação acima, ela se assemelha à fórmula de Ornstein-Uhlenbeck, usada em cálculos estocásticos para descrever processos reversores à média:

$$
dy(t) = (\lambda y(t - 1) + \mu) \, dt + d\epsilon,
$$

onde $d\epsilon$ representa algum ruído Gaussiano. Na forma discreta, obtemos $\lambda$ por meio de uma regressão linear de $\Delta y(t)$ contra $y(t - 1)$. Esse valor de $\lambda$ é mantido na forma diferencial, mas a vantagem de expressá-lo assim é que obtemos uma solução analítica para o valor esperado de $y(t)$:

$$
E(y(t)) = y_0 e^{\lambda t} - \frac{\mu}{\lambda}\left(1 - e^{\lambda t}\right).
$$

Sabendo que $\lambda$ é negativo em um processo reversor à média, essa expressão indica que o valor esperado do preço decai exponencialmente para $-\frac{\mu}{\lambda}$ com uma meia-vida igual a $-\frac{\ln(2)}{\lambda}$.

#### Interpretações Úteis do Coeficiente $\lambda$ para Traders

1. **Sinal de $\lambda$**: Se $\lambda$ for positivo, isso significa que a série de preços não é reversora à média, logo, uma estratégia baseada em reversão à média não seria adequada.
2. **Magnitude de $\lambda$**: Se $\lambda$ for muito próximo de zero, a meia-vida será longa, o que torna uma estratégia de reversão à média menos lucrativa, já que não conseguiremos realizar muitas operações completas em um período de tempo razoável.
3. **Escala Temporal Natural**: $\lambda$ também define uma escala de tempo natural para vários parâmetros da estratégia. Por exemplo, se a meia-vida é de 20 dias, não deveríamos usar uma janela de 5 dias para calcular uma média móvel ou desvio padrão em uma estratégia de reversão à média. Definir a janela como um múltiplo pequeno da meia-vida tende a ser ideal e evita a otimização exaustiva de um parâmetro baseado no desempenho da estratégia.
""", unsafe_allow_html=False)

            colab_link = "https://colab.research.google.com/drive/1728THYP3eXkGqXEDo1OjXhPiMRY_erqt?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")

# ----------------------------------------------  
            
            st.divider()
            st.markdown(r"""
    ### Estratégia de Trading Linear com Reversão à Média

    Depois de confirmar que uma série de preços é reversora à média e que sua meia-vida de reversão é curta o suficiente para o nosso horizonte de trading, podemos lucrar com uma estratégia linear simples. Para isso, basta calcular o desvio normalizado do preço em relação à sua média móvel (desvio padrão móvel dividido pelo desvio padrão móvel do preço). A quantidade de unidades desse ativo mantidas na carteira deve ser proporcionalmente negativa em relação a esse desvio normalizado. A janela para a média móvel e o desvio padrão pode ser ajustada para igualar a meia-vida da reversão.

    #### Por Que Usar Média Móvel e Desvio Padrão?

    Você pode se perguntar por que usar uma média móvel ou um desvio padrão móvel em uma estratégia de reversão à média. Se uma série de preços é estacionária, seus parâmetros de média e desvio padrão não deveriam ser fixos? Embora, em teoria, a média de uma série de preços estacionária seja fixa, na prática, ela pode mudar lentamente devido a fatores econômicos ou mudanças na gestão corporativa. Já para o desvio padrão, até mesmo uma série estacionária com (0 < H < 0.5) apresenta uma variância crescente com o tempo, ainda que mais lentamente do que em um passeio aleatório geométrico. Assim, ao usar médias e desvios móveis, ajustamos a estratégia a uma média e desvio padrão que evoluem gradativamente, permitindo capturar lucros de maneira mais ágil.

    #### Importância dos Testes de Estacionaridade e Cálculo da Meia-Vida

    Um objetivo crucial dos traders é determinar se o retorno esperado ou o índice de Sharpe de uma estratégia de reversão à média é satisfatório. Então, por que nos preocuparmos com testes de estacionaridade (como o ADF ou o Teste de Razão de Variância) e o cálculo da meia-vida em vez de rodar um backtest diretamente? Esses testes preliminares têm uma significância estatística geralmente mais alta do que um backtest direto, pois utilizam os dados de preço de todos os dias (ou barras) disponíveis, enquanto um backtest gera um número menor de trades completos para análise de desempenho.

    Além disso, o resultado de um backtest depende dos parâmetros específicos da estratégia. Entretanto, se a série de preços passar nos testes estatísticos de estacionaridade, ou pelo menos apresentar uma meia-vida curta, podemos ter confiança de que conseguiremos encontrar uma estratégia de trading lucrativa, mesmo que não seja exatamente a estratégia backtestada inicialmente.

    Em capítulos seguintes, exploraremos mais essa ideia de adaptar a estratégia a uma média e desvio padrão móveis, principalmente no contexto de “scaling-in” (estratégia de incremento de posição).
    """)

            code_3 = '''
            import numpy as np
            import pandas as pd
            import matplotlib.pyplot as plt
            from tabulate import tabulate
            import yfinance as yf

            def rolling_z(series, window):
                """Calcula o Z-score móvel de uma série com uma janela especificada."""
                mean = series.rolling(window=window).mean()
                std = series.rolling(window=window).std()
                return (series - mean) / std

            def linear_mean_reversion_strategy(df, window):
                """
                Implementa uma estratégia simples de reversão à média.

                Parâmetros:
                - df (pd.DataFrame): DataFrame contendo uma coluna 'Close' com os preços do ativo.
                - window (int): Janela de tempo para o cálculo do Z-score.
                """
                
                # Calcula a quantidade de ativos a serem mantidos, baseado no Z-score inverso
                df["Quantity"] = -rolling_z(df["Close"], window)
                
                # Calcula o retorno diário, deslocando para obter o retorno no dia seguinte
                df["Return"] = df["Close"].pct_change().shift(-1)
                
                # Remove linhas com valores nulos e a última linha (que não terá retorno futuro)
                df = df.dropna(how="any")[:-1]
                
                # Calcula o lucro e perda (PnL) diário da estratégia multiplicando a quantidade pela variação do ativo
                df["PnL"] = df["Return"] * df["Quantity"]
                    
                # Plota o retorno cumulativo do instrumento e o PnL cumulativo da estratégia
                plt.plot(np.cumsum(df["Return"]), label="Cumulative Return of Stock")
                plt.plot(np.cumsum(df["PnL"]), label="Cumulative PnL of Strategy")
                
                # Adiciona uma legenda para identificação das linhas no gráfico
                plt.legend()
                
                # Exibe o gráfico
                plt.show()

            # Coleta de dados do Yahoo Finance
            ticker = "AAPL"  # Símbolo do ativo (por exemplo, "AAPL" para Apple)
            start_date = "2022-01-01"
            end_date = "2023-01-01"

            # Obtém os dados de preço de fechamento ajustado
            df = yf.download(ticker, start=start_date, end=end_date)[["Close"]]

            # Define o tamanho da janela para o Z-score
            window = 20

            # Aplica a estratégia
            linear_mean_reversion_strategy(df, window)

            '''
            st.code(code_3, language="python")

            colab_link = "https://colab.research.google.com/drive/1728THYP3eXkGqXEDo1OjXhPiMRY_erqt?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")

            col1, col2 = st.columns(2)
            # Exibir a imagem do primeiro gráfico
            with col1:
                st.image("img/simple_meanrev_strate.png", caption='Legenda: Estratégia e Trading Linear com Reversão à Média', use_column_width=True)
            # Exibir a imagem do segundo gráfico
            with col2:
                st.write("")

# ==================== Mean Reversion ========================


# ==================== Cointegração ========================

        elif subsecao == "2. Cointegração":
            
            st.markdown("""
                ### Cointegração

                Na introdução deste capítulo, mencionamos que a maioria das séries de preços financeiras não é estacionária ou reversora à média. No entanto, isso não nos limita a negociar essas séries financeiras “pré-fabricadas”. Podemos, de forma proativa, criar uma carteira de séries de preços individuais, de maneira que o valor de mercado (ou preço) dessa carteira seja estacionário. Esse é o conceito de **cointegração**: se conseguimos encontrar uma combinação linear estacionária de várias séries de preços não estacionárias, dizemos que essas séries de preços são cointegradas.

                ##### Estratégia de Pairs Trading (Operação de Pares)

                A combinação mais comum na cointegração envolve duas séries de preços: compramos (long) um ativo e simultaneamente vendemos (short) outro, com uma alocação apropriada de capital em cada ativo. Esse é o conceito de **pairs trading**, uma estratégia que se beneficia da relação entre duas séries de preços. Se as duas séries forem cointegradas, esperamos que qualquer desvio em relação à combinação estacionária entre elas eventualmente retorne à média, o que nos permite lucrar com esses movimentos de reversão.

                ##### Cointegração com Múltiplos Ativos

                Embora o pairs trading seja um exemplo prático de cointegração com apenas dois ativos, o conceito pode ser facilmente estendido para três ou mais ativos. Neste caso, criamos uma combinação linear de várias séries de preços, buscando que a soma ponderada dessas séries resulte em uma série estacionária.

                ##### Testes de Cointegração

                Para verificar se duas ou mais séries de preços são cointegradas, utilizamos testes específicos. Dois testes de cointegração amplamente aplicados são:

                1. **Teste CADF (Augmented Dickey-Fuller Cointegration Test)**: Esse teste é adequado para pares de séries de preços, verificando se uma combinação linear entre elas é estacionária.
                
                2. **Teste de Johansen**: Esse método é aplicável a um número maior de séries e permite identificar relações de cointegração em portfólios que contenham mais de dois ativos.

                Esses testes são fundamentais para traders que desejam criar estratégias baseadas em cointegração, pois permitem identificar ativos cujas relações mantêm uma combinação estacionária ao longo do tempo, possibilitando operações com uma perspectiva de retorno à média.

                **Em resumo**, a cointegração amplia o campo de oportunidades de negociação, permitindo a criação de portfólios estacionários a partir de séries de preços que, individualmente, são não estacionárias. Esta abordagem fornece uma base robusta para estratégias de reversão à média e é uma ferramenta essencial para estratégias de pares e portfólios multivariados.
            """)


            st.divider()
            st.markdown("""
                ### Teste Cointegrated Augmented Dickey-Fuller (CADF)

                O teste Cointegrated Augmented Dickey-Fuller (CADF) é utilizado para determinar se uma combinação linear de duas séries temporais não estacionárias pode formar um portfólio estacionário. Esse teste resolve a questão de identificar as proporções ideais (hedge ratios) para combinar os ativos de forma a criar um portfólio estacionário.

                ##### Por que precisamos do CADF?

                Embora já existam testes como o ADF e o Variance Ratio para verificar a estacionaridade de uma série, eles não são suficientes para lidar com múltiplos ativos. Isso ocorre porque:

                1. **Falta de Hedge Ratios Pré-Definidos**: Quando temos várias séries de preços, não sabemos de antemão os hedge ratios ideais para combiná-las em um portfólio estacionário.
                2. **Combinatórias Aleatórias Não Funcionam**: Nem toda combinação linear aleatória de ativos cointegrados resulta em um portfólio estacionário. 

                ##### Como o CADF Funciona?

                O teste CADF utiliza uma abordagem sistemática para determinar a cointegração:

                1. **Regressão Linear**: Primeiro, realiza-se uma regressão linear entre duas séries de preços para determinar os hedge ratios ideais.
                2. **Formação do Portfólio**: Em seguida, esses hedge ratios são aplicados para criar uma combinação linear das séries de preços.
                3. **Teste de Estacionaridade**: Finalmente, o teste ADF é aplicado à série de preços do portfólio para verificar se ela é estacionária.

                Essa metodologia foi originalmente proposta por Engle e Granger (1987).

                ##### Exemplo de Aplicação

                Considere dois ETFs, **EWA** e **EWC**. O CADF pode ser usado para:

                1. Determinar a proporção ideal de capital para estar comprado (ou vendido) em cada ETF.
                2. Formar um portfólio estacionário com base nesses hedge ratios.
                3. Validar a estacionaridade do portfólio resultante, indicando a viabilidade de estratégias de reversão à média baseadas nesses ETFs.

                Com o CADF, os traders podem identificar combinações de ativos que potencialmente oferecem oportunidades de lucro consistentes por meio de estratégias de reversão à média.
            """)

            colab_link = "https://colab.research.google.com/drive/1zkR1PxN3eLnRESlV03_idqVBPYy3VM1C?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar um exemplo no Colab]({colab_link})")

            # Johansen Test
            st.divider()
            st.markdown("""
                ### Johansen Test for Cointegration

                O Johansen test é uma abordagem estatística usada para identificar relações de cointegração em séries temporais múltiplas. Diferentemente de testes como o CADF, que avaliam cointegração entre duas variáveis e são dependentes da ordem das séries, o Johansen test pode ser aplicado a mais de duas séries simultaneamente, determinando todas as combinações lineares possíveis que formam portfólios estacionários.

                ##### Fundamentos do Johansen Test
                1. **Generalização de Cointegração**: Amplia a análise para vetores de preços e matrizes de coeficientes. O número de relações de cointegração (r) é determinado pelo posto da matriz de coeficientes (Λ).
                2. **Estatísticas de Teste**:
                - **Trace Statistic**: Testa hipóteses nulas de r ≤ k, onde k varia de 0 a (n-1), sendo n o número de séries.
                - **Eigen Statistic**: Também avalia r ≤ k, mas com base na decomposição de autovalores de Λ.

                ##### Exemplo 1: EWA e EWC
                - **Resultado**: Ambos os testes rejeitam a hipótese r = 0 (sem cointegração) e r ≤ 1, confirmando duas relações de cointegração entre os ETFs EWA e EWC.  
                - **Significado**: Mesmo com apenas duas séries, é possível formar dois portfólios estacionários com diferentes hedge ratios. O Johansen test elimina a dependência da ordem das variáveis, fornecendo diretamente todos os portfólios possíveis.

                ##### Exemplo 2: EWA, EWC e IGE
                - **Adição de uma terceira série**: Incluindo o ETF IGE, que representa ações de recursos naturais, o teste foi estendido para três séries.  
                - **Resultado**: Foram identificadas três relações de cointegração com 95% de certeza, permitindo a formação de múltiplos portfólios estacionários. Os autovalores e autovetores encontrados determinam os hedge ratios para cada portfólio.

                O Johansen test é uma ferramenta poderosa para estratégias de cointegração, especialmente ao lidar com múltiplas séries temporais. Sua independência em relação à ordem das séries e capacidade de identificar todas as combinações cointegradas tornam-no superior a métodos univariados em análises mais complexas.
                """)

            code = '''
# Importações necessárias
import yfinance as yf
import pandas as pd
import numpy as np
from statsmodels.tsa.vector_ar.vecm import coint_johansen
from tabulate import tabulate

# Função para imprimir linha pontilhada (caso precise)
def print_dashed_line():
    print("-" * 50)

# Função para realizar o teste de cointegração de Johansen
def johansen_cointegration(df, ticker_one, ticker_two):
    """
    Realiza o teste de cointegração de Johansen entre duas séries temporais.

    Parâmetros:
    - df: DataFrame contendo as séries temporais.
    - ticker_one: Nome da primeira série (coluna do DataFrame).
    - ticker_two: Nome da segunda série (coluna do DataFrame).

    Retorno:
    - jres: Resultado do teste de cointegração de Johansen.
    """
    # Realizando o teste de cointegração de Johansen
    jres = coint_johansen(df[[ticker_one, ticker_two]], det_order=0, k_ar_diff=1)

    # Resumo dos resultados do teste Trace
    summary = []
    for i in range(jres.trace_stat.shape[0]):
        summary.append([
            f"r<={i}", jres.trace_stat[i], jres.trace_stat_crit_vals[i][0], jres.trace_stat_crit_vals[i][1],
            jres.trace_stat_crit_vals[i][2]])

    # Exibindo os resultados do teste Trace
    print("Johansen Cointegration Test (Trace Statistics)")
    print(tabulate(summary, headers=["NULL:", "Trace Statistics", "Crit 90%", "Crit 95%", "Crit 99%"]))
    print("\n")

    # Resumo dos resultados do teste Eigen
    summary = []
    for i in range(jres.max_eig_stat.shape[0]):
        summary.append([
            f"r<={i}", jres.max_eig_stat[i], jres.max_eig_stat_crit_vals[i][0], jres.max_eig_stat_crit_vals[i][1],
            jres.max_eig_stat_crit_vals[i][2]])

    # Exibindo os resultados do teste Eigen
    print("Johansen Cointegration Test (Eigen Statistics)")
    print(tabulate(summary, headers=["NULL:", "Eigen Statistics", "Crit 90%", "Crit 95%", "Crit 99%"]))

    # Exibindo os valores próprios e os vetores próprios
    print("Eigen values: " + " ".join(f"{i:0.6f}" for i in jres.eig))
    print("Eigen vectors: " + " ".join(f"{i}" for i in jres.evec))

    # Imprimindo linha pontilhada de separação
    print_dashed_line()

    # Retornando os resultados do teste
    return jres

# Função para obter dados históricos de ativos com o yfinance
def get_data(tickers, start_date, end_date):
    """
    Obtém dados históricos de ativos financeiros com yfinance.

    Parâmetros:
    - tickers: Lista de tickers dos ativos.
    - start_date: Data de início (formato 'YYYY-MM-DD').
    - end_date: Data de fim (formato 'YYYY-MM-DD').

    Retorno:
    - DataFrame com os dados históricos dos ativos.
    """
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    return data

# Testando a função com dados reais de ativos
if __name__ == "__main__":
    # Defina os tickers e o período
    tickers = ['EWC', 'EWA']  # Exemplo: AAPL e MSFT
    start_date = '2006-01-01'
    end_date = '2012-01-01'

    # Obtendo os dados históricos
    df = get_data(tickers, start_date, end_date)

    # Chamando a função de cointegração de Johansen
    johansen_cointegration(df, 'EWC', 'EWA')


====================== Output ============================
Johansen Cointegration Test (Trace Statistics)
NULL:      Trace Statistics    Crit 90%    Crit 95%    Crit 99%
-------  ------------------  ----------  ----------  ----------
r<=0               20.5197      13.4294     15.4943     19.9349
r<=1                4.30495      2.7055      3.8415      6.6349


Johansen Cointegration Test (Eigen Statistics)
NULL:      Eigen Statistics    Crit 90%    Crit 95%    Crit 99%
-------  ------------------  ----------  ----------  ----------
r<=0               16.2148      12.2971     14.2639     18.52
r<=1                4.30495      2.7055      3.8415      6.6349
Eigen values: 0.010688 0.002849
Eigen vectors: [1.03947063 0.13619127] [-1.53822008  0.2337235 ]
--------------------------------------------------
            '''
            st.code(code, language="python")

            colab_link = "https://colab.research.google.com/drive/1zkR1PxN3eLnRESlV03_idqVBPYy3VM1C?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")


            # Estratégia
            st.divider()
            st.markdown("""
                ### Linear Mean-Reverting Trading on a Portfolio

                No exemplo, o portfólio EWA-EWC-IGE, formado com o "melhor" autovetor do Johansen test, mostrou uma curta meia-vida, tornando-o adequado para estratégias de reversão à média. A estratégia testada consiste em acumular unidades do portfólio proporcionalmente ao Z-Score negativo do preço do portfólio. Aqui, o portfólio unitário é determinado pelos pesos do autovetor do Johansen test, funcionando de forma semelhante a um ETF ou fundo mútuo.

                ##### Características da Estratégia
                1. **Linearidade**: 
                - A quantidade investida é proporcional ao Z-Score do portfólio, mas não ao valor de mercado total do investimento.
                - Essa abordagem linear simplifica o modelo, removendo a necessidade de otimização de parâmetros e eliminando o viés de data-snooping.

                2. **Praticidade**:
                - Embora útil para backtesting, a estratégia não é diretamente prática. Entrar ou sair de infinitas posições conforme pequenos movimentos de preço não é viável, e o capital máximo necessário não pode ser previsto com precisão.

                3. **Significância Estatística**:
                - Como a estratégia realiza posições continuamente e não depende de regras de entrada e saída complexas, os resultados têm maior significância estatística, reduzindo o impacto de eventos aleatórios no desempenho.

                O backtesting dessa estratégia linear simples demonstra que lucros podem ser extraídos de séries de preços cointegradas sem viés de otimização, usando apenas propriedades intrínsecas da série, como a meia-vida. Embora não seja diretamente aplicável ao mercado real, o modelo oferece uma base para entender e avaliar estratégias de reversão à média.
                """)


            colab_link = "https://colab.research.google.com/drive/1zkR1PxN3eLnRESlV03_idqVBPYy3VM1C?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")

# ==================== Cointegração ========================

# ==================== Pros and Cons of Mean-Reverting Strategies ========================

        elif subsecao == "3. Prós e Contras da Reversão a média":
 
            st.markdown("""
                ### Prós e Contras das Estratégias de Reversão à Média

                As estratégias de reversão à média possuem características específicas que as tornam atraentes para traders, mas também apresentam alguns riscos e desafios. Abaixo, listamos os principais prós e contras dessas estratégias.

                #### Prós

                - **Facilidade de Construção**: É relativamente simples construir estratégias de reversão à média, pois não estamos limitados a instrumentos que sejam intrinsecamente estacionários. Podemos escolher e combinar uma variedade de ações e ETFs cointegrados para criar um portfólio estacionário.

                - **Abundância de Ativos**: Há uma grande variedade de ativos para selecionar, incluindo novos ETFs que surgem anualmente e que oferecem oportunidades de cointegração.

                - **Fundamento Econômico**: Muitas vezes, pares cointegrados possuem uma lógica econômica sólida. Por exemplo, EWA e EWC são ETFs que cointegram devido às economias de Canadá e Austrália serem orientadas por commodities. Esse fundamento sólido diferencia as estratégias de reversão à média das estratégias de momentum, que dependem de diferenças na velocidade de reação dos investidores às notícias.

                - **Variedade de Escalas de Tempo**: As estratégias de reversão à média podem ser aplicadas em diversas escalas de tempo. Estratégias de market-making operam com reversões em segundos, enquanto investidores de longo prazo esperam anos pela valorização de ações subvalorizadas. Em particular, estratégias de curto prazo são vantajosas para traders, pois o maior número de trades aumenta a confiança estatística e o Sharpe Ratio do backtest e das operações ao vivo.

                #### Contras

                - **Risco de Consistência Enganosa**: A aparente consistência nas estratégias de reversão à média pode levar à confiança excessiva e ao uso de alavancagem elevada. Quando a estratégia falha – muitas vezes por razões fundamentais que só ficam claras em retrospecto –, os traders geralmente estão altamente alavancados, o que torna as perdas raras, mas severas.

                - **Desafios na Gestão de Risco**: A gestão de risco é particularmente difícil para essas estratégias, pois o uso de stop losses convencionais não é sempre viável. Além disso, como as perdas são raras, elas podem ser imprevisivelmente grandes quando ocorrem. Em estratégias de reversão à média, é essencial desenvolver técnicas de controle de risco adaptadas, abordadas mais detalhadamente no Capítulo 8.

                Esses pontos ressaltam a importância de equilibrar as vantagens das estratégias de reversão à média com uma gestão de risco rigorosa, especialmente para evitar o impacto de eventos extremos e inesperados.
                """)
        
        elif subsecao == "4. Resumo":
            st.markdown("""
            ###  Conceitos fundamentais:

            - **Reversão à Média**: Refere-se ao fenômeno em que a mudança no preço é proporcional à diferença entre o preço médio e o preço atual. Em outras palavras, espera-se que o preço reverta em direção à média ao longo do tempo.

            - **Estacionaridade**: Uma série estacionária se difunde mais lentamente do que um passeio aleatório geométrico. Isso significa que, embora o preço possa variar, ele tende a se manter dentro de certos limites.

            - **Teste ADF**: O teste de Dickey-Fuller Aumentado (ADF) é utilizado para testar a hipótese de reversão à média em uma série temporal. Ele verifica se a série retorna consistentemente para uma média ao longo do tempo.

            - **Exponente de Hurst e Teste de Razão de Variância**: Esses métodos são empregados para testar a estacionaridade de uma série. Eles ajudam a identificar se a série tende a se difundir de maneira controlada, caracterizando-a como estacionária.

            - **Half-Life de Reversão à Média**: Mede a velocidade com que uma série de preços retorna à sua média. Esse indicador é útil para prever a lucratividade ou o Sharpe Ratio de uma estratégia de trading de reversão à média. Um half-life curto indica uma reversão rápida, ideal para estratégias de trading mais ativas.

            - **Estratégia de Trading Linear**: Em uma estratégia linear, o número de unidades ou ações que possuímos em um portfólio é proporcional ao Z-Score negativo da série de preços. Isso significa que, à medida que o preço se afasta da média, aumentamos ou reduzimos nossa posição de acordo.

            - **Cointegração**: Se combinarmos duas ou mais séries de preços não estacionárias e formarmos um portfólio estacionário, essas séries são consideradas cointegradas. A cointegração permite a criação de portfólios que mantêm uma relação estável, apesar das variações de cada ativo individualmente.

            - **Testes de Cointegração (CADF e Johansen)**: O teste CADF verifica a cointegração entre dois ativos, enquanto o teste de Johansen pode ser aplicado a um número maior de séries. Estes testes ajudam a identificar combinações estacionárias de séries não estacionárias.

            - **Autovalores e Autovetores no Teste de Johansen**: Os autovetores resultantes do teste de Johansen podem ser usados como proporções de hedge para criar um portfólio estacionário a partir das séries de preços analisadas. O autovetor associado ao maior autovalor é aquele com o half-life mais curto, indicando uma reversão mais rápida.

            Esses conceitos são fundamentais para desenvolver estratégias de reversão à média e cointegração, fornecendo uma base analítica para avaliar a viabilidade e lucratividade de operações nesses mercados.
""")

# ====================== Chapter 2 The Basics of Mean Reversion ============


# ====================================================================================


# ===================== Chapter 3 Implementing Mean Reversion Strategies =============

    elif pagina == "4 . Estratégias de Reversão à Média":
        st.title("4 . Estratégias de Reversão à Média")

        if subsecao == "Introdução":
            st.markdown("""
#### **Implementação de Estratégias de Reversão à Média**

As estratégias de reversão à média fundamentam-se na premissa de que os preços tendem, ao longo do tempo, a retornar a um valor médio. Embora testes estatísticos no capítulo anterior tenham sido usados para identificar séries estacionárias ou cointegradas, a aplicação prática dessas estratégias não depende exclusivamente da estacionariedade perfeita.

##### Considerações Fundamentais
1. **Estacionariedade e Cointegração**  
   - Ativos individuais raramente apresentam estacionariedade. No entanto, portfólios formados por ativos cointegrados (como pares long-short) podem ser explorados para capturar oportunidades de reversão à média.  
   - Além disso, a reversão pode ocorrer em horizontes temporais curtos ou sazonais, como durante condições específicas de um dia.  
   - *Exemplo*: Uma série com tempo de reversão muito longo (por exemplo, 10 anos) dificilmente será lucrativa para operações de curto prazo.

2. **Estratégias Lineares e seus Desafios**  
   - Uma abordagem simples pode ser a estratégia linear escalonada, que compra ou vende de forma proporcional ao desvio do preço em relação à média.  
   - Embora conceitualmente interessante, essa estratégia requer reequilíbrios constantes e pressupõe um poder de compra ilimitado, o que a torna inviável na prática.

##### Estratégias Práticas de Implementação
1. **Bandas de Bollinger**  
   - Uma técnica prática que utiliza limites superiores e inferiores, definidos a partir do desvio padrão, para indicar pontos de entrada e saída.  
   - Variantes dessa estratégia permitem múltiplos níveis de entrada e saída (o chamado "scaling-in"), ajustando a posição de forma gradual conforme o preço se afasta ou retorna à média.

2. **Filtro de Kalman**  
   - Ferramenta dinâmica utilizada para estimar, em tempo real, o hedge ratio e o preço médio, proporcionando uma modelagem adaptativa da reversão à média.

##### Cuidados Essenciais na Implementação
- **Erros de Dados**: Estratégias de reversão à média são altamente sensíveis a erros nos dados. Pequenas imprecisões podem gerar sinais falsos e resultar em perdas.
- **Custos de Transação**: Embora frequentemente ignorados em exemplos teóricos, os custos de transação são críticos na avaliação da viabilidade prática da estratégia.
- **Viés de Look-ahead**: É fundamental evitar o uso dos mesmos dados para otimização dos parâmetros (como o hedge ratio) e para backtesting, pois isso pode inflar os resultados e comprometer a eficácia preditiva do modelo.

Em resumo, a implementação de estratégias de reversão à média exige rigor na gestão dos dados, uma compreensão aprofundada dos custos envolvidos e atenção especial para evitar vieses que possam comprometer os resultados. Traders devem ajustar e testar cuidadosamente esses modelos para assegurar sua robustez e aplicabilidade em condições reais de mercado.
""")

        elif subsecao == "Trading Pairs":
        
            st.markdown("""
            ### **Trading Pairs: Uso de Spreads de Preços, Log Spreads ou Ratios**

            Estratégias de reversão à média podem ser implementadas utilizando diferentes formas de sinalização, tais como spreads de preços, logaritmos dos preços ou ratios. Cada método possui características específicas e pode ser mais adequado para diferentes cenários de mercado.

            ##### 1. Price Spreads
            - **Definição**: Consiste no cálculo do spread direto entre os preços de dois ativos.  
            - **Como Funciona**: Um portfólio é criado atribuindo pesos fixos (hedge ratios) aos ativos, geralmente determinados por métodos de regressão ou testes de cointegridade. A diferença resultante entre os preços é monitorada para identificar desvios da média.  
            - **Vantagens**:  
            Simplicidade de cálculo e implementação.  
            Boa aplicação quando os ativos possuem escalas de preços semelhantes.
            - **Limitações**:  
            Pode se tornar ineficaz se os ativos não estiverem adequadamente escalonados, pois diferenças absolutas podem distorcer o sinal.
            - **Exemplo Prático**:  
            Se dois ativos historicamente se movem de forma correlacionada, um desvio significativo no spread pode indicar uma oportunidade de compra no ativo subvalorizado e venda no ativo sobrevalorizado.

            ##### 2. Log Price Spreads
            - **Definição**: Em vez de trabalhar com preços absolutos, utiliza-se o logaritmo dos preços para formar o spread.  
            - **Como Funciona**: O uso de logaritmos tende a estabilizar a variância e criar um portfólio com pesos de capital constantes, o que pode refletir melhor a relação proporcional entre os ativos.
            - **Vantagens**:  
            Ajuda a mitigar o efeito de grandes variações absolutas e diferenças de escala entre os preços.  
            Mantém uma relação de capital mais estável ao longo do tempo.
            - **Limitações**:  
            Pode requerer reequilíbrios mais frequentes para garantir que as proporções de capital sejam mantidas, o que pode aumentar os custos operacionais.
            - **Exemplo Prático**:  
            Em mercados com alta volatilidade, usar logaritmos pode suavizar os movimentos bruscos e oferecer sinais mais confiáveis para a reversão à média.

            ##### 3. Ratios
            - **Definição**: Utiliza a razão entre os preços de dois ativos como sinal de negociação, sem a necessidade de calcular hedge ratios complexos.  
            - **Como Funciona**: A estratégia baseia-se na premissa de que, mesmo que os ativos não sejam cointegrados, a razão entre seus preços pode se comportar de forma reversível em curto prazo.
            - **Vantagens**:  
            Simplifica o modelo ao eliminar a necessidade de ajustar continuamente os hedge ratios.  
            Pode ser mais robusta quando os ativos apresentam diferenças significativas de escala.
            - **Limitações**:  
            Pode não capturar todas as nuances de mercados onde a relação entre os ativos é complexa e não linear.
            - **Exemplo Prático**:  
            Em pares de moedas, como EUR/GBP, a relação pode naturalmente funcionar como uma razão. Por outro lado, em pares onde há discrepâncias marcantes (por exemplo, MXN/NOK), utilizar ratios pode evitar a distorção causada pela diferença de escala.

            ##### Considerações Finais
            - **Contexto e Características dos Ativos**:  
            Cada abordagem deve ser escolhida com base no comportamento histórico e nas propriedades estatísticas dos ativos em questão.  
            - **Custo e Frequência de Reequilíbrio**:  
            Estratégias que exigem reequilíbrios frequentes, como os log price spreads, devem ser avaliadas quanto aos custos de transação e à liquidez dos ativos.  
            - **Robustez dos Sinais**:  
            É essencial testar cada método em diferentes cenários de mercado para verificar a robustez dos sinais gerados e evitar armadilhas, como ruídos excessivos ou sinais falsos.

            Em resumo, a escolha entre price spreads, log price spreads ou ratios dependerá do contexto específico do par de ativos e dos objetivos do trader. Um entendimento aprofundado das vantagens e limitações de cada abordagem possibilita a seleção da estratégia mais adequada para capturar oportunidades de reversão à média.
            """)

            colab_link = "https://colab.research.google.com/drive/1ihcWiNwspG_qrUiPeZSstOl3PE9yfPc_?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")

        elif subsecao == "Bollinger Bands":
            st.markdown("""
            ### Bollinger Bands 

            A estratégia de reversão à média mais simples descrita até agora é a linear, na qual o número de unidades investidas em um portfólio estacionário é proporcional ao desvio do preço em relação à média móvel. Embora útil para testar a viabilidade da reversão à média, essa abordagem não é prática, pois não define um limite para o capital investido, deixando a estratégia vulnerável a desvios prolongados.

            ##### Estratégia das Bandas de Bollinger
            Para contornar essa limitação, utilizamos **Bollinger Bands**, que estabelecem limites baseados no desvio-padrão da média móvel. A estratégia funciona da seguinte maneira:
            1. **Entrada**: Compra ou venda ocorre quando o preço se desvia **entryZscore** desvios-padrão acima ou abaixo da média móvel.
            2. **Saída**: A posição é encerrada quando o preço retorna a **exitZscore** desvios-padrão da média. Algumas abordagens comuns:
            - **exitZscore = 0**: Sai da posição quando o preço volta à média.
            - **exitZscore = -entryZscore**: Sai da posição apenas quando o preço atinge o extremo oposto da banda, invertendo a posição.

            ##### Parâmetros da Estratégia
            - **entryZscore** e **exitZscore** são parâmetros livres, ajustáveis com otimização em um conjunto de treinamento.
            - **Período de Look-back**: A média móvel e o desvio-padrão podem ser calculados com um período de look-back fixo ou ajustado com base na meia-vida da reversão à média.
            - **Gestão de Capital e Risco**: A estratégia opera com posições discretas (long ou short), facilitando a alocação de capital e o gerenciamento de risco.

            O uso de **Bollinger Bands** torna a estratégia de reversão à média mais prática e controlada, evitando exposição ilimitada a desvios prolongados. A escolha adequada dos parâmetros pode melhorar a robustez da estratégia e minimizar riscos associados a oscilações excessivas do mercado.
            """)

            colab_link = "https://colab.research.google.com/drive/1ihcWiNwspG_qrUiPeZSstOl3PE9yfPc_?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")

            st.divider()
                      
            st.image("img/bbands.png", caption="Bollinger Bands. Link: https://learn.swyftx.com/wp-content/uploads/2022/07/Fig-3-Riding-the-bands.png")
            
            st.divider()

            st.markdown("""
### **Scaling-in: Funciona Mesmo?**

A estratégia de **scaling-in** (ou averaging-in) envolve aumentar gradualmente a posição em uma estratégia de reversão à média à medida que o preço se afasta da média. Essa abordagem busca capturar ganhos parciais em cada pequena reversão, reduzindo o impacto de mercado para posições maiores e permitindo ganhos mesmo quando a série de preços não é perfeitamente estacionária. Uma implementação comum utiliza múltiplos níveis de entrada e saída com **Bollinger Bands**, definindo pontos de entrada (por exemplo, *entryZscore = 1, 2, 3...N*) e saída (por exemplo, *exitZscore = 0, 1, 2...N-1*). Contudo, pesquisas indicam que **scaling-in pode não ser a abordagem mais lucrativa**.

##### Comparação entre Estratégias "All-in" e "Scaling-in"
O estudo de **Schoenberg e Corwin (2010)** demonstra que entrar em múltiplos pontos nunca supera a estratégia de entrada única otimizada. Em um cenário onde o preço oscila entre:
- **L1** (nível inicial),
- **L2** (nível mais baixo antes da reversão) e
- **F** (preço final esperado),

são comparados três métodos:
1. **All-in at L1**: Compra total na primeira oportunidade em **L1**, independentemente de quedas subsequentes.
2. **All-in at L2**: Aguarda a queda para **L2** antes de investir toda a posição.
3. **Scaling-in**: Compra uma parte da posição em **L1** e o restante em **L2**, caso o preço continue a cair.

- Se a probabilidade de o preço atingir **L2** for baixa (**p < p̂**), a estratégia **All-in at L1** tende a ser mais lucrativa.
- Se essa probabilidade for alta (**p > p̂**), **All-in at L2** se mostra superior.
- Em nenhum cenário, segundo o estudo, o **scaling-in** supera as estratégias de entrada única.

##### Possíveis Cenários para o Uso de Scaling-in
Apesar das evidências contrárias nos backtests, alguns fatores do mercado real podem justificar o uso do scaling-in:
- **Volatilidade Variável**: O estudo pressupõe volatilidade constante, mas na prática a volatilidade varia ao longo do tempo, o que pode favorecer a entrada gradual.
- **Melhoria no Sharpe Ratio**: Mesmo com retornos absolutos ligeiramente menores, o scaling-in pode reduzir a volatilidade da estratégia, melhorando a relação risco-retorno.
- **Desempenho Fora da Amostra**: Embora o scaling-in possa parecer inferior nos dados históricos de treinamento, em mercados dinâmicos ele pode superar o método "all-in" sob determinadas condições.

Em resumo, apesar de parecer intuitivo e oferecer vantagens, como a redução do impacto de mercado, estudos sugerem que a estratégia **"all-in" em um único ponto de entrada otimizado** gera retornos superiores nos backtests. Contudo, fatores como variações na volatilidade e condições de mercado reais podem fazer com que o scaling-in se mostre vantajoso em determinados contextos. O ideal é testar e comparar ambas as abordagens antes de aplicá-las em trading ao vivo.
""")

        elif subsecao == "Kalman Filter":

            st.markdown("""
            Kalman Filter como Regressão Linear Dinâmica

            **Contexto e Problema**  
            - Para séries de preços cointegradas, o hedge ratio pode ser obtido facilmente com OLS ou o teste de Johansen.  
            - No entanto, séries reais raramente são perfeitamente estacionárias ou cointegradas.  
            - Métodos tradicionais que utilizam janelas móveis podem provocar mudanças abruptas e artificiais no hedge ratio.

            **A Solução: Kalman Filter**  
            - **Definição**: Um algoritmo linear ótimo que atualiza a estimativa de uma variável oculta (neste caso, o hedge ratio) com base no último valor de uma variável observável.  
            - **Premissas**:  
                - A relação entre a variável observável e a oculta é linear e sujeita a ruídos gaussianos.  
                - A variável oculta no tempo t é a mesma de t − 1 acrescida de um ruído, permitindo modelar sua evolução sem um corte arbitrário na ponderação dos dados.

            **Especificação do Modelo**  
            - **Variáveis e Matrizes**:  
                - **Variável Observável (y)**: Uma das séries de preço.  
                - **Variável Oculta (β)**: Representa o hedge ratio (incluindo intercepto e coeficiente angular).  
                - **Modelo de Transição de Estado**: β(t) = β(t − 1) + ω(t − 1), onde ω é ruído com covariância definida.  
                - **Equação de Medição**: y(t) = x(t)β(t) + ∊(t), onde x(t) (incluindo uma coluna de uns para o intercepto) atua como o modelo de observação e ∊(t) é ruído gaussiano.

            **Vantagens do Uso do Kalman Filter**  
            - **Atualização Dinâmica**: Gera um hedge ratio que se ajusta continuamente com a chegada de novos dados, evitando cortes arbitrários.  
            - **Estimativas Múltiplas**: Além do hedge ratio, o filtro produz estimativas da média (através do intercepto) e da volatilidade (desvio padrão do erro de previsão), substituindo os métodos de médias móveis e bandas de Bollinger.  
            - **Otimização**: Minimiza o erro quadrático médio das estimativas, sendo a melhor opção se os ruídos realmente seguirem uma distribuição gaussiana.

            - **Aplicação Prática**  
            - Após definir as variáveis observáveis, ocultas e os modelos (transição de estado e observação), o Kalman Filter é aplicado de forma iterativa para atualizar as estimativas em tempo real.  
            - Essa abordagem é implementada com pacotes de software que automatizam os cálculos, permitindo que traders se concentrem na análise e aplicação dos sinais.

            Em resumo, o Kalman Filter oferece uma abordagem robusta para estimar dinamicamente o hedge ratio e os parâmetros do spread, superando limitações dos métodos de janelas móveis e ponderações arbitrárias.
            """)
            
            colab_link = "https://colab.research.google.com/drive/1ihcWiNwspG_qrUiPeZSstOl3PE9yfPc_?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")

            st.divider()

            st.write(r"""
### Resumo: Equações Iterativas do Filtro de Kalman

O Filtro de Kalman é um algoritmo recursivo que atualiza de forma dinâmica a estimativa de uma variável oculta (neste caso, o vetor \(\beta\), que pode representar tanto o hedge ratio quanto o intercepto) com base em novas observações. Esse método é dividido em duas etapas principais: **previsão** e **atualização**.

#### 1. Etapa de Previsão

Nesta etapa, o filtro utiliza a estimativa atual para prever o estado e a incerteza (covariância) para o próximo instante, antes de receber a nova medição.

- **Previsão do Estado:**  
  $$\hat{\beta}(t|t-1) = \hat{\beta}(t-1|t-1)$$  
  A melhor estimativa do estado no tempo \(t\) é considerada igual à estimativa do tempo anterior. Essa equação reflete a hipótese de que, na ausência de novas informações, o estado se mantém constante.

- **Previsão da Covariância do Estado:**  
  $$R(t|t-1) = R(t-1|t-1) + V_w$$  
  A matriz \(R(t|t-1)\) representa a incerteza na previsão do estado. Ela é atualizada somando a incerteza do estado anterior com o ruído do modelo (\(V_w\)).

- **Previsão da Medição:**  
  $$\hat{y}(t) = x(t)\hat{\beta}(t|t-1)$$  
  Estima o valor observado com base na previsão do estado, onde \(x(t)\) atua como o modelo de observação.

- **Previsão da Variância da Medição:**  
  $$Q(t) = x(t)' R(t|t-1) x(t) + V_e$$  
  Esta equação calcula a variância esperada do erro da medição, combinando a incerteza do estado com o ruído de medição (\(V_e\)).

#### 2. Etapa de Atualização

Após receber a nova medição \(y(t)\), o filtro ajusta a estimativa do estado e a sua incerteza, combinando a previsão com a nova informação.

- **Erro de Previsão:**  
  $$e(t) = y(t) - x(t)\hat{\beta}(t|t-1)$$  
  Representa a diferença entre o valor observado e o valor previsto.

- **Ganho de Kalman:**  
  $$K(t) = \frac{R(t|t-1)x(t)}{Q(t)}$$  
  Determina o peso que a nova observação terá na atualização do estado, equilibrando a confiança na previsão e na medição.

- **Atualização do Estado:**  
  $$\hat{\beta}(t|t) = \hat{\beta}(t|t-1) + K(t)\cdot e(t)$$  
  A estimativa do estado é ajustada com base no erro de previsão, ponderado pelo ganho de Kalman.

- **Atualização da Covariância do Estado:**  
  $$R(t|t) = R(t|t-1) - K(t)\cdot x(t)\cdot R(t|t-1)$$  
  Após a atualização, a incerteza na estimativa é reduzida, refletindo a nova confiança após incorporar a medição.
                     
#### Considerações Adicionais

- **Inicialização:**  
  Normalmente, assume-se que $$\hat{\beta}(1|0) = 0$$ e $$R(0|0) = 0$$, indicando que inicialmente não há conhecimento sobre o estado.

- **Parâmetros de Ruído (\(V_w\) e \(V_e\)):**  
  - $$V_w = \delta \cdot I$$  
    onde \(\delta\) é um valor pequeno (por exemplo, \(0.0001\)), o que mantém a atualização estável, similar a uma regressão OLS com coeficientes fixos.  
  - $$V_e$$ define a incerteza na medição. Valores menores aumentam a confiança na observação, enquanto valores maiores indicam maior ruído.

Essas equações permitem que o Filtro de Kalman atualize continuamente a estimativa do hedge ratio e de outros parâmetros de forma dinâmica e otimizada, sendo uma ferramenta poderosa para modelagem e previsão em tempo real.

""")
   
            st.divider()

            st.write(r"""
### Resumo: Kalman Filter como Modelo de Market Making

Neste modelo, o Filtro de Kalman é aplicado a uma única série de preços com tendência de reversão à média, visando estimar dinamicamente o preço médio e a volatilidade da série. Diferentemente do caso de pares cointegrados (onde se estima o hedge ratio), aqui o preço médio \(m(t)\) é a variável oculta e o preço observado \(y(t)\) é a variável mensurada.

#### Modelagem e Equações

- **Equação de Medição:**  
  A medição relaciona o preço observado ao preço médio oculto:
  $$
  y(t) = m(t) + \epsilon(t)
  $$
  onde \(\epsilon(t)\) representa o ruído da medição.

- **Equação de Transição de Estado:**  
  O modelo assume que o preço médio evolui de forma simples:
  $$
  m(t) = m(t-1) + \omega(t-1)
  $$
  com \(\omega(t-1)\) representando o ruído do estado.

- **Atualização do Estado:**  
  Após observar \(y(t)\), a estimativa do preço médio é atualizada conforme:
  $$
  m(t|t) = m(t|t-1) + K(t) \Big( y(t) - m(t|t-1) \Big)
  $$
  onde \(K(t)\) é o ganho de Kalman.

- **Erro de Previsão e Variância:**  
  A variância do erro da previsão é dada por:
  $$
  Q(t) = \operatorname{Var}(m(t)) + V_e
  $$
  e o ganho de Kalman é definido como:
  $$
  K(t) = \frac{R(t|t-1)}{R(t|t-1) + V_e}
  $$
  A atualização da incerteza do estado é feita com:
  $$
  R(t|t) = \big( 1 - K(t) \big) R(t|t-1)
  $$

#### Considerações Práticas e Aplicações

- **Uso em Market Making:**  
  Esse modelo é popular entre market makers para atualizar suas estimativas do preço médio de um ativo em tempo real, permitindo que ajustem rapidamente seus preços de oferta e demanda.

- **Incorporação do Tamanho da Ordem:**  
  Para tornar o modelo mais realista, o erro de medição $V_e$ pode ser ajustado de acordo com o tamanho da ordem $T$. Se $T$ se aproxima de um tamanho de referência $T_{\text{max}}$, a incerteza diminui:
  $$
  V_e = R(t|t-1) \left(1 - \frac{T}{T_{\text{max}}}\right)
  $$
  Assim, quando  $T = T_{\text{max}}$, $V_e$ é zero, o ganho de Kalman é 1, e o novo preço médio passa a ser exatamente o preço observado. Essa abordagem é análoga a calcular um preço médio ponderado pelo volume e tempo (VWAP).

- **Ferramentas Disponíveis:**  
  Além da implementação manual, existem códigos em Python e pacotes open-source para facilitar o uso do Filtro de Kalman nesse contexto.

#### Observações Finais

O modelo de market making com Filtro de Kalman oferece uma forma robusta de estimar dinamicamente o preço médio e a volatilidade de um ativo, ajustando o peso dado às novas observações com base em seu tamanho e recência. Essa técnica permite aos market makers reagir de forma mais precisa às mudanças no mercado, integrando informações de volume e tempo para definir um preço "justo" de forma contínua.
""")

        elif subsecao == "Erros nos Dados":
            st.markdown(r"""
        ### **O Perigo dos Erros nos Dados**

        Erros nos dados podem comprometer significativamente estratégias de reversão à média, tanto em **backtesting** quanto na **execução ao vivo**. Pequenas falhas ou outliers nos preços históricos podem gerar oportunidades fictícias de lucro, inflando os resultados do backtest. Por exemplo, um registro de preço incorreto, que apareça muito acima do valor real, pode induzir a estratégia a sugerir uma venda a descoberto lucrativa que jamais ocorreria no mercado real.

        ##### Impacto nos Backtests
        - **Reversão à Média**: Dados imprecisos podem criar lucros artificiais, pois preços atípicos geram sinais falsos de entrada e saída.  
        - **Estratégias de Momentum**: Embora geralmente menos sensíveis, essas estratégias também podem ser afetadas, já que erros podem resultar em ordens de compra que rapidamente se transformam em perdas, prejudicando a performance do backtest.

        ##### Problemas na Execução ao Vivo
        - **Erros nas Cotações Bid/Ask**: Um erro que inflacione os preços de compra ou venda pode levar a ordens equivocadas, causando perdas reais.  
        - **Impacto em Pairs Trading e Arbitragem**: Estratégias que dependem de pequenas variações entre os preços dos ativos são particularmente vulneráveis. Um erro em uma das cotações pode aumentar artificialmente o spread, acionando negociações erradas.  
        - *Exemplo*: Se o spread real entre dois ativos for \$5 , mas um erro o faça parecer \$6 , um trade indevido pode ser executado, resultando em prejuízo.

        ##### Mitigação dos Erros
        - **Utilização de Feeds de Dados Confiáveis**: A escolha de fontes de dados robustas é crucial. Feeds de terceiros, como **Bloomberg** ou **Yahoo! Finance**, geralmente oferecem maior estabilidade e precisão.  
        - **Mecanismos de Correção em Tempo Real**: Alguns provedores utilizam sistemas de "cancel-and-correct", que ajustam automaticamente os dados quando erros são detectados, minimizando impactos negativos.

        Em resumo, dados errôneos representam um risco significativo para estratégias de **reversão à média** e **pairs trading**, onde pequenas discrepâncias podem ter grandes efeitos. A seleção criteriosa de fornecedores de dados e o monitoramento contínuo da qualidade são essenciais para evitar perdas desnecessárias e assegurar a eficácia das estratégias tanto em backtesting quanto na execução real.
        """)

        elif subsecao == "Conclusão":
            st.markdown("""
        ### Key Points: Mean-Reverting Strategies and Practical Considerations

        **Construção de Portfólios**:  
        - Para um portfólio de reversão à média com um **número fixo de ações**, utilize **séries de preços** para calcular os hedge ratios.  
        - Para um portfólio com **valores de mercado fixos**, utilize **logaritmos dos preços**.  

        **Escolha entre Spreads e Ratios**:  
        - Para **moedas e pares cambiais**, o **uso de razões (ratios)** pode ser mais eficaz do que spreads, especialmente quando não há cointegração perfeita.  

        **Ajustando-se a Mudanças no Mercado**:  
        - O **hedge ratio, a média e o desvio padrão** podem mudar ao longo do tempo. Para lidar com isso, utilize um **período de look-back móvel** ou um **Filtro de Kalman**.  

        **Bollinger Bands e Scaling-in**:  
        - A implementação prática de estratégias lineares de reversão à média pode ser feita com **Bandas de Bollinger** e **scaling-in**.  
        - Embora **scaling-in** nem sempre seja ótimo em backtests, ele pode ser útil no **trading ao vivo**, onde a volatilidade e as probabilidades mudam.  

        **Uso do Kalman Filter**:  
        - Para atualizar dinamicamente a **expectativa de preço** com base nos últimos negócios (preço e volume), o **Filtro de Kalman** pode ser empregado.  

        **Impacto de Erros nos Dados**:  
        - Erros de dados podem **inflacionar artificialmente os resultados** de backtests em estratégias de **reversão à média**, mas afetam menos estratégias de **momentum**.  
        - Estratégias baseadas em **spreads são altamente sensíveis** a pequenos erros de dados, tanto em backtests quanto em operações ao vivo.  

        A escolha dos métodos corretos para definir hedge ratios, ajustar estratégias e evitar armadilhas como erros de dados pode fazer a diferença entre um modelo teórico viável e uma estratégia prática e rentável no mercado real.
            """)

# ===================== Chapter 3 Implementing Mean Reversion Strategies =============

# ====================================================================================
    
# ===================== Chapter 4 Mean Reversion of Stocks and ETFs  =============

    elif pagina == "5 . Reversão à Média de Ações e ETFs":
        st.title("5 . Reversão à Média de Ações e ETFs")

        if subsecao == "Introdução":
            st.markdown("""
##### Mean Reversion of Stocks and ETFs**

O mercado de ações é um dos terrenos mais férteis para estratégias de **reversão à média** devido à sua alta diversidade e exposição a fatores econômicos comuns. Embora a teoria sugira que qualquer par de ações dentro de um setor pode apresentar **cointegração**, a realidade traz desafios específicos. Este capítulo explora como a reversão à média funciona em ações e ETFs, destacando estratégias práticas e dificuldades associadas.

##### **Principais Abordagens para Reversão à Média em Ações e ETFs**
- **Pares e triplets de ETFs**: Estratégias simples de reversão à média tendem a funcionar melhor em ETFs do que em ações individuais.  
- **Reversão à média sazonal**: No curto prazo, muitas ações demonstram comportamento de reversão mesmo em meio a um **caminho aleatório geométrico de longo prazo**.  
- **Arbitragem de Índice**: Estratégia baseada na **cointegração entre ações e futuros ou ações e ETFs**. Embora os lucros tenham diminuído, variações desta estratégia ainda podem ser exploradas.  
- **Reversão à média cross-sectional**: Ao contrário da reversão à média tradicional baseada no histórico de preços individuais, esta estratégia assume que os **retornos acumulados das ações em uma cesta convergem para a média da cesta**.  
- **Impacto da concorrência**: A grande quantidade de traders estatísticos explorando essas estratégias tem reduzido os retornos, tornando essencial a adoção de **técnicas adicionais para melhorar a performance**.  

##### **Considerações Importantes para Backtesting**
- **Custos de transação**: Não são incluídos nos backtests, pois variam conforme **método de execução e universo de ações escolhido**.  
- **Viés de sobrevivência**: Os dados utilizados podem conter viés, pois montar uma base **livre de viés de sobrevivência** é complexo e caro. Para uma análise mais precisa, seria necessário utilizar uma base contendo **a composição histórica diária do índice S&P 500**.  
- **Preços primários versus consolidados**: Os backtests utilizam **preços de fechamento consolidados**, mas estratégias de execução como **MOC (Market-on-Close)** ou **LOC (Limit-on-Close)** podem resultar em **preenchimentos diferentes**, impactando a performance real.  

O mercado de ações oferece um ambiente propício para estratégias de **reversão à média**, mas desafios como **custos de transação, concorrência e viés de sobrevivência** devem ser considerados. ETFs tendem a ser mais favoráveis do que ações individuais, e abordagens como **reversão sazonal e cross-sectional** ampliam as oportunidades. Porém, a necessidade de adaptações contínuas é essencial para manter a lucratividade dessas estratégias.  
""")

        elif subsecao == "Desafios na Negociação de Pares de Ações":
            
            st.markdown("""
            ## **Desafios na Negociação de Pares de Ações**

O **trading de pares de ações** foi uma das primeiras estratégias algorítmicas de **reversão à média**, mas hoje se tornou difícil extrair lucros consistentes. Isso ocorre porque as ações individuais raramente são **estacionárias**, seguindo um **caminho aleatório geométrico**. Mesmo pares de empresas do mesmo setor, como **Exxon vs. Chevron**, geralmente perdem **cointegração fora da amostra** devido a mudanças rápidas nas condições das empresas.

### **Principais Dificuldades**
- **Falta de Cointegração Consistente**  
  A correlação entre pares pode parecer forte em determinados períodos, mas frequentemente desaparece quando testada fora da amostra.  

- **Restrições à Venda a Descoberto**  
  Ações difíceis de tomar emprestado podem ser **recompradas à força** em momentos desfavoráveis, gerando **short squeezes**.  
  Além disso, desde 2010, a **regra do uptick** nos EUA limita ordens de venda a descoberto quando circuit breakers são acionados.  

- **Desafios no Trading Intradiário**  
  A diminuição da margem de lucro exige negociações rápidas, mas **o pequeno tamanho do NBBO (National Best Bid and Offer)** dificulta execuções eficientes.  
  Além disso, ordens grandes são fragmentadas ou ocultadas em **dark pools**, dificultando o preenchimento sem grande slippage.  

### **Por que o Trading de Pares de Ações Foi Lucrativo no Passado?**
- Mercados menos eficientes no passado possibilitavam lucros maiores, cobrindo perdas com pares que não revertiam à média.  
- A **decimalização dos preços das ações nos EUA** reduziu os spreads, prejudicando os lucros de traders que atuavam como market makers.  

### **Alternativa: ETFs ao invés de Ações**
Embora a negociação de pares de ações tenha perdido rentabilidade nos EUA, **pares de ETFs** ainda oferecem oportunidades lucrativas devido à sua maior liquidez e menor exposição a riscos específicos de empresas individuais.

            """)

            st.markdown("""
            ## **Trading de Pares de ETFs (e Triplas)**  

            ### **Vantagens dos Pares de ETFs**  
            Os pares de ETFs têm uma **maior estabilidade na cointegração** em comparação aos pares de ações. Isso ocorre porque os ETFs representam uma cesta de ativos, cuja composição muda mais lentamente do que o valor de uma empresa individual.  

            Por exemplo, os ETFs **EWA (Austrália) e EWC (Canadá)** são bons candidatos para cointegração devido às suas economias baseadas em commodities. Outra boa opção é o par **RTH (varejo) e XLP (bens de consumo),** setores que frequentemente compartilham fatores econômicos comuns.  

            Além disso, pares entre ETFs de commodities e **ETFs de empresas produtoras dessas commodities** também podem ser explorados. Um exemplo é o par **GLD (ouro físico) e GDX (mineradoras de ouro).** No entanto, essa cointegração foi quebrada em julho de 2008 devido à alta nos preços do petróleo, o que aumentou os custos de mineração e afetou as ações das mineradoras.  

            ### **Tripla Co-integração e Adaptação da Estratégia**  
            Para resolver essa quebra na cointegração, foi testada a introdução de um terceiro ativo no portfólio: **USO (fundo de petróleo).** O teste de Johansen indicou que GLD, GDX e USO formam um portfólio cointegrado, reforçando a importância de **adaptar estratégias conforme mudanças econômicas.**  

            Se operar um portfólio triplo for complicado, um trader pode pelo menos adotar uma **regra para interromper o trading de GLD-GDX sempre que o petróleo ultrapassar um certo limite de preço.**  

            ### **Riscos de ETFs de Commodities**  
            Nem todos os pares de ETFs de commodities são viáveis. Por exemplo, enquanto GLD realmente detém ouro físico, **USO investe em contratos futuros de petróleo,** e não no ativo físico. Como os preços futuros diferem dos preços à vista, pares como **USO-XLE (energia)** podem não ser adequados para negociação de reversão à média.  

            ### **Execução de Ordens em ETFs**  
            A mecânica de trading de pares de ETFs é similar à de pares de ações, mas com vantagens:  
            - O **tamanho do NBBO** (National Best Bid and Offer) para ETFs é maior, reduzindo problemas de liquidez.  
            - ETFs são afetados pelas **regras de uptick,** mas geralmente possuem maior facilidade de execução do que ações individuais.  

            Portanto, a negociação de pares de ETFs é uma **alternativa robusta à negociação de pares de ações**, com menos riscos de descontinuidade na cointegração e maior liquidez.  
            """)

        elif subsecao == "Buy-on-Gap Model":
            st.markdown("""
            ## **Reversão à Média Intradiária: Modelo Buy-on-Gap**  

            ### **Visão Geral**  
            Embora os preços das ações sigam um **caminho aleatório geométrico** no longo prazo, há condições em que a **reversão à média** pode ser explorada no curto prazo. O modelo **Buy-on-Gap** identifica oportunidades de reversão intradiária em ações que sofrem quedas bruscas na abertura do mercado.  

            ### **Regras da Estratégia**  
            1. Selecionar ações cuja variação do **piso do dia anterior** até a abertura de hoje seja menor que **uma vez o desvio padrão** dos últimos 90 dias.  
            2. Filtrar as ações cuja **abertura esteja acima da média móvel de 20 dias**.  
            3. Comprar as 10 ações com os **piores retornos em relação ao piso do dia anterior**. Se houver menos de 10 ações, comprar todas as disponíveis.  
            4. **Vender todas as posições no fechamento do mesmo dia.**  

            ### **Justificativa da Estratégia**  
            - **Pânico na abertura:** Ações podem ser vendidas em excesso na abertura devido a movimentos bruscos no índice futuro antes da abertura do mercado.  
            - **Filtro de Momentum (Regra 2):** Evita ações com **notícias negativas** reais (exemplo: resultados ruins), que tendem a continuar caindo.  
            - **Demanda de liquidez:** Investidores institucionais podem exagerar o movimento de queda ao vender para ajustar suas posições.  

            ### **Desempenho**  
            - **Período:** 11 de maio de 2006 a 24 de abril de 2012.  
            - **Taxa de retorno anualizada (APR):** 8,7%.  
            - **Sharpe Ratio:** 1,5.  
            - **Variação Short-Only:** Estratégia espelhada para **ações que sobem excessivamente** pode gerar APR de 46%, mas com maior drawdown devido a **restrições de venda a descoberto**.  

            ### **Pontos Importantes**  
            - **Ajustes possíveis:** Estratégia pode ser **combinada na versão long e short** ou protegida com hedge em futuros de índices.  
            - **Capacidade limitada:** Poucas ações atendem aos critérios diários, dificultando a escalabilidade.  
            - **Execução no pré-mercado:** Sinais podem ser gerados usando **preços pré-abertura** (exemplo: ARCA), mas haverá um **ruído** entre os sinais previstos e os preços reais de abertura.  
            - **Variação Setorial:** É possível limitar posições dentro de setores para evitar concentração de risco.  

            Essa estratégia ilustra como a **reversão à média pode existir em períodos específicos**, mesmo que não ocorra em amostragens diárias regulares.  
            """)

            colab_link = "https://colab.research.google.com/drive/1g4MIlioNhdUnepXnGlcX2sVoLQA-zTQ7?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar um exemplo no Colab]({colab_link})")

            #mostrar_imagem("https://example.com/imagem_scalping.png", "Scalping")
        


        elif subsecao == "Arbitragem entre um ETF e suas Ações Componentes":
            st.markdown("""
            ## **Arbitragem entre um ETF e suas Ações Componentes**  

            ### **Visão Geral**  
            A arbitragem entre um **ETF e um subconjunto de suas ações componentes** segue princípios semelhantes ao **index arbitrage**, mas com maior flexibilidade. Em vez de usar todas as ações do índice, escolhemos **apenas aquelas que cointegram com o ETF**, permitindo uma melhor oportunidade de arbitragem.  

            ### **Passos da Estratégia**  
            1. **Identificação de Ações Cointegrantes:**  
            - Utilizar um período de treinamento para encontrar **ações do índice que cointegram com o ETF** (exemplo: SPY).  
            - Aplicar o **teste de Johansen** para verificar a cointegração com **pelo menos 90% de probabilidade**.  

            2. **Construção do Portfólio:**  
            - Criar um portfólio **long-only** composto apenas por essas ações.  
            - Verificar novamente a cointegração entre o **portfólio** e o ETF.  

            3. **Implementação da Estratégia:**  
            - Utilizar um **modelo de reversão à média linear** para operar o portfólio contra o ETF.  
            - Determinar **hedge ratios** para manter o portfólio estacionário.  
            - Definir janelas de look-back para cálculo da média móvel e volatilidade.  

            ### **Considerações Importantes**  
            - **Alternativa ao Index Arbitrage:** A estratégia pode ser aplicada **a qualquer ETF, índice ou subíndice** e pode utilizar futuros no lugar do ETF, desde que os preços sejam contemporâneos.  
            - **Evitar Riscos de Venda a Descoberto:**  
            - Em vez de usar todos os ativos do índice, a estratégia **escolhe apenas os que cointegram**.  
            - Caso a venda a descoberto seja um problema, pode-se utilizar **otimização algorítmica (ex.: Algoritmos Genéticos, Simulated Annealing)** para construir um portfólio apenas com **posições longas**.  
            - **Desafio da Cointegração Ampla:**  
            - A execução de um **teste de Johansen direto em todas as ações do S&P 500 não é viável**.  
            - Em vez disso, é preciso testar **ação por ação**, formando um subconjunto.  

            Essa estratégia é uma forma **mais flexível e eficiente** de explorar a arbitragem entre ETFs e seus ativos subjacentes, contornando algumas limitações do **index arbitrage tradicional**.  
            """)

            colab_link = "https://colab.research.google.com/drive/1g4MIlioNhdUnepXnGlcX2sVoLQA-zTQ7?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar um exemplo no Colab]({colab_link})")

        elif subsecao == "Cross-Sectional Mean Reversion":
            st.markdown(
                """
        ## Reversão à Média Transversal: Modelo Linear Long-Short

        ### Visão Geral

        A estratégia de **reversão à média transversal** explora a anticorrelação serial dos **retornos relativos** das ações em um universo (ex: S&P 500 ou Russell 2000). Diferente da reversão à média baseada em cointegração (que usa um conjunto fixo de ativos), esta abordagem **reajusta os pesos ou seleciona diferentes ações diariamente**.

        ---

        ### Funcionamento da Estratégia

        - **Seleção e Alocação de Capital:**
            - Para cada ação \\(i\\), calcula-se o retorno diário \\(r_i\\).
            - Calcula-se o retorno médio do universo.
            - A alocação de capital para cada ação é dada por:

                $$
                w_i = -\\frac{r_i - \\langle r_j \\rangle}{\\sum_k |r_k - \\langle r_j \\rangle|}
                $$

            - **Vende-se a descoberto** ações com retornos acima da média.
            - **Compra-se** ações com retornos abaixo da média.
            - O total de capital alocado é **sempre 1**, garantindo neutralidade de mercado.

        ---

        ### Versão Intradiária

        - Utiliza **retornos do fechamento anterior até a abertura** para definir pesos.
        - Todas as posições são liquidadas no fechamento do mesmo dia.
        - **Resultados:**
            - **APR:** 73%
            - **Sharpe Ratio:** 4,7
        - **Desafios:** Custos de transação maiores e maior sensibilidade a ruídos no preço de abertura.

        ---

        ### Aprimoramentos e Fatores Alternativos

        - Além de **retornos relativos**, pode-se usar fatores preditivos:
            - **Índice P/L (P/E):**
                - Ações com aumento nas **estimativas de lucro** tendem a manter retornos positivos.
                - Evitar short nesses casos pode tornar a estratégia mais robusta.

        ---

        ### Considerações Finais

        - Estratégia **altamente flexível**, permite seleção dinâmica de ativos.
        - Menos dependente do desempenho individual de cada ação.
        - Pode ser aprimorada com **outras variáveis preditivas** para maior eficiência.

        [🔗 Clique aqui para editar um exemplo no Colab](https://colab.research.google.com/drive/1g4MIlioNhdUnepXnGlcX2sVoLQA-zTQ7?usp=sharing)
                """,
                unsafe_allow_html=True
            )



        elif subsecao == "Conclusão":
            st.markdown(r"""
- **Você sente vontade de negociar pares de ações devido ao enorme número de opções?**  
  Cuidado com mudanças nos fundamentos das empresas, que podem tornar o desempenho fora da amostra bastante fraco, apesar de excelentes resultados nos backtests.

- **Negociar um portfólio de ETFs cointegrados pode ser melhor do que negociar pares de ações.**  

- **Você está negociando pares de ETFs que possuem futuros?**  
  Cuidado com o impacto dos retornos de rolagem na determinação dos retornos totais dos futuros.

- **A reversão à média sazonal ou intradiária é difícil de detectar com os testes usuais de estacionariedade ou cointegração, mas pode ser muito lucrativa.**  

- **Impor um filtro de momentum às estratégias de reversão à média geralmente melhora sua consistência.**  

- **Você acha que a arbitragem de índice entre ações e futuros não é mais lucrativa?**  
  Experimente selecionar apenas um subconjunto das ações do índice.

- **Estratégias de reversão à média transversal podem ser implementadas facilmente com uma estratégia linear long-short.**  

- **A variável usada para classificar ações em uma estratégia de reversão à média transversal geralmente é o retorno relativo, mas pode incluir outros fatores fundamentais, como a relação P/L (Preço/Lucro).**

            """)
# ===================== Chapter 4 Mean Reversion of  =============

# ====================================================================================


# ===================== Chapter 5 Mean Reversion of Currencies and Futures =============

    elif pagina == "6 . Reversão à Média de Moedas e Futuros":
        st.title("6 . Reversão à Média de Moedas e Futuros")
        if subsecao == "Introdução":
            st.markdown(r"""
        ### Introdução
        A sabedoria convencional diz que moedas e contratos futuros são território dos traders de momentum — e, em geral, isso é verdade. A maioria dos CTAs (Commodities Trading Advisors) utiliza estratégias baseadas em momentum.

        Além disso, é raro encontrar pares de moedas ou futuros que apresentem cointegração, e portfólios desses ativos costumam **não** exibir reversão à média transversal. Ou seja, as oportunidades para estratégias de reversão à média nesses mercados são **limitadas**, mas não inexistentes.

        Neste capítulo, vamos explorar exatamente **quando e onde** a reversão à média pode ser aplicada em moedas e futuros, destacando casos especiais como os spreads de calendário em futuros (calendar spreads). Em especial, será apresentada uma estratégia de trading envolvendo o spread entre futuros de volatilidade e futuros de índices de ações.

        Também vamos discutir um modelo matemático simples para preços de futuros, ajudando a entender conceitos como:
        - **Spot x Retorno de Rolagem (roll return)**
        - **Backwardation x Contango**

        Compreender esse modelo abre caminho para novas estratégias de trading com futuros — sem depender apenas de indicadores técnicos arbitrários.

        Por fim, será abordado como operar moedas exige certos cuidados, diferentes do trading de ações. É preciso atenção especial ao testar cointegração entre moedas e ao calcular retornos de portfólios, garantindo que movimentos em diferentes pares tenham o **mesmo valor em dólares**. Além disso, os juros de rolagem (rollover) podem influenciar bastante o retorno total, dependendo do contexto.

        Essas nuances e particularidades serão detalhadas ao longo desta seção.
        """)

 
        elif subsecao == "Negociação de Pares de Moedas":
            st.markdown(r"""
            ### Negociando Cross-Rates de Moedas

            A ideia de formar um portfólio estacionário de moedas estrangeiras é semelhante à negociação de pares de ETFs de ações de diferentes países: procuramos países com fundamentos econômicos parecidos. Por exemplo, se ETFs de ações da Austrália (EWA) e do Canadá (EWC) apresentam cointegração, é razoável esperar que o dólar australiano (AUD) e o dólar canadense (CAD) também possam cointegrar. O mesmo pode acontecer com o dólar australiano (AUD) e o rand sul-africano (ZAR), já que ambos países têm forte presença no setor de mineração. Moedas como AUD, ZAR e a coroa norueguesa (NOK) são conhecidas como **moedas de commodities**.

            #### Vantagens do Trading de Moedas

            Negociar pares de moedas oferece diversas vantagens em relação aos pares de ETFs:
            - **Alta liquidez**: Menores custos de transação devido a spreads mais estreitos.
            - **Alavancagem elevada**: É possível operar com margens menores, mas atenção ao risco.
            - **Sem restrição de venda a descoberto**.
            - **Mercado 24h**: É possível operar praticamente cinco dias por semana, com mais oportunidades e uso eficiente de stop losses.

            Apesar da semelhança conceitual com pares de ETFs, a **mecânica de operação em moedas é bem diferente**. Ao negociar um cross-rate como AUD.ZAR, AUD é a moeda base e ZAR é a moeda de cotação (quote). Por exemplo, uma cotação AUD.ZAR de 9,58 significa que são necessários 9,58 rands para comprar 1 dólar australiano.

            #### Criação de Pares Sintéticos

            Muitas corretoras não oferecem diretamente todos os cross-rates (ex: AUD.ZAR). Para negociar, geralmente é preciso montar um **par sintético** usando moedas mais líquidas (como USD ou EUR):

            - Exemplo: Para negociar AUD.ZAR, pode-se comprar USD.ZAR e vender USD.AUD, formando o par sintético **USD.ZAR / USD.AUD**, que replica a cotação AUD.ZAR.

            Ao operar esses pares, os lucros podem ficar denominados em diferentes moedas. Para que o P&L realizado reflita o backtest, é preciso **converter regularmente todos os saldos para a moeda local** (ex: USD para investidores americanos).

            #### Estratégias Cointegradas e Hedge Ratio

            Mesmo quando existe um cross-rate pronto (ex: AUD.CAD), pode ser vantajoso operar cada moeda separadamente usando AUD.USD versus USD.CAD, permitindo ajustar o hedge ratio de capital de forma ótima via o **teste de Johansen**. Para isso, ambos os pares devem estar na mesma moeda de cotação, garantindo que movimentos de preço tenham o mesmo valor em dólares.

            No exemplo clássico do livro:
            - O portfólio é construído usando os pesos do eigenvector do teste de Johansen entre AUD.USD e CAD.USD.
            - Calcula-se o número de unidades a operar com base no desvio da média móvel (z-score).
            - O P&L diário é calculado em USD, com retornos ajustados pelo valor de mercado do portfólio.

            **Dica importante:** O maior desafio não é a estratégia em si, mas **preparar corretamente as séries de preços** para o teste de cointegração e calcular os retornos corretamente.

            ---
            """)

            st.markdown(r"""
            ### Juros de Rolagem (Rollover) em Trading de Moedas

            Ao operar pares de moedas (cross-rates), um fator importante é o **juros de rolagem** (“rollover interest”), que representa a diferença entre as taxas de juros das moedas do par quando a posição é mantida de um dia para o outro (após 17h de NY).

            - **Cálculo:**  
              Se você está comprado no par B.Q durante a noite, o juros de rolagem é:

              $$
              i_B - i_Q
              $$

              onde $i_B$ e $i_Q$ são as taxas de juros diárias das moedas B e Q.  
              - Se $i_Q > i_B$, você **paga** juros (débito na conta).  
              - Se $i_B > i_Q$, você **recebe** juros.

            - **Finais de semana e feriados:**  
              Devido ao sistema de liquidação (T+2), se você mantém a posição após 17h na quarta-feira, os juros de rolagem são multiplicados por 3 (referente a sexta, sábado e domingo).  
              Existem exceções, como pares USD.CAD e USD.MXN, onde a liquidação é T+1.

            #### Impacto no Backtesting e Sharpe Ratio

            Ao calcular o Sharpe ratio, deve-se considerar **excess return** — ou seja, o retorno descontando o custo de financiamento.  
            - Para estratégias **intraday** ou portfólios neutros em dólar (ações ou futuros), geralmente o custo é zero.  
            - Para pares de moedas, o custo de financiamento é zero **apenas se** o juros de rolagem for incorporado no cálculo de retorno.

            Por isso, o retorno excessivo diário ao manter uma posição de B.Q de $t$ para $t+1$ é:

            $$
            r_{t+1} = \log(y_{B.Q}(t+1)) - \log(y_{B.Q}(t)) + \log(1 + i_B(t)) - \log(1 + i_Q(t))
            $$

            Onde:
            - $y_{B.Q}(t)$ é a cotação do par no tempo $t$  
            - $i_B(t)$ e $i_Q(t)$ são as taxas de juros diárias  

            #### Exemplo Prático: Estratégia de Reversão à Média com AUD.CAD e Rollover

            - O exemplo usa uma estratégia simples de reversão à média no par pronto AUD.CAD, incorporando o juros de rolagem nos retornos.  
            - As taxas diárias de juros (AUD e CAD) devem ser ajustadas para considerar rolagens múltiplas em determinados dias da semana.

            **Resumo dos resultados:**  
            - APR = 6,2%  
            - Sharpe ratio = 0,54  
            - Se ignorarmos o juros de rolagem, os resultados sobem levemente, mas a diferença pode ser relevante para estratégias de longo prazo.

            **Conclusão:**  
            Mesmo que o impacto dos juros de rolagem em estratégias de curto prazo seja pequeno, ele pode ser significativo ao longo do tempo. Por isso, sempre ajuste os retornos no backtest para refletir corretamente o efeito do rollover.

            ---
            """, unsafe_allow_html=True)




        elif subsecao == "Taxas Cruzadas de Moedas":
            
            st.markdown("""
                        
            A negociação de pares de moedas baseia-se na mesma lógica da reversão à média aplicada a ETFs de índices de ações: buscar ativos que compartilham fundamentos econômicos semelhantes e que, portanto, exibem movimentos de preços cointegrados. Por exemplo, como EWA (ETF da Austrália) e EWC (ETF do Canadá) apresentam cointegração, é razoável supor que suas moedas — AUD (dólar australiano) e CAD (dólar canadense) — também possam se mover de forma correlacionada. Da mesma forma, moedas como AUD e ZAR (rand sul-africano), associadas a economias com forte dependência de commodities, são conhecidas como “commodity currencies”.

            ### Vantagens do Trading de Moedas

            O mercado cambial oferece vantagens significativas em relação ao mercado de ações: maior liquidez, menores custos de transação, ausência de restrições de venda a descoberto e operação contínua cinco dias por semana. Além disso, a alta alavancagem disponível amplia as oportunidades — embora também eleve o risco. A liquidez contínua permite ainda o uso eficiente de mecanismos de stop loss, o que seria inviável em mercados que permanecem fechados por longos períodos.

            ### Estrutura e Mecânica das Operações

            Em um par cambial como AUD.ZAR, AUD é a **moeda base** e ZAR é a **moeda cotada** — ou seja, AUD.ZAR = 9,58 significa que são necessários 9,58 rands para comprar 1 dólar australiano. Contudo, muitos corretores não oferecem diretamente esse cruzamento; por isso, cria-se uma **paridade sintética**, como USD.ZAR/USD.AUD. Nessa estrutura, o lucro ou prejuízo realizado envolve múltiplas moedas (ZAR e AUD) e precisa ser convertido regularmente para a moeda local do investidor (geralmente USD) para manter a coerência entre os resultados reais e os simulados no backtest.

            ### Teste de Cointegração e Estratégia de Hedge

            A estratégia exemplificada (Exemplo 5.1) utiliza o **teste de Johansen** para determinar o hedge ratio ideal entre pares como AUD.USD e CAD.USD, assegurando que ambos compartilhem a mesma moeda de cotação (USD) — condição essencial para que os movimentos de preço tenham o mesmo valor nominal. A partir da cointegração, constrói-se um portfólio linear reversor à média, no qual a exposição é ajustada dinamicamente conforme o desvio do spread em relação à sua média móvel.

            Essa abordagem gera um portfólio com retornos estacionários, cujo desempenho pode ser medido em termos de **APR (Annual Percentage Return)** e **Sharpe Ratio**, indicadores que, no exemplo do autor, alcançaram 11% e 1,6, respectivamente. A principal complexidade dessa técnica não está na execução da estratégia, mas sim na preparação correta das séries de preços e na formulação precisa dos retornos.

            """)


            st.divider()


        elif subsecao == "Operando Calendar Spread com Futuros":
            st.markdown("""
                ### **Futures Intermarket Spreads**

                Intermarket spreads em contratos futuros envolvem pares de ativos subjacentes diferentes. Embora seja difícil encontrar spreads com comportamento de reversão à média, existem alguns candidatos interessantes, especialmente em mercados inter-relacionados.

                ### Exemplos de Spreads em Mercados de Energia
                1. **Crack Spread (CL, RB e HO)**:
                - Consiste em uma carteira formada por três contratos longos de WTI crude oil (CL), dois contratos short de gasolina (RB) e um contrato short de óleo de aquecimento (HO).
                - Representa a relação entre a produção de derivados a partir do petróleo bruto, onde a proporção 3:2:1 reflete a produção média de refinarias.
                - **Resultado do Teste ADF**: Não estacionário. Durante o período de 2007-2008, apresentou alta volatilidade e retornos negativos em estratégias de reversão à média.
                - **Vantagem Operacional**: A NYMEX oferece uma cesta pronta para o crack spread, reduzindo os requisitos de margem em comparação com negociações separadas.

                2. **Spread entre CL e BZ (1:1)**:
                - Ambas as commodities representam petróleo bruto (WTI e Brent), sugerindo uma relação forte.
                - **Resultado do Teste ADF**: Não estacionário, devido a fatores como:
                    - Aumento da produção de petróleo nos EUA.
                    - Gargalos nos oleodutos em Cushing, Oklahoma.
                    - Questões geopolíticas, como o embargo ao petróleo iraniano, que impactaram o Brent (BZ) mais do que o WTI (CL).

                ### Cuidados no Backtesting de Intermarket Spreads
                1. **Sincronização de Preços**: Certifique-se de que os preços sejam registrados no mesmo horário. Antes de setembro de 2001, o Brent (BZ) era negociado na Intercontinental Petroleum Exchange em Londres, com horário de fechamento diferente do NYMEX, onde o WTI (CL) é negociado.
                2. **Ajustes para USD**: Futuros podem exigir multiplicadores para converter os preços para dólares americanos, garantindo consistência nos cálculos.

                ### Conclusão
                Embora intermarket spreads sejam promissores em mercados relacionados, como energia, a falta de estacionariedade torna muitos deles inadequados para estratégias de reversão à média. A análise cuidadosa e a consideração de fatores como sincronização de preços são essenciais para evitar erros em backtests e estratégias.
                """)

            mostrar_imagem("https://example.com/imagem_rompimento.png", "Estratégias de Rompimento")


        elif subsecao == "Spreads Intermercado com Futuros":
            st.markdown("""
                        
            A busca por **spreads intermercado** em contratos futuros — isto é, combinações de futuros sobre diferentes ativos subjacentes — visa identificar pares de mercados que se movam de forma correlacionada e possam apresentar **reversão à média**. Embora o conceito pareça simples, encontrar spreads verdadeiramente estacionários nesse contexto é uma tarefa desafiadora.

            ### Spreads no Complexo de Energia

            Um dos exemplos mais intuitivos de spreads intermercado surge no **complexo de energia**, que inclui contratos como o petróleo bruto WTI (CL), o Brent (BZ), a gasolina (RB) e o óleo para aquecimento (HO), todos negociados na NYMEX. Entre eles, destaca-se o conhecido **crack spread**, composto por uma posição **long** em três contratos de petróleo bruto (CL), **short** em dois contratos de gasolina (RB) e **short** em um contrato de óleo para aquecimento (HO). Essa proporção 3:2:1 reflete o processo físico de “cracking” do petróleo, no qual três barris de petróleo produzem aproximadamente dois de gasolina e um de óleo de aquecimento.  

            A vantagem prática desse spread é que a NYMEX oferece um **contrato padronizado de crack spread**, com exigência de margem inferior à de operar os três contratos separadamente. No entanto, testes estatísticos — como o **ADF (Augmented Dickey-Fuller)** aplicado entre 2002 e 2012 — indicam que o spread **não é estacionário**. Durante esse período, o valor do spread apresentou forte alta entre março de 2007 e julho de 2008, seguida de uma queda acentuada, resultando em **retornos negativos** para estratégias lineares de reversão à média.

            ### O Spread entre Brent e WTI

            Outro candidato natural seria o spread entre **CL (WTI)** e **BZ (Brent)** em proporção 1:1, uma vez que ambos representam tipos de petróleo bruto. Contudo, testes de estacionariedade mostram que essa relação também **não apresenta reversão à média**. O Brent tem consistentemente superado o WTI, impulsionado por fatores estruturais e geopolíticos, como o aumento da produção norte-americana, gargalos logísticos em Cushing (Oklahoma) e o embargo ao petróleo iraniano em 2012, que afetou mais fortemente o mercado europeu.

            ### Considerações Metodológicas

            Ao realizar backtests de spreads intermercado, é essencial garantir que as **séries de preços sejam síncronas**. Por exemplo, antes de o Brent começar a ser negociado na NYMEX em 2001, ele era cotado na Intercontinental Petroleum Exchange de Londres, com horário de fechamento diferente do WTI. Usar preços de fechamento não alinhados temporalmente distorceria os resultados. Além disso, os preços devem ser devidamente **ajustados por fatores de conversão em dólares** e **corrigidos nos rollovers** para evitar saltos artificiais nas séries.

            Apesar de as tentativas iniciais com o complexo de energia não indicarem spreads estacionários, o autor ressalta que existem **casos excepcionais** — explorados a seguir — em que estratégias de reversão à média podem, sim, ser aplicadas com sucesso no mercado de futuros.

            """)

          

        elif subsecao == "Conclusão":
            st.markdown(r"""
            ### Pontos-Chave sobre Moedas e Futuros

            - **Moedas de Commodities:**  
              Moedas como AUD, CAD, ZAR e NOK frequentemente apresentam oportunidades de **cointegração** devido a fundamentos econômicos semelhantes (ex: exportação de commodities).

            - **Cálculo de Retornos em Portfólios de Moedas:**  
              Atenção ao combinar cross-rates: os retornos dependem se os pares compartilham a **mesma moeda base**, a **mesma moeda de cotação** ou **nenhuma das duas**.  
              → As fórmulas de retorno mudam conforme o caso.

            - **Retornos de Futuros:**  
              Todo contrato futuro possui **dois componentes de retorno**:
              1. **Spot return** (variação do ativo-spot).  
              2. **Roll return** (diferença entre contratos de vencimentos distintos).

            - **Backwardation vs. Contango:**  
              - **Backwardation:** roll return **positivo** → contratos mais longos são **mais baratos** que os curtos.  
              - **Contango:** roll return **negativo** → contratos mais longos são **mais caros** que os curtos.

            - **Impacto do Roll Return:**  
              A reversão à média do preço spot **não garante** reversão à média nos preços dos futuros — porque o roll return altera a dinâmica.

            - **Calendar Spreads em Futuros:**  
              A reversão à média de spreads de calendário só ocorre se o **roll return** for ele próprio estacionário (ou seja, reverter à média).  

            ---
            """)

# ===================== Chapter 5 Mean Reversion of Currencies and Futures =============

# ====================================================================================

# ===================== Chapter 6 Interday Momentum Strategies ==================

    elif pagina == "7 . Estratégias de Momentum Interdiário":
        st.title("7 . Estratégias de Momentum Interdiário")
        
        if subsecao == "Introdução":
           st.markdown("""
                **Momentum in Trading**

                Momentum em preços de ativos tem quatro causas principais: persistência nos retornos de rolagem de futuros, lenta assimilação de novas informações, compras ou vendas forçadas por fundos e manipulação de mercado por traders de alta frequência. Esse fenômeno é classificado em dois tipos: **momentum temporal**, em que retornos passados estão positivamente correlacionados com retornos futuros, e **momentum cross-sectional**, em que ativos com desempenho superior a outros tendem a continuar superando. Estratégias de momentum interday, abordadas neste capítulo, mantêm posições por vários dias e podem explorar esses padrões. No entanto, elas apresentam fragilidades recentemente identificadas, que afetam menos as estratégias de momentum intraday, tema do próximo capítulo. Além disso, estratégias de momentum diferem significativamente de estratégias de reversão à média em propriedades, vantagens e desvantagens.

                ### Considerações Finais
                Momentum é uma ferramenta poderosa para trading, especialmente em futuros e ações, mas requer atenção às suas fragilidades e ao contexto de aplicação. A distinção entre estratégias interday e intraday permite adaptar os modelos a diferentes dinâmicas de mercado, maximizando retornos enquanto minimiza riscos associados às vulnerabilidades recentemente descobertas.
                """)

        elif subsecao == "Testes para Momentum em Séries Temporais":

           st.markdown("""
            
            **Tests for Time Series Momentum**

            O momentum em séries temporais ocorre quando retornos passados estão **positivamente correlacionados** com retornos futuros. Para testar essa característica, utilizamos métricas estatísticas como o **coeficiente de correlação** e o **p-valor**, que indicam se a relação entre os retornos é estatisticamente significativa.

            ### Métodos de Teste para Momentum
            1. **Correlação entre Retornos Passados e Futuros**:
            - Identifica pares de períodos (look-back e holding) com maior correlação positiva.
            - Exemplo: O retorno de **20 dias no passado** pode estar mais correlacionado com o **retorno de 40 dias no futuro** do que com um retorno de apenas 1 dia.

            2. **Correlação entre Sinais de Retorno**:
            - Mede se um movimento de alta tende a ser seguido por outro, independentemente da magnitude dos retornos.

            3. **Testes de Tendência de Longo Prazo**:
            - **Hurst Exponent** e **Variance Ratio Test**: Avaliam se a série segue uma tendência ou um comportamento de random walk.
            - Esses testes, originalmente usados para detecção de reversão à média, também são úteis para identificar momentum.

            ### Cuidados na Computação dos Testes
            - **Evitar Dados Sobrepostos**:  
            - Se o **look-back** for maior que o **holding period**, avançamos os dados pelo tamanho do período de holding.  
            - Se o **holding period** for maior que o **look-back**, avançamos pelo período de look-back.  
            - Esse ajuste garante que os pares de retornos sejam independentes, evitando viés nos resultados.

            ### Exemplo Prático
            A aplicação desses testes no **futuro de Treasury Note de 2 anos (TU)** da CME pode ajudar a identificar padrões de momentum. No MATLAB, funções como **corrcoef** (para correlação), **genhurst** (para o Hurst exponent) e **vratiotest** (para o Variance Ratio test) podem ser utilizadas para validar a presença de momentum em diferentes períodos.

            ### Conclusão
            A escolha correta do período de look-back e holding é essencial para maximizar a eficácia de uma estratégia de momentum. O uso de múltiplos testes estatísticos permite identificar padrões robustos e evitar armadilhas de aleatoriedade nas séries temporais.
            """)

           colab_link = "https://colab.research.google.com/drive/1g-HL2ofAAB_hcgWXqSgg4vyf_sipGoyJ?usp=sharing"  # Coloque o link do Colab aqui
           st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")

        elif subsecao == "Estratégias de Séries Temporais":
           
           st.markdown("""
**Time Series Strategies**

As estratégias de **time series momentum** exploram a correlação entre retornos passados e futuros para identificar padrões preditivos. Se a correlação entre um retorno passado e um retorno futuro for significativa (correlação alta e p-valor baixo), pode-se testar uma estratégia lucrativa baseada nesses períodos de análise e manutenção.

### Construção da Estratégia  
- **Escolha dos Parâmetros**:  
  - Exemplo: Para o contrato futuro **TU**, os retornos de **250 dias de look-back** e **25 dias de holding** apresentaram uma correlação de **0.27** e um p-valor de **0.02**, indicando um possível sinal de momentum.  

- **Regras da Estratégia**:  
  - Inspirada no estudo de **Moskowitz, Yao e Pedersen (2012)**, a estratégia compra se o retorno dos últimos **12 meses** for positivo e vende se for negativo.  
  - A posição é mantida por **1 mês**.  
  - Em vez de negociar apenas uma vez por mês, a versão modificada da estratégia realiza uma **nova decisão diária**, investindo gradualmente **1/25 do capital total por dia**.  

### Conclusão  
Essa abordagem busca capturar tendências persistentes no mercado ao longo do tempo. A adaptação da frequência de negociação para decisões diárias pode suavizar a volatilidade e melhorar a eficiência do capital alocado na estratégia.
""")
           colab_link = "https://colab.research.google.com/drive/1g-HL2ofAAB_hcgWXqSgg4vyf_sipGoyJ?usp=sharing"  # Coloque o link do Colab aqui
           st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")


           
        elif subsecao == "Extraindo Retornos de Rolagem":

            st.markdown("""
### **Extracting Roll Returns through Future versus ETF Arbitrage**

O retorno total de um contrato futuro é composto por **retorno do ativo à vista + roll return**. Dessa forma, podemos capturar o **roll return** através de uma estratégia de arbitragem entre o ativo subjacente e o contrato futuro correspondente. Se o **roll return for negativo** (contango), podemos **comprar o ativo e vender o futuro**. Se for **positivo** (backwardation), fazemos o oposto.

#### Arbitragem entre Futuros e ETFs  
Para facilitar a execução da estratégia, em vez de comprar diretamente o ativo subjacente (o que pode ser complicado), utilizamos **ETFs** que possuem o ativo físico:
- **Exemplo: Ouro (GLD vs. GC)**  
  - O ETF **GLD** detém ouro físico e acompanha o preço à vista do metal.  
  - Os **futuros de ouro (GC)** têm um **roll return negativo** de -4,9% ao ano (1982-2004).  
  - Estratégia: **Long GLD e Short GC** → Backtest mostrou retorno anualizado de **1,9%** com drawdown máximo de **0,8%** (2007-2010).  
  - **Problema**: O custo de financiamento de GLD praticamente elimina esse lucro.

#### Arbitragem Alternativa: ETFs de Empresas do Setor  
Como a maioria das commodities **não possui ETFs com o ativo físico**, podemos usar ETFs de empresas que produzem a commodity como proxy:
- **Exemplo: Energia (XLE vs. USO)**  
  - **XLE**: ETF do setor energético, composto por empresas relacionadas ao petróleo.  
  - **USO**: ETF que contém contratos futuros de WTI Crude Oil (CL).  
  - **Estratégia**:  
    - **Short USO e Long XLE quando CL estiver em contango.**  
    - **Long USO e Short XLE quando CL estiver em backwardation.**  
  - **Resultado**: Retorno anualizado de **16%** (2006-2012) com **Sharpe ratio ≈ 1**.

#### Arbitragem com Índices Voláteis  
Para futuros sem um ativo subjacente negociável, como o **VIX**, podemos buscar instrumentos correlacionados.  
- **Exemplo: VIX (VX) e S&P 500 (SPY/ES)**  
  - O ETF **SPY** (S&P 500) tem alta correlação negativa com o VIX.  
  - O **E-mini S&P 500 (ES)** tem roll return insignificante (~1% ao ano), tornando-se uma alternativa melhor para a arbitragem.  

### Conclusão  
A arbitragem entre ETFs e futuros pode ser uma forma eficiente de capturar **roll returns**, especialmente quando um ETF físico não está disponível. O uso de ETFs setoriais e ativos correlacionados permite a aplicação dessa estratégia em diferentes mercados, maximizando oportunidades de arbitragem.
""")
            
            st.divider()
            
            st.markdown("""
### **Volatility Futures versus Equity Index Futures: Redux**

Os futuros de volatilidade **VX** apresentam **roll returns altamente negativos** (até -50% anualizados) e são **altamente anticorrelacionados** com os futuros do índice **E-mini S&P 500 (ES)**, com um coeficiente de correlação de -75%. Em **Capítulo 5**, essa relação foi explorada para desenvolver uma **estratégia de reversão à média**. Aqui, utilizamos essa mesma dinâmica para construir uma **estratégia de momentum baseada no roll return**.

#### Estratégia Proposta por Simon e Campasano (2012)
1. **Venda em Contango**:  
   - Se o preço do contrato futuro **VX** estiver **0.1 ponto acima do VIX** multiplicado pelo número de dias até o vencimento,  
   - **Short 0.3906 contratos de VX** e **Short 1 contrato de ES**.  
   - **Segura a posição por 1 dia**.

2. **Compra em Backwardation**:  
   - Se o preço do contrato futuro **VX** estiver **0.1 ponto abaixo do VIX** multiplicado pelo número de dias até o vencimento,  
   - **Compra 0.3906 contratos de VX** e **Compra 1 contrato de ES**.  
   - **Segura a posição por 1 dia**.

#### Justificativa da Estratégia
- Se o preço do **VX** está **acima** do preço do **VIX**, isso indica um **roll return negativo** → **Vendemos VX**.  
- Se o preço do **VX** está **abaixo** do preço do **VIX**, isso indica um **roll return positivo** → **Compramos VX**.  

#### Ajustes e Resultados
- A razão de hedge usada na estratégia é baseada em uma **regressão entre os preços** de VX e ES (e não entre os retornos, como no estudo original).  
- O período de backtest (29/07/2010 - 07/05/2012) gerou um **APR de 6.9%** com um **Sharpe Ratio de 1**.  

#### Conclusão
A estratégia explora a **relação entre o roll return de VX e a dinâmica de ES**, aproveitando a **forte anticorrelação** entre os dois ativos para gerar lucros consistentes. O modelo ajustado mostrou desempenho estável, sugerindo que a abordagem pode ser utilizada para operar futuros de volatilidade de forma sistemática.
""")


            colab_link = "https://colab.research.google.com/drive/1g-HL2ofAAB_hcgWXqSgg4vyf_sipGoyJ?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")
            
        elif subsecao == "Estratégias Cross-Sectional":
            
            st.markdown("""
### **Cross-Sectional Strategies**

Além de comprar e segurar futuros ou utilizá-los em arbitragem contra ativos subjacentes, uma terceira abordagem para capturar **roll returns** é o uso de **estratégias cross-sectional**. Esse método consiste em **comprar futuros em backwardation** e **vender a descoberto futuros em contango**, esperando que os retornos dos preços à vista se neutralizem e que reste apenas o **ganho proveniente dos roll returns**.

#### **Estratégia de Momentum Cross-Sectional**  
Inspirada no modelo de **Daniel & Moskowitz (2011)**, essa estratégia segue uma abordagem semelhante à estratégia de reversão à média proposta por **Khandani & Lo**, mas com períodos de **look-back e holding muito mais longos**:
1. **Ranking de Commodities**:  
   - Ordena-se **52 commodities físicas** com base no **retorno dos últimos 12 meses (252 dias de negociação)**.  
   - Compra-se o futuro com o **maior retorno** e vende-se o futuro com o **menor retorno**.  
   - Mantém-se as posições por **1 mês (25 dias de negociação)**.  

2. **Resultados do Backtest**:  
   - De **junho de 2005 a dezembro de 2007**, a estratégia teve um **APR de 18%** e um **Sharpe Ratio de 1.37**.  
   - No entanto, sofreu um colapso durante a **crise financeira de 2008-2009**, com um **APR de -33%** nesse período.  

#### **Expansão da Estratégia para Outros Mercados**  
Daniel & Moskowitz demonstraram que essa abordagem funciona para **várias classes de ativos**, incluindo:  
- **Índices de ações globais**  
- **Moedas**  
- **Ações internacionais**  
- **Ações dos EUA**  

A persistência do momentum nesses mercados não pode ser explicada apenas pelo **sinal dos roll returns**, mas pode ser atribuída a fatores como:
- **Correlação serial no crescimento econômico global** (afeta moedas e índices).  
- **Difusão lenta de informações no mercado de ações** (impacta o momentum em ações).  

#### **Aplicação da Estratégia em Ações (Cross-Sectional Momentum para Stocks)**  
- Compra-se ações no **topo do decil dos retornos dos últimos 12 meses** e vende-se ações no **fundo do decil**.  
- Essa abordagem pode ser expandida utilizando **outros fatores** além do retorno passado, como:  
  - **Fatores fundamentais**: crescimento de lucros, book-to-price ratio.  
  - **Fatores estatísticos**: Principal Component Analysis (PCA).  

#### **Cross-Sectional Factors em Futuros**  
- Modelos fatoriais podem ser aplicados a **portfólios de futuros**, considerando **fatores macroeconômicos** como **crescimento do PIB** ou **taxa de inflação**.  
- PCA pode ser usado para identificar **componentes estatísticos ocultos** que explicam os retornos dos futuros.  

#### **Conclusão**  
As estratégias **cross-sectional** são uma forma poderosa de capturar **momentum** e **roll returns**, permitindo a diversificação entre diferentes mercados. Apesar dos desafios enfrentados em **períodos de crise**, elas permanecem relevantes e podem ser aprimoradas com modelos fatoriais e técnicas avançadas de análise de dados.  
""")

            st.divider()
            st.markdown("""
### **News Sentiment as a Fundamental Factor**

Com o avanço dos **newsfeeds programáveis** e da **análise de linguagem natural (NLP)**, tornou-se possível quantificar o impacto de notícias sobre ações por meio de **sentiment scores**. Esse fator fundamental pode ser utilizado para estratégias de **momentum cross-sectional**, aproveitando a **difusão lenta de informações** no mercado.

#### **Impacto do Sentimento das Notícias em Estratégias de Momentum**
- Pesquisadores como **Hafez & Xie (2012)** demonstraram que estratégias baseadas no sentimento das notícias podem gerar retornos expressivos:  
  - **APR entre 52% e 156%** e **Sharpe Ratios de 3.9 a 5.3** (antes dos custos de transação).  
  - Estratégia: **comprar ações com mudanças positivas de sentimento** e **vender ações com mudanças negativas de sentimento**.  

#### **Fornecedores de News Sentiment Data**
- **RavenPack**: Um dos principais provedores de análise de sentimento baseada em notícias.  
- **Outros fornecedores**:  
  - **Recorded Future**  
  - **thestocksonar.com**  
  - **Thomson Reuters News Analytics**  
  - **Bloomberg Event-Driven Trading**  
  - **Dow Jones Elementized News Feeds**  

Caso um trader acredite possuir um **modelo de sentimento superior**, pode adquirir diretamente um **newsfeed elementizado** e aplicar seu próprio algoritmo.  

#### **Análise de Sentimento em Redes Sociais**  
- Pesquisadores como **Bollen, Mao & Zeng (2010)** sugeriram que o **humor coletivo no Twitter** pode prever o comportamento de índices de mercado.  
- Essa hipótese levou ao lançamento de **hedge funds baseados em análise de mídias sociais**, embora a validade dessas pesquisas tenha sido contestada.  

#### **Conclusão**  
O **sentimento das notícias** oferece um fator adicional para estratégias quantitativas, permitindo explorar a **assimetria de informação e a lentidão na assimilação de notícias pelo mercado**. Apesar de desafios na implementação, a combinação de **NLP e análise de sentimentos** pode ser uma ferramenta poderosa para estratégias algorítmicas de momentum.  
""")

            st.divider()
            # Outro

        elif subsecao == "Prós e Contras das Estratégias de Momentum":
            
            st.markdown("""
**Pros and Cons of Momentum Strategies**

As estratégias de **momentum** possuem características de risco e retorno **opostas** às estratégias de **reversão à média**. Embora possam gerar retornos elevados em certos cenários, também apresentam desafios significativos.  

### **Contras das Estratégias de Momentum**
1. **Menor Sharpe Ratio e Menos Sinais Independentes**  
   - Estratégias de momentum tendem a ter um **Sharpe Ratio mais baixo** do que estratégias de reversão à média.  
   - Como possuem **longos períodos de look-back e holding**, os sinais de negociação são menos frequentes, reduzindo a consistência dos retornos.  

2. **"Momentum Crashes" Pós-Crise Financeira**  
   - Pesquisas mostram que estratégias de momentum **desempenham mal após crises financeiras** (Daniel & Moskowitz, 2011).  
   - Exemplo: O índice **S&P DTI** sofreu um drawdown de -25,9% desde 2008.  
   - Em alguns casos históricos, estratégias de momentum levaram **décadas para se recuperar** (como após o crash de 1929).  

3. **Duração Decrescente do Momentum**  
   - Conforme mais traders adotam estratégias de momentum, os períodos em que essas tendências persistem **ficam cada vez mais curtos**.  
   - Exemplo: O impacto de anúncios de lucros costumava durar **dias**, mas agora pode se dissipar antes do fechamento do mercado.  

### **Prós das Estratégias de Momentum**
1. **Gestão de Risco Mais Eficiente**  
   - Momentum strategies permitem **saídas predefinidas**, seja por **tempo (holding period)** ou **stop loss**, limitando perdas.  
   - **Stop losses** são compatíveis com momentum, pois indicam a reversão da tendência, enquanto **não funcionam bem** em estratégias de reversão à média.  

2. **Potencial de Altos Retornos em Eventos Extremos ("Black Swans")**  
   - Estratégias de momentum **não possuem limite de ganhos**, ao contrário das estratégias de reversão à média, onde o lucro é limitado pelo retorno à média.  
   - Mercados com alta **kurtosis** (distribuição de retornos com caudas mais pesadas) favorecem estratégias de momentum.  

3. **Diversificação Global e Multiativos**  
   - A maioria dos **futuros e moedas** exibe momentum, permitindo **diversificação entre diferentes classes de ativos e países**.  
   - Combinar **momentum e reversão à média** pode melhorar o **Sharpe Ratio** e reduzir drawdowns, criando um portfólio mais robusto.  

### **Conclusão**
Apesar das dificuldades, estratégias de **momentum** podem ser extremamente lucrativas, especialmente em mercados voláteis e sujeitos a eventos extremos. Quando combinadas com estratégias de **reversão à média**, ajudam a criar um portfólio mais equilibrado e resistente a diferentes condições de mercado.  
""")

        elif subsecao == "Conclusão":
            
            st.markdown("""
**Key Points: Momentum Strategies**

- **Tipos de Momentum**:  
  - **Time-series momentum**: Retornos passados de um ativo **estão positivamente correlacionados** com seus retornos futuros.  
  - **Cross-sectional momentum**: Ativos que tiveram retornos superiores no passado tendem a continuar superando outros ativos no portfólio.  

- **Momentum em Futuros e Commodities**:  
  - Futuros exibem **time-series momentum** devido à **persistência do sinal dos roll returns**.  
  - É possível extrair **roll returns** de futuros encontrando um instrumento correlacionado (ETF ou outro futuro) e ajustando as posições conforme o mercado está em **contango** ou **backwardation**.  

- **Momentum em Ações e Portfólios**:  
  - Portfólios de ações ou futuros costumam apresentar **cross-sectional momentum**.  
  - Estratégias simples de **ranking de retornos** podem ser eficazes para capturar essa tendência.  

- **Fatores que Contribuem para Momentum**:  
  - **Difusão lenta de notícias** cria oportunidades de negociação baseadas em **sentimento de mercado**.  
  - **Vendas forçadas de ativos** por fundos mútuos geram movimentos prolongados nos preços das ações.  

- **Momentum e Eventos Extremos ("Black Swans")**:  
  - Estratégias de momentum **se beneficiam** de eventos raros e extremos.  
  - A distribuição dos retornos com **caudas mais pesadas (alta kurtosis)** favorece estratégias de momentum.  

### **Conclusão**  
Estratégias de momentum podem ser aplicadas em **diversos mercados**, aproveitando a persistência dos retornos, a reação a notícias e eventos extremos. Quando bem estruturadas, podem complementar estratégias de reversão à média para melhorar o desempenho e a resiliência do portfólio.
""")

# ===================== Chapter 6 Interday Momentum Strategies =============


# ===================== Chapter 7 Intraday Momentum Strategies ==================

    elif pagina == "8 . Estratégias de Momentum Intradiário":
        st.title("8 . Estratégias de Momentum Intradiário")

        if subsecao == "Introdução":
           
           st.markdown("""
**Estratégias de Momentum Intradiário**

No capítulo anterior, constatamos que a maioria dos ativos financeiros – sejam **ações** ou **futuros** – apresenta momentum tanto em termos **cross-sectional** quanto **time-series**. Contudo, esse momentum tende a ocorrer em horizontes de tempo mais longos (um mês ou mais), o que gera dois problemas principais:

1. **Baixo Sharpe Ratio e Significância Estatística**:  
   - A escassez de sinais de negociação independentes reduz a eficácia das estratégias.

2. **Desempenho Deficiente em Períodos de Crise**:  
   - Estratégias de longo prazo sofrem perdas acentuadas durante períodos de turbulência econômica.

### **Momentum Intradiário: Uma Alternativa Eficaz**

Este capítulo propõe o uso de **estratégias de momentum intradiário** para superar as limitações das abordagens tradicionais. Diferentemente do momentum de longo prazo – frequentemente influenciado por fatores como **roll returns** –, o foco aqui é a ação do preço ao longo do mesmo dia.

### **Fatores Determinantes do Momentum Intradiário**

1. **Ativação de Stop Loss e Estratégias de Breakout**  
   - Ordens de stop acionadas em pontos de suporte e resistência podem desencadear movimentos explosivos.  
   - Exemplos incluem entradas de mercado na abertura e operações baseadas em níveis técnicos.

2. **Eventos Corporativos e Macroeconômicos**  
   - Anúncios de lucros, mudanças nas recomendações de analistas e notícias macroeconômicas estimulam um momentum de curtíssimo prazo.  
   - Pesquisas recentes demonstram como esses eventos influenciam o comportamento intradiário dos mercados.

3. **Rebalanceamento de ETFs Alavancados**  
   - A necessidade diária de ajuste das posições por parte dos fundos alavancados gera padrões previsíveis no fluxo de ordens, resultando em momentum de curto prazo.

4. **Dinâmica do Fluxo de Ordens e High-Frequency Trading (HFT)**  
   - Desequilíbrios entre ordens de compra e venda, combinados com alterações no fluxo e concentração de stop orders, podem ocasionar movimentos rápidos.  
   - Estratégias de HFT se aproveitam desses pequenos deslocamentos para obter lucros consistentes.

### **Conclusão**

As **estratégias de momentum intradiário** surgem como uma alternativa promissora para superar os desafios inerentes às abordagens de longo prazo. Ao explorar eventos corporativos, dinâmicas do fluxo de ordens e movimentos de stop loss, essas estratégias oferecem oportunidades de lucro com uma exposição reduzida aos riscos macroeconômicos.

""")

        elif subsecao == "Opening Gap Strategy":

            st.markdown("""
  **Resumo da Estratégia de Momentum por Gap**

  Diferente da estratégia de reversão à média para ações, esta abordagem foca em aproveitar os gaps de preço. A ideia é comprar quando o ativo apresenta gap de alta e vender (ou operar vendido) quando ocorre gap de baixa.

- **Mecanismo de Acionamento:**  
  Os gaps resultam de períodos prolongados sem negociação, o que pode gerar uma diferença expressiva entre os preços de fechamento e de abertura. Esse cenário provoca o disparo simultâneo de ordens stop, criando um efeito cascata que intensifica o movimento de preço.
  Eventos importantes que ocorrem durante esses períodos também podem contribuir para a formação de gaps e para a geração de momentum.
                        
- **Aplicação em Futuros:**  
  A estratégia tem sido aplicada com sucesso em futuros, demonstrando bom desempenho quando o gap ocorre entre o fechamento e a abertura do mercado, impulsionando os movimentos de preço.

- **Aplicação em Moedas:**  
  Para moedas, é necessário redefinir os horários de abertura e fechamento do mercado. A estratégia se aproveita do gap gerado pelo período em que o mercado está fechado (por exemplo, do final de semana) para capturar movimentos significativos na abertura.

A estratégia de momentum por gap busca explorar os movimentos abruptos entre o fechamento e a abertura do mercado, seja em futuros ou em moedas, capturando oportunidades de lucro a partir do efeito cascata das ordens stop e de eventos relevantes.

            """)

            colab_link = "https://colab.research.google.com/drive/1s9QKpA72ZDvngGyvqkb44A7JuyPsYhbA?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")

            st.divider()
            
        elif subsecao == "News Sentiment":

            st.markdown("""
### **Post-Earnings Announcement Drift - (PEAD)**

- **Conceito Básico:**  
  - Acredita-se que o momentum é impulsionado pela lenta difusão das notícias. Assim, é possível se beneficiar dos primeiros momentos — horas ou até segundos — após um evento relevante, como anúncios de lucros.

- **Dinâmica do PEAD:**  
  - Após o anúncio dos lucros, os preços das ações se movem de forma persistente na mesma direção do movimento inicial, permitindo que traders capturem esse drift sem precisar julgar se os resultados foram “bons” ou “ruins”.
  - A estratégia consiste em entrar na posição no início do dia seguinte ao anúncio (comprando se o retorno for muito positivo e vendendo se for muito negativo) e liquidá-la ao final do mesmo dia.

- **Implementação Prática:**  
  - É essencial dispor de dados históricos precisos dos horários dos anúncios de lucros para identificar corretamente os eventos ocorridos após o fechamento do dia anterior e antes da abertura do dia atual.
  - O critério para entrar na operação envolve medir a volatilidade dos retornos (por exemplo, utilizando a média móvel da volatilidade) e selecionar apenas os anúncios que surpreendem o mercado.

- **Resultados e Observações:**  
  - Em testes com um universo de ações, a estratégia PEAD demonstrou resultados positivos, com retornos consistentes e Sharpe ratio robusto.
  - A alavancagem pode ser utilizada para potencializar os ganhos diários.
  - Manter as posições durante a noite não agrega valor, pois os retornos noturnos costumam ser negativos.  
  - O fenômeno, estudado desde 1968, pode ter tido sua duração encurtada devido ao aumento da conscientização do mercado sobre essa vantagem.

            """)
            st.divider()

            st.markdown("""
    ### **Drift Decorrente de Outros Eventos**

- **Outros Eventos Corporativos:**  
  - Além dos anúncios de lucros, outros eventos como orientações de lucro, mudanças de ratings de analistas, dados de vendas em lojas e fatores de carga aérea também podem gerar drift pós-anúncio.
  - Qualquer evento que leve a uma reavaliação do valor justo de uma empresa tende a provocar um movimento no preço da ação em direção a um novo equilíbrio.

- **Fusões e Aquisições (M&A):**  
  - Apesar de serem analisados profundamente por fundos especializados, modelos técnicos simples podem capturar drift pós-anúncio em M&A, demonstrando retornos positivos mesmo em cenários contrários à crença comum.

- **Rebalanceamento de Índices:**  
  - Alterações na composição de índices provocam pressão de compra ou venda imediata, gerando momentum, cujo efeito se restringiu a um período intradiário nos últimos anos.

- **Eventos Macroeconômicos:**  
  - Testes em EURUSD não indicaram momentum significativo para eventos como decisões de taxa de juros ou divulgação do índice de preços ao consumidor.
  - Em contraste, dados macroeconômicos do Reino Unido e anúncios do Banco da Inglaterra mostraram gerar momentum no GBPUSD por alguns minutos, embora a duração desse efeito possa ter sido reduzida com o tempo.
""")

        elif subsecao == "Leveraged ETF Strategy":
            st.markdown("""
**Leveraged ETF Strategy**

ETFs alavancados possuem uma dinâmica de **reequilíbrio diário**, que pode gerar **momentum previsível no mercado**, especialmente próximo ao fechamento. Como esses ETFs precisam **manter uma alavancagem constante** (por exemplo, 3×), eles realizam **compras e vendas forçadas** dependendo da variação diária do mercado.

#### **Como o Rebalanceamento dos ETFs Gera Momentum?**
- Se o **índice subjacente cai**, o ETF **precisa vender ações** para manter a alavancagem.  
- Se o **índice sobe**, o ETF **precisa comprar mais ações**.  
- Como esses ETFs movimentam **centenas de milhões de dólares**, essa atividade gera **momentum significativo próximo ao fechamento**.  
- ETFs **long** e **short** são afetados igualmente, pois ETFs inversos também precisam ajustar posições.  

#### **Estratégia de Momentum Baseada em ETFs Alavancados**
- **Ativo:** DRN (ETF alavancado 3× de real estate).  
- **Sinal de Entrada:**  
  - **Comprar** DRN se o retorno desde o fechamento do dia anterior até **15 minutos antes do fechamento** for **maior que +2%**.  
  - **Vender** DRN se o retorno for **menor que -2%**.  
- **Saída:** Fechar a posição no fechamento do mercado.  
- **Resultados do Backtest (12/10/2011 a 25/10/2012):**  
  - **APR: 15%**  
  - **Sharpe Ratio: 1.8**  

#### **Impacto do Crescimento dos ETFs Alavancados**
- Em **janeiro de 2009**, os ETFs alavancados (long e short) tinham um **AUM total de US$ 19 bilhões**.  
- Um **movimento de 1% no S&P 500 pode gerar operações equivalentes a 17% do volume de fechamento**, impactando o mercado (Cheng & Madhavan, 2009).  
- Estudos mais recentes **confirmam esse efeito** (Rodier, Haryanto, Shum & Hejazi, 2012).  

#### **O Papel do Fluxo de Investimentos nos ETFs**
- Grandes **aportes em ETFs long alavancados** criam **momentum positivo** nas ações subjacentes.  
- Grandes **aportes em ETFs inversos (short)** criam **momentum negativo**.  
- Apesar da possibilidade de **neutralização do efeito por investidores realizando lucros**, os backtests mostram que **o momentum persiste**.  

Os **ETFs alavancados criam oportunidades previsíveis de momentum próximo ao fechamento**, devido ao **reequilíbrio obrigatório das posições**. À medida que esses ETFs **crescem em tamanho**, seu impacto no mercado pode **se tornar ainda mais relevante** para estratégias de trading.  
""")

            
            colab_link = "https://colab.research.google.com/drive/1s9QKpA72ZDvngGyvqkb44A7JuyPsYhbA?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")

            st.divider()
 
        elif subsecao == "Estratégias de Alta Frequência":
          st.markdown("""
                      
### **Estratégias de Alta Frequência (HFT)**  

As estratégias de alta frequência (HFT) exploram **padrões de curto prazo** no mercado, baseando-se em **livro de ordens, fluxo de ordens e stop orders**. Elas exigem **dados detalhados** e **execução extremamente rápida**, sendo amplamente aplicadas em ações, futuros e moedas.  

---

#### **Desequilíbrio entre Oferta e Demanda**  
Pesquisas indicam que existe uma **relação linear** entre o desequilíbrio no **livro de ordens** e mudanças de preço de curto prazo.  
- Se o **tamanho do bid** for muito maior que o **ask**, há maior chance de o preço subir.  
- Se o **ask** for maior, a tendência é de queda.  
- Esse efeito é **mais forte** em ações de **baixo volume**.  

---

#### **Ratio Trade (Pro-Rata Fills)**  
Alguns mercados, como o **Eurodollar** no CME, preenchem ordens proporcionalmente ao tamanho delas.  
- O trader pode entrar no **melhor bid** para garantir uma fração da execução sempre que houver um preenchimento no bid.  
- Se o preço subir, ele vende no **ask**, lucrando com o spread.  

---

#### **Ticking ou Quote Matching**  
Se o **spread bid-ask** for **maior que dois ticks**, um trader pode:  
1. Colocar uma **compra um tick acima do bid**.  
2. Vender **um tick abaixo do ask**.  
3. Se ambas forem executadas, o trader captura o lucro com base no spread.  

**Risco:** Se a compra for executada, mas a venda não, o trader pode ser forçado a liquidar a posição a um preço inferior.  

---

#### **Momentum Ignition (Criação de Pressão Artificial de Compra/Venda)**  
Traders podem **manipular o mercado** criando **falsa pressão de compra ou venda**:  
1. Colocam uma **grande ordem de compra no bid**, atraindo traders que esperam alta.  
2. Simultaneamente, colocam uma **pequena ordem de venda no ask**, que é executada.  
3. Depois, **cancelam a grande ordem de compra**, gerando pânico e forçando traders a venderem a um preço mais baixo.  

---

#### **Flipping (Revertendo Manipulação de Outros Traders)**  
Se um trader suspeitar que uma **grande ordem de compra** é falsa (*momentum ignition*), ele pode:  
1. **Vender contra a ordem manipulada**.  
2. Se o manipulador cancelar sua ordem, o preço pode cair, e o trader compra de volta mais barato.  
3. Isso força o manipulador a sair de sua posição com prejuízo.  

Para detectar manipulação, traders podem monitorar **cancelamentos frequentes de ordens grandes** por meio de feeds privados das exchanges (*ITCH da Nasdaq, PITCH da BATS, etc.*).  

---

#### **Stop Hunting (Caça a Stops)**  
HFTs exploram **níveis de suporte e resistência**, onde muitos traders colocam ordens de **stop-loss**.  
1. Criam **pressão artificial** para romper um suporte.  
2. Ativam stops de venda, forçando o preço ainda mais para baixo.  
3. Compram as posições liquidadas a preços menores, lucrando quando o preço estabiliza.  

Esse comportamento gera **momentum de curto prazo**, especialmente no mercado de moedas e futuros.  

---

#### **Monitoramento de Fluxo de Ordens (Order Flow Trading)**  
O **fluxo de ordens** representa o volume líquido de compras e vendas em tempo real.  
- HFTs monitoram **grandes ordens unidirecionais** (ex.: hedge funds reagindo a notícias), pois isso sinaliza **novas informações no mercado**.  
- **Market makers ajustam seus preços** rapidamente ao detectar ordens grandes, e os traders de alta frequência podem antecipar essas mudanças.  

Ferramentas como **ITCH da Nasdaq e PITCH da BATS** permitem acesso detalhado ao histórico de ordens, ajudando a identificar **flippers e manipulação de mercado**.  

---

As estratégias de **HFT** são sofisticadas e exploram **ineficiências momentâneas do mercado**, obtendo lucros contra **traders mais lentos**. No entanto, a crescente competição:  
- **Reduziu os tamanhos das ordens visíveis**.  
- **Fragmentou o mercado**.  
- **Diminuiu as margens de lucro** entre os próprios traders de alta frequência.  

A evolução da tecnologia continuará moldando esse ambiente, tornando-o cada vez mais desafiador para novos participantes.  
""")

        elif subsecao == "Conclusão":
            st.markdown("""
**Estratégias de Momentum Intradiário**

As estratégias de momentum intradiário **não sofrem com muitas das desvantagens** das estratégias de momentum interdiário, mas ainda **mantêm algumas vantagens importantes**.  

#### **Tipos de Estratégias de Momentum**
- **Estratégias de "Breakout"** ocorrem quando o preço **ultrapassa um intervalo de negociação**.  
- A **estratégia de gap na abertura** é um tipo de breakout que funciona para **alguns futuros e moedas**.  
- O momentum de breakout pode ser causado pela **ativação de ordens de stop**.  

#### **Fatores que Induzem Momentum de Curto Prazo**
- **Notícias corporativas e macroeconômicas** frequentemente geram **momentum de curto prazo** nos preços.  
- Mudanças na **composição de índices** criam momentum nas ações que são **adicionadas ou removidas** do índice.  
- O **reequilíbrio dos ETFs alavancados** perto do fechamento **gera momentum na mesma direção do retorno do mercado desde o fechamento anterior**.  

#### **Momentum de Alta Frequência e Fluxo de Ordens**
- Muitas estratégias de momentum de **alta frequência** envolvem **desequilíbrio entre os tamanhos do bid e ask**, um desequilíbrio que às vezes é **artificialmente criado pelos próprios traders de alta frequência**.  
- **Stop hunting** é uma estratégia de **trading de alta frequência** que visa **acionar ordens de stop**, geralmente próximas a **números redondos** perto do preço de mercado.  
- O **fluxo de ordens** pode prever **movimentos de preço de curto prazo na mesma direção**.  

As estratégias de momentum intradiário oferecem **vantagens sobre as estratégias interdiárias**, aproveitando fatores como **breakouts, gaps de abertura, mudanças em índices e reequilíbrio de ETFs alavancados**. Além disso, o **trading de alta frequência** desempenha um papel significativo na criação e exploração do momentum de curto prazo.  
""")

# ===================== Chapter 7 Interday Momentum Strategies =============


# ====================================================================================

# ==================== Chapter 8 - Gestão de Risco ========================

    elif pagina == "9 . Gestão de Riscos":
        st.title("Gestão de Risco")

        if subsecao == "Introdução":
            st.markdown("""
            A gestão de risco é interpretada de maneiras variadas, mas geralmente está associada à aversão a perdas, um comportamento emocional amplamente discutido por Kahneman (2011). Apesar de compreensível, essa aversão nem sempre é racional, pois o objetivo central deve ser a maximização do crescimento do patrimônio no longo prazo.

            Uma gestão de risco eficaz exige o uso prudente da alavancagem, que pode ser otimizada por ferramentas como a fórmula de Kelly, projetada para maximizar a taxa de crescimento composta do capital. Além disso, estratégias como stop loss e constant proportion portfolio insurance (CPPI) são frequentemente implementadas para limitar perdas severas. O CPPI, em particular, busca equilibrar a proteção contra perdas significativas e a maximização de ganhos potenciais.

            Outra abordagem relevante é a de evitar operar em condições adversas, identificando períodos de maior probabilidade de perdas por meio de indicadores de risco. Essa prática permite uma alocação mais eficiente do capital, preservando recursos para momentos mais favoráveis.
            """)

        elif subsecao == "Alavancagem":
            st.markdown(r"""
            ## Optimal Leverage (Alavancagem Ótima)

            A alavancagem, embora seja uma ferramenta poderosa para potencializar os retornos de uma estratégia de trading, traz consigo desafios significativos. A questão central é como determinar a alavancagem ideal para maximizar os retornos, sem correr riscos excessivos. Se a alavancagem for zero, não haverá risco, mas também não se gerará nenhum retorno. Portanto, é essencial encontrar o ponto de equilíbrio.

            Para muitos gestores, especialmente os que administram seus próprios fundos, o objetivo principal é maximizar o crescimento do patrimônio ao longo do tempo. Eles tendem a ignorar volatilidades e quedas de curto prazo. Para esses traders, a alavancagem ótima é aquela que maximiza a taxa de crescimento composta do portfólio, mantendo o risco sob controle.

            Existem várias abordagens para calcular a alavancagem ótima, sendo que a maioria delas se baseia na suposição de que a distribuição dos retornos futuros será semelhante à dos retornos passados. Embora essa premissa não seja completamente precisa, ela é amplamente utilizada em modelos quantitativos. A fórmula de Kelly, por exemplo, assume uma distribuição Gaussiana e oferece uma solução simples para calcular a alavancagem ideal que maximiza o crescimento composto, sem levar a uma perda total do capital (ruína).
            
            ---
                        
            """)

            latext = r'''
            ### A fórmula de Kelly

            A **Fórmula de Kelly** é amplamente utilizada em finanças e estratégias de trading para determinar o nível ótimo de alavancagem e maximizar o crescimento composto do capital. Ela é especialmente relevante quando assumimos que os retornos seguem uma distribuição aproximadamente Gaussiana (normal). O uso da Fórmula de Kelly foi popularizado por Edward Thorp e explorado em profundidade no livro *Quantitative Trading* (Chan, 2009).

            A **Fórmula de Kelly** determina o nível ótimo de alavancagem \( f \) usando a seguinte equação:

            $$
            f = \frac{m}{\sigma^2}
            $$

            Onde:

            - $$ m $$ é o retorno médio excedente (*mean excess return*);
            - $${\sigma^2}$$ é a variância dos retornos excedentes.

            Se assumirmos que os retornos seguem uma distribuição normal (*Gaussiana*), o valor \( f \) calculado pela **Fórmula de Kelly** maximiza a taxa de crescimento composta do capital ao longo do tempo, desde que todos os lucros sejam reinvestidos.
            '''
            st.write(latext)


            code = '''
                import yfinance as yf
                import numpy as np

                def kelly_formula(ticker, risk_free_rate=0.02, start_date="2010-01-01", end_date="2024-12-31"):
                    # Baixar dados históricos do Yahoo Finance
                    data = yf.download(ticker, start=start_date, end=end_date)

                    # Calcular os retornos diários
                    data['Daily Return'] = data['Adj Close'].pct_change()

                    # Calcular o retorno médio excedente (m) e a variância dos retornos excedentes (s^2)
                    excess_returns = data['Daily Return'] - (risk_free_rate / 252)  # Ajustar taxa livre de risco para base diária
                    mean_excess_return = np.mean(excess_returns)
                    variance_excess_return = np.var(excess_returns)

                    # Aplicar a Fórmula de Kelly
                    if variance_excess_return > 0:
                        optimal_leverage = mean_excess_return / variance_excess_return
                    else:
                        optimal_leverage = 0  # Evitar divisão por zero

                    # Exibir resultados
                    print(f"Ticker: {ticker}")
                    print(f"Retorno médio excedente (m): {mean_excess_return:.6f}")
                    print(f"Variância dos retornos excedentes (s^2): {variance_excess_return:.6f}")
                    print(f"Alavancagem ótima (f): {optimal_leverage:.2f}")

                    return optimal_leverage

                # Exemplo de uso
                ticker_symbol = "MSFT"  # Símbolo da ação, ex: AAPL para Apple, MSFT para Microsoft
                optimal_leverage = kelly_formula(ticker_symbol)

            ====================== Output ============================
                Retorno médio excedente (m): 0.000820
                Variância dos retornos excedentes (s^2): 0.000259
                Alavancagem ótima (f): 3.16
            '''
            st.code(code, language="python")

            colab_link = "https://colab.research.google.com/drive/1oomGr66P92TigEEDKj5b7bkmaxkHSa_v?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")


            st.write(r"""
                     
            ---           
            ### Monte Carlo Simulation and Leverage Optimization         

            Para determinar a alavancagem ótima em distribuições não-Gaussianas, a fórmula de Kelly pode não ser suficiente. Nessas situações, simulações de Monte Carlo ajudam a estimar o crescimento composto esperado. Considerando que a taxa livre de risco é zero, a fórmula para o crescimento composto esperado em função da alavancagem \(f\) é:

            """)

            st.latex(r"g(f) = \langle \log(1 + fR) \rangle")

            st.markdown(
    r"Onde \( R(t) \) é o retorno diário (ou em qualquer período definido) da estratégia, e $\langle ... \rangle$ representa a média sobre amostras aleatórias da distribuição de \( R \). Se a distribuição for Gaussiana, a fórmula se reduz a:"
)
            st.latex(r"g(f) = fm - \frac{f^2 m^2}{2}")

            st.write(r"""
            Essa fórmula é equivalente à da alavancagem de Kelly em distribuições Gaussianas, onde o máximo de \( g(f) \) pode ser encontrado derivando a equação com relação a \( f \) e igualando a zero. No entanto, para distribuições não-Gaussianas, como as modeladas pelo sistema de Pearson, a solução analítica pode ser impossível.

            O **Sistema de Pearson** utiliza a média, desvio padrão, assimetria e curtose da distribuição empírica para ajustá-la a uma das sete distribuições parametrizadas, incluindo Gaussiana, beta, gamma e Student's t. Embora não capture todos os momentos superiores ou distribuições infinitas, é suficiente para evitar viés por excesso de ajuste em dados limitados.

            """)
            colab_link = "https://colab.research.google.com/drive/1oomGr66P92TigEEDKj5b7bkmaxkHSa_v?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")



            # ==========================

            st.write(r"""
                      
            ---         

            ### Optimization of Historical Growth Rate
                     
            Em vez de otimizar o valor esperado da taxa de crescimento usando uma distribuição analítica de probabilidades dos retornos, como feito anteriormente, podemos simplesmente otimizar a taxa de crescimento histórica no backtest em relação à alavancagem. 

            Este método requer apenas um conjunto específico de retornos: aqueles que realmente ocorreram no backtest. Contudo, essa abordagem apresenta limitações significativas:

            - **Viés de Data-Snooping**: A otimização nos retornos históricos pode levar a um ajuste excessivo aos dados, resultando em uma alavancagem que não será ideal para realizações futuras.
            - **Generalização Limitada**: A alavancagem ótima encontrada para a realização histórica pode não ser aplicável a outras realizações futuras da estratégia.

            Apesar dessas limitações, em alguns casos, a otimização direta sobre os retornos históricos pode produzir resultados semelhantes à alavancagem de Kelly e à otimização baseada em Monte Carlo.

            #### Método Prático

            Usando a mesma estratégia mencionada anteriormente, podemos alterar o programa de otimização para utilizar os retornos históricos  no lugar dos retornos simulados. Embora essa abordagem possa fornecer insights rápidos, é importante interpretar os resultados com cautela devido aos problemas inerentes ao uso exclusivo de dados históricos.

            Essa técnica pode ser útil como complemento a métodos mais robustos, como simulações de Monte Carlo, especialmente quando aplicada em conjunto com validações cruzadas ou outros mecanismos para mitigar o viés de ajuste aos dados históricos.
            """)

            st.markdown(""" 
            ---             

            ### Drawdown

            Embora a alavancagem ótima deva maximizar o crescimento composto, muitos traders impõem restrições ao nível de drawdown, ou seja, a perda máxima permitida em relação ao valor do portfólio. Isso é feito para proteger o portfólio de perdas excessivas e manter o risco em níveis aceitáveis. Quando esse limite é estabelecido, o cálculo da alavancagem ótima deve ser ajustado para garantir que a perda máxima não seja ultrapassada.

            Drawdown representa a redução percentual entre o valor máximo atingido pelo portfólio e o seu valor mínimo subsequente, antes que ele volte a crescer. Em outras palavras, é a maior queda sofrida pelo portfólio durante um determinado período. Por exemplo, se o valor do portfólio sobe para 100 mil e em seguida cai para 80 mil, o drawdown será de 20%.

            O drawdown é uma métrica crucial para avaliar o risco de uma estratégia de investimento ou trading. Ele permite entender não apenas o quanto uma estratégia pode perder em momentos de adversidade, mas também como isso pode impactar a capacidade do investidor de permanecer fiel ao plano inicial. Estratégias com drawdowns elevados podem ser insustentáveis a longo prazo, pois podem levar a decisões emocionais, como resgates antecipados ou abandonos de estratégias rentáveis.

            Portanto, ao ajustar a alavancagem para respeitar um nível aceitável de drawdown, os traders buscam equilibrar o crescimento do portfólio com a proteção contra perdas significativas, garantindo assim uma gestão de risco mais robusta.
                        
            ---                      
            """)

            st.markdown("""
                ### Constant Proportion Portfolio Insurance (CPPI)**

                O método CPPI combina o objetivo de maximizar a taxa de crescimento composta com a limitação de perdas máximas (drawdown). Ele separa o capital total em duas partes: uma subconta alocada para negociação e uma conta em caixa. A subconta recebe uma alocação equivalente a uma proporção fixa **D** do capital total, e uma alavancagem **f** é aplicada apenas nessa subconta. Isso garante que o drawdown máximo não exceda **-D** do capital total.  

                ### Funcionamento do CPPI
                1. **Alocação Inicial**:
                - Aloca **D** do capital total para a subconta de negociação.
                - O restante (**1-D**) permanece em caixa para proteger contra perdas.
                2. **Reajuste do Capital**:
                - Quando o capital total atinge um novo pico, a subconta é reajustada para manter a proporção **D**.  
                - Em caso de perdas, o capital não é transferido da conta de caixa para a subconta.
                3. **Encerramento da Estratégia**:
                - Caso a subconta perca todo o seu capital, a estratégia é abandonada, servindo como um mecanismo automático de contenção de riscos.

                ##### Comparação com Alavancagem Reduzida
                Embora pareça semelhante ao uso de uma alavancagem reduzida (**fD**), o CPPI ajusta dinamicamente o tamanho das ordens, reduzindo o risco de atingir o drawdown máximo. Isso também evita o comportamento emocional no encerramento de estratégias.  

                ##### Vantagens do CPPI
                - Limitação do drawdown ao valor projetado (**-D**) por design.
                - Taxa de crescimento composta similar a estratégias com alavancagem reduzida, mesmo após períodos longos.  
                - Redução mais rápida do tamanho das posições em períodos de drawdown, protegendo o capital restante.

                ##### Limitações do CPPI
                - Não oferece proteção contra grandes gaps de mercado ou suspensões de negociação. O uso de opções fora do dinheiro pode mitigar esse risco.  
                - Deve ser aplicado a contas com apenas uma estratégia, pois estratégias não lucrativas podem ser "subsidiadas" por outras em contas multiestratégias, mascarando os drawdowns reais.

                O CPPI é uma abordagem eficiente para maximizar o crescimento composto enquanto limita drawdowns, oferecendo um método disciplinado e automático para controlar riscos. No entanto, é necessário atenção para lidar com eventos fora do controle, como gaps de mercado.
                """)
            
            mostrar_imagem("img/cppi.png", "Constant Proportion Portfolio Insurance (CPPI)")

            colab_link = "https://colab.research.google.com/drive/1oomGr66P92TigEEDKj5b7bkmaxkHSa_v?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")

            st.divider()
            st.write("""
    
            ### Conclusão

            A alavancagem ótima deve equilibrar os retornos desejados com o risco de perdas excessivas, respeitando limitações de drawdown. Embora a alavancagem constante seja fundamental para otimizar o crescimento composto, ela pode gerar efeitos negativos, especialmente durante crises. Por isso, é importante gerenciar cuidadosamente os níveis de risco e estar ciente das implicações dessa estratégia no longo prazo.

            """)

        elif subsecao == "Indicadores e métricas":
            st.markdown("""    
            Os indicadores de risco proativos ajudam a evitar períodos desfavoráveis para estratégias de trading ao antecipar riscos. Diferentes indicadores são eficazes dependendo da estratégia utilizada:

            ##### VIX:
            O índice de volatilidade implícita é útil para identificar riscos. Em estratégias como buy-on-gap, um VIX acima de 35 pode indicar alta rentabilidade, enquanto para outras, como gap de abertura FSTX, ele sinaliza períodos a serem evitados.

            ##### TED Spread:
            Mede o risco de default bancário ao calcular a diferença entre a taxa LIBOR de três meses e os T-bills. É especialmente relevante em crises financeiras, como em 2008, quando atingiu níveis recordes.

            ##### Ativos de Risco: 
            ETFs de high-yield bonds (HYG) e moedas emergentes, como o peso mexicano (MXN), funcionam como indicadores em crises específicas. O MXN, por exemplo, serviu como proxy para ativos arriscados durante a crise europeia de 2011.

            ##### Fluxo de Ordens: 
            Mudanças abruptas no fluxo de ordens indicam que informações importantes chegaram a investidores institucionais. Isso afeta negativamente ativos de risco (ações, commodities) e positivamente ativos seguros (USD, JPY, CHF).

            ##### Indicadores Específicos:
            Preços de commodities, como petróleo e ouro, são bons preditores para pair trading entre ETFs de produtores e mineradoras. O Índice Baltic Dry também pode antecipar riscos em países exportadores.

            Apesar da eficácia desses indicadores, crises financeiras são raras, o que aumenta o risco de viés de seleção de dados em backtests. Além disso, eventos imprevisíveis, como desastres naturais, não podem ser antecipados. O fluxo de ordens, por atuar em alta frequência, é uma das ferramentas mais úteis para antecipar mudanças de mercado com precisão.

            Em resumo, combinar indicadores como VIX, TED Spread, fluxo de ordens e ativos específicos permite mitigar riscos e aumentar a eficácia de estratégias de trading. A escolha do indicador deve ser validada rigorosamente para evitar vieses e garantir sua confiabilidade.
                        
            """)
            code_3 = '''
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

plt.style.use('dark_background')
# Baixar os dados do portfólio
ticker = "^GSPC"  # Altere para o ticker desejado

data = yf.download(ticker, start="2015-01-01", end="2023-01-01")
valor_carteira = data['Close']

# Calcular o retorno diário
portfolio_returns = valor_carteira.pct_change().dropna()

# Calcular a volatilidade diária e anualizada
daily_volatility = portfolio_returns.std()
annualized_volatility = daily_volatility * np.sqrt(252)

# Função para calcular o drawdown
def calculate_drawdown(portfolio_values):
    peaks = np.maximum.accumulate(portfolio_values)
    drawdowns = (portfolio_values - peaks) / peaks
    max_drawdown = np.min(drawdowns)
    return drawdowns, max_drawdown

drawdowns, max_drawdown = calculate_drawdown(valor_carteira)

# Calcular o Sharpe Ratio
risk_free_rate = 0.02  # Suponha uma taxa livre de risco anual de 2%
daily_risk_free_rate = (1 + risk_free_rate) ** (1/252) - 1  # Ajustar para base diária
excess_returns = portfolio_returns - daily_risk_free_rate
sharpe_ratio = np.mean(excess_returns) / daily_volatility * np.sqrt(252)  # Ajustar para base anual

# Retorno final
final_return = (valor_carteira.iloc[-1] / valor_carteira.iloc[0] - 1) * 100

# Exibir os resultados
print(f"Volatilidade diária: {daily_volatility}")
print(f"Volatilidade anualizada: {annualized_volatility}")
print(f"Drawdown máximo: {max_drawdown}")
print(f"Sharpe Ratio: {sharpe_ratio}")
print(f"Retorno final: {final_return}%")

            '''
            
            st.code(code_3, language="python")

            colab_link = "https://colab.research.google.com/drive/1pjlRF6K4fteMMaeoqGqNluNaiQMO_oFU?usp=sharing"  # Coloque o link do Colab aqui
            st.markdown(f"[Clique aqui para editar no Colab]({colab_link})")


            mostrar_imagem("img/risk_ind.png", "Risk Indicators")


            st.divider()
            st.markdown("""            
            #### Stop Loss
           
            Stop loss pode ser utilizado de duas maneiras: a mais comum é para sair de uma posição existente quando o lucro/prejuízo não realizado atinge um limite negativo, permitindo reentradas futuras. A segunda, menos comum, é usar o stop loss para encerrar completamente uma estratégia caso o drawdown ultrapasse um limite, o que é raro e pouco prático. O stop loss é eficaz apenas em mercados sempre abertos, pois gaps de preços após fechamentos podem resultar em perdas maiores. Em condições extremas, como na crise de liquidez durante o flash crash de 2010, o stop loss pode falhar completamente.
            
            Para estratégias de reversão à média, o stop loss pode parecer contraditório, pois se espera que os preços voltem ao normal, mas falha ao considerar mudanças permanentes no comportamento do mercado. Caso ocorra uma mudança de regime, o stop loss pode prevenir perdas catastróficas, sendo mais útil se configurado acima do drawdown máximo do backtest. Já estratégias de momentum se beneficiam logicamente do stop loss, pois perdas indicam reversão do momento, justificando a saída ou reversão da posição.""")

        elif subsecao == "Conclusão":

            st.write("### Maximization of Long-Term Growth Rate and Risk Management")
            st.write("""
            Para maximizar o crescimento composto e gerenciar riscos em estratégias de trading, considere as seguintes abordagens:

            ### 1. Maximização da Taxa de Crescimento de Longo Prazo

            - **Uso da Alavancagem Ótima (Half-Kelly)**:
            - Se o objetivo é maximizar o patrimônio líquido no longo prazo, a alavancagem de meio-Kelly pode oferecer um equilíbrio entre risco e retorno.

            - **Distribuições de Retorno Assimétricas**:
            - Estratégias com retornos de caudas grossas (fat-tailed) devem evitar a fórmula de Kelly pura.
            - Utilize simulações de Monte Carlo para calcular a alavancagem ótima e evitar resultados extremos.

            - **Otimização Direta em Backtests**:
            - Você pode otimizar a alavancagem diretamente com base na taxa de crescimento composta dos retornos históricos.
            - Cuidado com o viés de data-snooping ao confiar exclusivamente nos backtests.

            - **Limitação de Drawdowns com CPPI**:
            - Para limitar o drawdown máximo e ainda maximizar o crescimento, utilize a técnica de Constant Proportion Portfolio Insurance (CPPI).

            ---

            ### 2. Stop Loss

            - **Estratégias de Reversão à Média**:
            - Stop loss geralmente reduz o desempenho nos backtests devido ao viés de sobrevivência.
            - Configure stop loss de forma que não sejam acionados nos backtests, prevenindo eventos de cisne negro.

            - **Estratégias de Momentum**:
            - O uso de stop loss é natural e parte lógica das estratégias de momentum.

            ---

            ### 3. Indicadores de Risco

            - **Indicadores Líderes de Risco**:
            - Considere o uso de indicadores como: VIX, TED spread, HYG, ONN/OFF, MXN.
            - Teste cuidadosamente esses indicadores para evitar viés de data-snooping.

            - **Fluxo de Ordem Negativo**:
            - Um fluxo de ordem cada vez mais negativo de ativos arriscados pode servir como um indicador de risco de curto prazo.

            ---

            ### Conclusão

            Para maximizar o crescimento composto e gerenciar riscos, é essencial equilibrar alavancagem, controle de drawdowns e uso de ferramentas como CPPI, stop loss e indicadores de risco. Testes robustos e validações rigorosas são cruciais para evitar armadilhas de viés e tomar decisões bem informadas.
            """)

# ==================== Chapter 8 - Gestão de Risco ========================

# ==================== Conclusão ========================

    elif pagina == "10 . Conclusão":

        st.title("Conclusão - Princípios Fundamentais do Trading Algorítmico")

        # Texto completo
        st.write("""
        ### 1. Estratégias Não Como Receitas, Mas Como Fundamentos
        O objetivo principal não é fornecer estratégias prontas, mas ilustrar **princípios fundamentais**:
        - **Identificar ineficiências de mercado**:
            - Regressão à média.
            - Retornos de rolagem em futuros.
            - Necessidade de rebalanceamento em ETFs alavancados.
        - A partir dessas ineficiências, criar estratégias simples e eficazes para explorá-las.

        ---

        ### 2. Abordagem Científica ao Trading Algorítmico
        A abordagem ao trading deve seguir um processo científico:
        1. **Formular hipóteses** sobre o mercado.
        2. Criar um **modelo quantitativo**.
        3. Testar o modelo em dados novos e não vistos.
        4. Identificar causas de falhas e ajustar variáveis.

        **Exemplo:** 
        - A cointegração entre GLD e GDX falhou em 2008 devido ao preço elevado do petróleo.
        - Ao adicionar o preço do petróleo como variável, o modelo voltou a funcionar.

        A investigação de **razões fundamentais** para falhas é mais eficaz do que adicionar regras ou indicadores arbitrários.

        ---

        ### 3. Juízo Subjetivo no Trading Algorítmico
        Apesar da base científica, decisões subjetivas são inevitáveis:
        - **Eventos extremos**: Confiar no modelo ou reduzir alavancagem antes de crises?
        - **Distribuição de capital**:
            - Alocar com base no portfólio total (subsidia estratégias temporariamente fracas).
            - Alocar por estratégia individual (reduz rapidamente a alocação em estratégias fracas).

        **Experiência do autor:**
        - Use alavancagem conservadora em tempos bons para evitar cortes em tempos ruins.
        - Aplique Kelly individualmente para estratégias, eliminando aquelas com baixo desempenho.

        ---

        ### 4. Mercados Não-Estacionários e Mudanças de Regime
        Diferenças entre backtest e trading ao vivo geralmente são causadas por **mudanças estruturais** no mercado, como:
        - Regulações governamentais.
        - Alterações macroeconômicas.

        Mesmo em estratégias automatizadas, os gestores desempenham um papel crucial:
        - Fazer julgamentos de alto nível sobre a validade dos modelos.

        ---

        ### 5. Superioridade de Algoritmos Sobre Julgamento Humano
        Como destacado por Daniel Kahneman:
        - Em ambientes de alta incerteza, **algoritmos superam especialistas**.
        - Mercados financeiros provavelmente seguem essa regra.

        Desenvolver estratégias simples, baseadas em fundamentos, e testá-las rigorosamente são práticas-chave para o sucesso.
        """)

# ==================== Conclusão ========================

# ==================== Referências ========================

    elif pagina == "Referências":

        st.title("Referências")

        # Texto completo
        st.write("""
                 
1. CHAN, Ernie. Algorithmic trading: winning strategies and their rationale. John Wiley & Sons, 2013.
2. https://github.com/AnjayGoel/algorithmic-trading/tree/master
3. Moskowitz, Tobias, Hua Ooi Yao, and Lasse Heje Pedersen. “Time Series Momentum.” Journal of Financial Economics 104, no. 2 (2012): 228–250.
4. Chan, Ernest P. Quantitative Trading: How to Build Your Own Algorithmic Trading Business. John Wiley & Sons, 2009.
5. Daniel, Ken, and Tobias Moskowitz. “Momentum Crashes.” Preprint, 2011. Available at www.columbia.edu/~kd2371/papers/unpublished
/mom4.pdf..
6. Hafez, Peter A., and Junqiang Xie. “Short-Term Stock Selection Using News Based Indicators,” May 15, 2012, www.ravenpack.com/research/shorttermstockselectionpaperform.htm.
7. Bollen, Johan, Huina Mao, and Xiao-Jun Zeng. “Twitter Mood Predicts the Stock Market,” 2010. Available at http://arxiv.org/pdf/1010.3003.pdf.

           
        
        """)

# ==================== Referências ========================




elif mode == "Chat":
    chat_option = st.sidebar.radio(
        "Opções de Chat:", options=["Conversar", "Configurações", "Debug"], index=0
    )

    def run_streamlit_script(path):
        try:
            runpy.run_path(path, run_name="__main__")
        except Exception as e:
            st.error(f"Erro ao executar o arquivo '{path}': {e}")

    if chat_option == "Conversar":
        run_streamlit_script("pag/chat.py")
    elif chat_option == "Configurações":
        run_streamlit_script("pag/02_Configuração.py")
    elif chat_option == "Debug":
        run_streamlit_script("pag/01_Debug.py")

