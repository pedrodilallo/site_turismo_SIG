# Sistema Informação Gerencial para uma transportadora
## Escolha do Problema
A indústria de transporte desempenha um papel vital na economia global, garantindo o fluxo de mercadorias e serviços. As transportadoras enfrentam desafios operacionais, logísticos e econômicos complexos, que exigem abordagens inovadoras para aprimorar suas atividades e se manterem competitivas em um mercado em constante evolução. A Engenharia de Produção, com sua abordagem sistêmica e conhecimentos multidisciplinares em Pesquisa Operacional, Logística, Economia e Computação, destaca-se como uma disciplina capaz de enfrentar esses desafios por meio da construção de um sistema de informações.

Um sistema de informações bem projetado e implementado desempenha um papel crucial na resolução de problemas em uma transportadora. Ele consiste em uma infraestrutura tecnológica e processos organizacionais para coletar, armazenar, processar e disseminar informações relevantes em tempo real. Para isso será necessária a coleta sistemática de dados precisos sobre todas as atividades da transportadora, como roteirização, tempos de entrega, desempenho de motoristas e custos operacionais. Esses dados fornecem uma visão completa das operações, identificando gargalos, pontos de ineficiência e áreas que requerem melhorias.

## Descrição Detalhada do Caso
A indústria de transporte desempenha um papel vital na economia global, sendo a espinha dorsal que garante o fluxo contínuo de mercadorias e serviços em todo o mundo. No entanto, essa indústria enfrenta desafios complexos e multifacetados que afetam sua eficiência e competitividade. Problemas relacionados às operações logísticas, como o planejamento de rotas, a gestão de estoques e a coordenação de entregas, tornam-se ainda mais desafiadores em um cenário de constante evolução tecnológica e exigências crescentes dos clientes.

Além disso, questões econômicas também desempenham um papel crítico. As transportadoras enfrentam pressões para reduzir custos operacionais, ao mesmo tempo em que precisam oferecer serviços de qualidade e atender às demandas específicas dos clientes. A falta de controle adequado dos custos e receitas pode levar a margens de lucro apertadas e afetar negativamente a saúde financeira da empresa.

Nesse contexto, o sistema de informações proposto, baseado na abordagem sistêmica e conhecimentos multidisciplinares da Engenharia de Produção, surge como uma solução estratégica e inovadora para enfrentar esses desafios. Através da integração de Pesquisa Operacional, Logística, Economia e Computação, o sistema busca criar uma plataforma que permita à transportadora coletar, armazenar, processar e disseminar informações relevantes em tempo real.

A compreensão dos processos existentes é fundamental para identificar os gargalos e ineficiências no fluxo de trabalho. A coleta e análise de dados precisos sobre todas as atividades da transportadora, como roteirização, tempos de entrega, desempenho de motoristas e custos operacionais, fornecem uma visão completa das operações. Isso possibilita a identificação de áreas que requerem melhorias, a otimização das rotas de transporte e o controle eficiente dos estoques.

Um dos pontos problemáticos é a falta de informações centralizadas e integradas. Com múltiplos sistemas e fontes de dados, a tomada de decisões pode ser dificultada e a coordenação entre departamentos pode ser prejudicada. A ausência de uma visão holística das operações pode resultar em decisões subótimas e redundâncias no processo.

Outro desafio é a necessidade de melhorar a satisfação do cliente e fornecer uma experiência positiva ao longo de toda a jornada. Acompanhar o status das entregas, fornecer informações em tempo real e permitir que os clientes avaliem o serviço são aspectos cruciais para construir confiança e fidelidade com a base de clientes.

Diante desses desafios, a solução proposta tem como objetivo aumentar a eficiência operacional da transportadora, aprimorar a gestão de estoques, centralizar e integrar informações, otimizar a roteirização e aumentar a satisfação do cliente. O sistema de informações permitirá o compartilhamento transparente de dados entre os diferentes atores envolvidos, possibilitando a colaboração e a coordenação eficiente das atividades.

Ao implementar esse sistema, a transportadora terá uma visão mais precisa e abrangente de suas operações, possibilitando a identificação de oportunidades de melhoria e a adoção de estratégias mais eficazes. Isso resultará em processos mais eficientes, entregas mais rápidas, redução de custos operacionais e, ao mesmo tempo, o aumento da satisfação dos clientes.
## Levantamento e Análise dos Requisitos do Usuário
**Requisitos**

