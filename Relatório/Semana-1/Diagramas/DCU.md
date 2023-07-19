@startuml
skinparam actorStyle awesome
!theme mars
left to right direction
actor "Clientes" as cliente
actor "Administrador do Sistema" as sys_admin

cliente -- (Realizar cadastro)




package "Otimização dos Roteiros"{
actor "Sistema de Otimização" as  otimizador


(Otimizar rotas) -- otimizador 


    package "Coleta dos Dados"{
        actor "Sistema de Coleta de dados" as coletador
        actor "API do Google sobre as cidades" as API   

        cliente -- (Selecionar cidades ou atrações do roteiro da API)
        (Selecionar cidades ou atrações do roteiro da API) ..> (Otimizar rotas): <<include>>
        (Solicitar a API do Google para Coletar Dados sobre as Cidades) ..> (Enviar dados sobre as cidades) : <<incude>>
        coletador -- (Solicitar a API do Google para Coletar Dados sobre as Cidades)
        coletador -- (Registrar Rotas Já Otimizadas em uma Base de Dados)
        coletador -- (Formatar e Computar os Dados Adquiridos)
        API -- (Enviar dados sobre as cidades)
        API -- (Disponibilizar informações sobre as cidades)
        (Disponibilizar informações sobre as cidades) <.. (Selecionar cidades ou atrações do roteiro da API) : <<include>>
        (Otimizar rotas) ..> (Registrar Rotas Já Otimizadas em uma Base de Dados) : <<include>>
        (Registrar Rotas Já Otimizadas em uma Base de Dados) <.. (Consultar Relatórios sobre as Rotas) : <<extends>>

    }
(Registrar Rotas Já Otimizadas em uma Base de Dados) <.. (Elaborar Relatórios Sobre Rotas):<<include>>
(Elaborar Relatórios Sobre Rotas) <.. (Consultar Relatórios sobre as Rotas): <<extends>> 
(Elaborar Relatórios Sobre Rotas) -- otimizador

}



(Consultar Relatórios sobre as Rotas) -- sys_admin




(Realizar cadastro) <.. (Selecionar cidades ou atrações do roteiro da API) : <<extends>>
(Enviar dados sobre as cidades) ..> (Formatar e Computar os Dados Adquiridos) : <<include>>


package "Feedbacks"{
actor "Sistema de Feedback" as feedback

(Enviar Feedbacks) ..> (Armazenar dados do Feedback) : <<include>>
(Elaborar Relatório sobre Feedbacks) <.. (Consultar Relatórios sobre os Feedbacks) : <<include>>
cliente -- (Enviar Feedbacks)
feedback -- (Armazenar dados do Feedback)
(Consultar Relatórios sobre os Feedbacks) -- sys_admin
feedback -- (Elaborar Relatório sobre Feedbacks)



}



@enduml
