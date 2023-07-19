@startuml
skinparam actorStyle awesome
!theme mars
left to right direction

actor "Clientes" as cliente
actor "API do Google sobre as cidades" as API
actor "Sistema de Otimização" as  otimizador
actor "Administrador do Sistema" as sys_admin
actor "Sistema de Feedback" as feedback
actor "Sistema de Log In" as login
actor "Sistema de Coleta de dados" as coletador

cliente -- (Cadastro de Novos Clientes)
cliente -- (Enviar Cidades ou Atrações)
cliente -- (Enviar Feedbacks)
cliente -- (Receber Rotas Otimizadas)



login   --   (Cadastro de Novos Clientes)
coletador -- (Acessar a API do Google para Coletar Dados sobre as Cidades)
coletador -- (Registro de Rotas Já Otimizadas em uma Base de Dados)

feedback -- (Receber Feedbacks)
feedback -- (Elaborar Relatório sobre Feedbacks)

API -- (Enviar dados sobre as cidades)

(Receber Cidades ou Atrações de Interesse dos Clientes) -- otimizador 
(Otimizar Rotas) -- otimizador 
(Executar Pedidos de Otimização) -- otimizador 
(Verificar Satisfação das Restrições) -- otimizador 
(Registro de Rotas Já Otimizadas em uma Base de Dados) -- otimizador 
(Receber Rotas Otimizadas) <-- (Otimizar Rotas) : <<include>>
(Enviar Feedbacks) --> (Receber Feedbacks) : include
(Receber Feedbacks) --> (Elaborar Relatório sobre Feedbacks) : <<extends>>
(Elaborar Relatório sobre Feedbacks) --> (Consultar Relatórios sobre as Rotas) : <<extends>>
(Consultar Relatórios sobre as Rotas) --> (Elaborar Relatório sobre Feedbacks) : <<include>>

(Enviar dados sobre as cidades) --> (Enviar dados sobre atrações) : <<include>>
(Enviar dados sobre as cidades) --> (Enviar dados sobre hotéis) : <<include>>
(Enviar dados sobre as cidades) --> (Enviar dados sobre restaurantes) : <<include>>

(Acessar a API do Google para Coletar Dados sobre as Cidades) --> (Enviar dados sobre as cidades) : <<incude>>

(Enviar dados sobre atrações) --> (Formatar e Computar os Dados Adquiridos) : <<include>>
(Enviar dados sobre hotéis) --> (Formatar e Computar os Dados Adquiridos) : <<include>>
(Enviar dados sobre restaurantes) --> (Formatar e Computar os Dados Adquiridos) : <<include>>

coletador -- (Formatar e Computar os Dados Adquiridos)

(Enviar Cidades ou Atrações) -->  (Receber Cidades ou Atrações de Interesse dos Clientes) : <<include>>

sys_admin -- (Consultar Relatórios sobre as Rotas)


@enduml