1. Atender e Registrar Pedidos dos Clientes:
   - Requisito: Esse requisito visa permitir que os clientes façam pedidos à transportadora e que esses pedidos sejam registrados para processamento posterior.
   - Ator Envolvido: Clientes
   - Interação: O ator "Clientes" interage com o caso de uso "Receber Pedidos dos Clientes", enviando seus pedidos, que são registrados pelo sistema para posterior processamento.

2. Permitir Ordens de Pedido dos Fornecedores:
   - Requisito: Esse requisito busca possibilitar que a transportadora emita ordens de pedido aos fornecedores, garantindo o suprimento adequado de materiais e produtos necessários para as operações da empresa.
   - Ator Envolvido: Fornecedores
   - Interação: Os "Fornecedores" interagem com o caso de uso "Emitir Ordens de Pedido aos Fornecedores". O sistema gera e envia as ordens de pedido aos fornecedores, garantindo o abastecimento adequado.

3. Cadastrar Fornecedores:
   - Requisito: Esse requisito consiste em permitir que a transportadora cadastre informações detalhadas sobre seus fornecedores para manter um registro organizado e atualizado dos parceiros de negócios.
   - Ator Envolvido: Funcionários
   - Interação: O ator "Funcionários" interage com o caso de uso "Cadastrar Fornecedores", inserindo os dados relevantes sobre os fornecedores no sistema.

4. Gerenciar Estoques:
   - Requisito: Esse requisito tem o objetivo de permitir o gerenciamento eficiente dos níveis de estoque da transportadora, garantindo que os produtos estejam disponíveis conforme a demanda e evitando faltas ou excessos de estoque.
   - Ator Envolvido: Funcionários
   - Interação: O ator "Funcionários" interage com o caso de uso "Atualizar Estoques", responsável por ajustar as quantidades de estoque com base nas movimentações de entrada e saída de mercadorias.

5. Auxiliar na Tomada de Decisões Logísticas:
   - Requisito: Esse requisito visa fornecer informações relevantes para apoiar as decisões estratégicas e operacionais relacionadas à logística da transportadora, visando otimizar as operações e reduzir custos.
   - Ator Envolvido: Funcionários
   - Interação: O ator "Funcionários" interage com o caso de uso "Tomar Decisões Logísticas", que disponibiliza relatórios e dados relevantes para apoiar a tomada de decisões logísticas.

6. Integrar Multi CD’s:
   - Requisito: Esse requisito envolve a integração de múltiplos Centros de Distribuição (CDs) para coordenar e utilizar eficientemente os recursos disponíveis em diferentes locais.
   - Ator Envolvido: Sistema de Roteirização
   - Interação: O caso de uso "Verificar Capacidade do CD" e "Verificar Disponibilidade de Frota" são responsáveis por verificar a capacidade de cada CD e a disponibilidade da frota para acomodar as entregas de forma eficiente.

7. Emitir Notas Fiscais:
   - Requisito: Esse requisito tem o propósito de emitir notas fiscais para documentar as transações comerciais realizadas pela transportadora.
   - Ator Envolvido: Funcionários
   - Interação: O ator "Funcionários" interage com o caso de uso "Emitir Notas Fiscais", gerando as notas fiscais para as transações comerciais realizadas.

8. Emitir Relatórios de Capacidade e Operação:
   - Requisito: Esse requisito busca fornecer relatórios detalhados sobre a capacidade dos recursos da transportadora e o desempenho das operações.
   - Ator Envolvido: Sistema de Roteirização
   - Interação: O caso de uso "Emitir Relatórios de Utilização e de Operação" gera os relatórios necessários para apresentar informações relevantes sobre a capacidade e o desempenho da operação logística.

9. Controlar os Indicadores Financeiros da Empresa:
   - Requisito: Esse requisito visa controlar e calcular os indicadores financeiros relevantes para a transportadora, auxiliando na gestão financeira eficiente.
   - Ator Envolvido: Sistema Financeiro
   - Interação: O caso de uso "Calcular Indicadores" é responsável por realizar o cálculo dos indicadores financeiros, fornecendo informações relevantes para a tomada de decisões financeiras.

