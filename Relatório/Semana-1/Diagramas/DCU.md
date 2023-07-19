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
coletador -- (Formatar e Computar os Dados Adquiridos)


feedback -- (Receber Feedbacks)
feedback -- (Elaborar Relatório sobre Feedbacks)

API -- (Enviar dados sobre as cidades)

sys_admin -- (Consultar Relatórios sobre as Rotas)

(Receber Cidades ou Atrações de Interesse dos Clientes) -- otimizador 
(Otimizar Rotas) -- otimizador 
(Executar Pedidos de Otimização) -- otimizador 
(Verificar Satisfação das Restrições) -- otimizador 
(Receber Rotas Otimizadas) <.. (Otimizar Rotas) : <<include>>
(Enviar Feedbacks) --> (Receber Feedbacks) : include
(Receber Feedbacks) ..> (Elaborar Relatório sobre Feedbacks) : <<extends>>
(Elaborar Relatório sobre Feedbacks) ..> (Consultar Relatórios sobre as Rotas) : <<extends>>
(Consultar Relatórios sobre as Rotas) ..> (Elaborar Relatório sobre Feedbacks) : <<include>>
(Cadastro de Novos Clientes) ..> (Enviar Cidades ou Atrações) : <<extends>>
(Enviar dados sobre as cidades) ..> (Formatar e Computar os Dados Adquiridos) : <<include>>
(Enviar Cidades ou Atrações) -->  (Receber Cidades ou Atrações de Interesse dos Clientes) : <<include>>
(Acessar a API do Google para Coletar Dados sobre as Cidades) ..> (Enviar dados sobre as cidades) : <<incude>>




@enduml
