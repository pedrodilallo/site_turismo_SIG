@startuml
skinparam actorStyle awesome
!theme mars
left to right direction

actor "Clientes" as cliente
actor "API do Google sobre as cidades" as API
actor "Sistema de Otimização" as  otimizador
actor "Administrador do Sistema" as sys_admin
actor "Sistema de Feedback" as feedback
actor "Sistema de Coleta de dados" as coletador

package "Coleta dos Dados"{
cliente -- (Selecionar cidades ou atrações do roteiro na API)

coletador -- (Solicitar a API do Google para Coletar Dados sobre as Cidades)
coletador -- (Registro de Rotas Já Otimizadas em uma Base de Dados)
coletador -- (Formatar e Computar os Dados Adquiridos)
API -- (Enviar dados sobre as cidades)
API -- (Disponibilizar Cidades disponíveis)
(Disponibilizar Cidades disponíveis) <.. (Selecionar cidades ou atrações do roteiro na API) : <<include>>


}


cliente -- (Cadastrar Cliente)
cliente -- (Enviar Feedbacks)
cliente -- (Solicitar Rotas Otimizadas)

feedback -- (Receber Feedbacks)
feedback -- (Elaborar Relatório sobre Feedbacks)


sys_admin -- (Consultar Relatórios sobre as Rotas)

(Receber Cidades ou Atrações de Interesse dos Clientes) -- otimizador 
(Otimizar Rotas) -- otimizador 
(Executar Pedidos de Otimização) -- otimizador 
(Verificar Satisfação das Restrições) -- otimizador 
(Solicitar Rotas Otimizadas) ..> (Otimizar Rotas) : <<include>>



(Enviar Feedbacks) ..> (Receber Feedbacks) : <<include>>
(Receber Feedbacks) <.. (Elaborar Relatório sobre Feedbacks) : <<extends>>

(Elaborar Relatório sobre Feedbacks) ..> (Consultar Relatórios sobre as Rotas) : <<extends>>
(Cadastrar Cliente) <.. (Selecionar cidades ou atrações do roteiro na API) : <<extends>>

(Enviar dados sobre as cidades) ..> (Formatar e Computar os Dados Adquiridos) : <<include>>
(Selecionar cidades ou atrações do roteiro na API) ..>  (Receber Cidades ou Atrações de Interesse dos Clientes) : <<include>>

(Receber Cidades ou Atrações de Interesse dos Clientes) ..> (Otimizar rotas): <<include>>

(Solicitar a API do Google para Coletar Dados sobre as Cidades) ..> (Enviar dados sobre as cidades) : <<incude>>




@enduml