10. Armazenar Dados sobre a Frota de Caminhões:
    - Requisito: Esse requisito busca manter um registro organizado dos dados da frota de caminhões da transportadora para facilitar o acompanhamento e a gestão dos veículos.
    - Ator Envolvido: Funcionários
    - Interação: O ator "Funcionários" interage com o caso de uso "Cadastrar Funcionários e Administradores", onde também são inseridos os dados dos motoristas e da frota de caminhões.

11. Permitir Avaliação Pelos Clientes:
    - Requisito: Esse requisito tem o objetivo de permitir que os clientes avaliem os serviços prestados pela transportadora, fornecendo feedback sobre a experiência de entrega.
    - Ator Envolvido: Clientes
    - Interação: Os "Clientes" interagem com o caso de uso "Avaliar Serviço", fornecendo suas avaliações sobre o serviço recebido.

12. Permitir que o Cliente Acompanhe o Produto:
    - Requisito: Esse requisito visa permitir que os clientes acompanhem o status de suas entregas, oferecendo maior transparência e satisfação ao cliente.
    - Ator Envolvido: Clientes
    - Interação: Os "Clientes" interagem com o caso de uso "Acompanhar a Entrega", permitindo-lhes acompanhar o andamento de suas entregas em tempo real.

**Diagrama de Caso de Uso (DCU)**

O Diagrama de Caso de Uso é uma poderosa ferramenta utilizada na Engenharia de Requisitos e no processo de análise e modelagem de sistemas de software. Essa representação gráfica tem como objetivo descrever de forma clara e detalhada as interações entre os atores e o sistema em questão, além de mapear as principais funcionalidades que o sistema oferece.

No contexto do projeto proposto para a transportadora, o Diagrama de Caso de Uso desempenha um papel estratégico na comunicação com os stakeholders, na identificação dos atores envolvidos e na definição clara das funcionalidades essenciais para atender às necessidades dos usuários. Essa representação visual permite uma compreensão comum entre a equipe de desenvolvimento, gerentes, clientes e outras partes interessadas, alinhando expectativas e objetivos desde o início do projeto. Por isso, segue o Diagrama de Caso de Uso proposto para a transportadora:

![Diagrama de Caso de uso](/Relatório/Semana-1/Diagramas/DCU.png)

O Diagrama de Caso de Uso apresentado é uma representação visual que descreve de forma detalhada as interações entre os atores e o sistema proposto para a transportadora, oferecendo uma visão abrangente das funcionalidades do sistema e como elas se relacionam com os usuários e demais atores envolvidos.

Os atores no diagrama são representados por ícones distintos, como "Clientes", "Administrador do Sistema", "Funcionários", "Fornecedores", "Motoristas", "Sistema de Pagamentos", "Sistema de Roteirização" e "Sistema Financeiro". Cada ator representa uma entidade externa ao sistema e desempenha um papel específico na interação com o sistema.

As funcionalidades do sistema são representadas pelos casos de uso, que são elipses no diagrama. Cada caso de uso descreve uma ação ou funcionalidade que o sistema oferece e é identificado por um nome significativo. Os casos de uso são conectados aos atores relevantes por meio de linhas, mostrando as interações e comunicações entre os atores e o sistema.

Por exemplo, o caso de uso "Receber Pedidos dos Clientes" é conectado ao ator "Clientes", indicando que os clientes interagem com o sistema para registrar seus pedidos. Isso pode envolver a utilização de um aplicativo ou plataforma online em que os clientes preencham os detalhes do pedido, como produtos desejados, endereço de entrega e informações de pagamento.

Além disso, o diagrama também mostra as relações de inclusão e extensão entre os casos de uso. A relação de inclusão é representada por uma seta pontilhada e indica que um caso de uso inclui outro caso de uso. Por exemplo, o caso de uso "Calcular Rota Otimizada" está incluído em "Confirmar Pedido", o que significa que o cálculo da rota otimizada é uma etapa essencial no processo de confirmação do pedido.

A relação de extensão é representada por uma seta tracejada e indica que um caso de uso estende outro caso de uso, ou seja, adiciona funcionalidades opcionais. Por exemplo, o caso de uso "Emitir Relatórios de Utilização e de Operação" estende o caso de uso "Registrar Histórico de Entregas", o que significa que, após o registro do histórico de entregas, o sistema pode fornecer a opção de gerar relatórios adicionais para análise e controle da operação.
