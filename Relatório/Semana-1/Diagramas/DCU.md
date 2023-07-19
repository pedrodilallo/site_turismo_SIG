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

cliente -- (Realizar cadastro)


package "Coleta dos Dados"{
cliente -- (Selecionar cidades ou atrações do roteiro na API)

coletador -- (Solicitar a API do Google para Coletar Dados sobre as Cidades)
coletador -- (Registrar Rotas Já Otimizadas em uma Base de Dados)
coletador -- (Formatar e Computar os Dados Adquiridos)
API -- (Enviar dados sobre as cidades)
API -- (Disponibilizar informações sobre as cidades)
(Disponibilizar informações sobre as cidades) <.. (Selecionar cidades ou atrações do roteiro) : <<include>>



}


package "Otimização dos Roteiros"{
cliente -- (Solicitar Rotas Otimizadas)
(Otimizar rotas) -- otimizador 
(Solicitar Rotas Otimizadas) ..> (Otimizar rotas) : <<include>>
(Selecionar cidades ou atrações do roteiro) ..> (Otimizar rotas): <<include>>
(Solicitar a API do Google para Coletar Dados sobre as Cidades) ..> (Enviar dados sobre as cidades) : <<incude>>


}



sys_admin -- (Consultar Relatórios sobre as Rotas)




(Realizar cadastro) <.. (Selecionar cidades ou atrações do roteiro na API) : <<extends>>
(Enviar dados sobre as cidades) ..> (Formatar e Computar os Dados Adquiridos) : <<include>>


package "Feedbacks"{

(Enviar Feedbacks) ..> (Receber Feedbacks) : <<include>>
(Receber Feedbacks) <.. (Elaborar Relatório sobre Feedbacks) : <<extends>>
(Elaborar Relatório sobre Feedbacks) ..> (Consultar Relatórios sobre as Rotas) : <<extends>>
cliente -- (Enviar Feedbacks)
feedback -- (Receber Feedbacks)
feedback -- (Elaborar Relatório sobre Feedbacks)



}



@enduml
