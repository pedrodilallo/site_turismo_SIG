@startuml
skinparam actorStyle awesome
!theme mars
left to right direction

actor Clientes as cliente
actor "Administrador do Sistema" as sys_admin
actor Funcionários as funcionario
actor Fornecedores as fornecedores
actor Motoristas as motoristas
actor "Sistema de Pagamentos" as pagamentos
actor "Sistema de Roteirização" as roteirizador
actor "Sistema Financeiro" as financeiro

package "Registros"{
fornecedores -- (Cadastrar Clientes)
fornecedores -- (Emitir ordem do de Pedido)

funcionario -- (Atualizar Estoques)
funcionario -- (Cadastrar Fornecedores)
funcionario -- (Consultar relatórios Financeiros)

sys_admin -- (Cadastrar Novos Funcionários)
sys_admin -- (Liiberar acesso dos Funcionários)
sys_admin -- (Consultar relatórios Financeiros)
funcionario -- (Confirmar pedido)


}

package "Finanças"{
fornecedores -- (Efetuar pagamento)

pagamentos -- (Emitir Nota)
pagamentos -- (Efetuar Pagamento)
pagamentos -- (Registrar dados Financeiros)
(Emitir Nota) <.. (Efetuar Pagamento) : <<include>>

financeiro -- (Calcular Indicadores)
(Emitir Relatórios Financeiros) ..> (Calcular Indicadores) : <<extends>>

}

package "Roteirização"{
(Confirmar pedido) ..> (Calcular rota otimizada) : <<include>>

roteirizador -- (Verificar Capacidade do CD)
roteirizador -- (Verificar a Disponibilidade de frota)
roteirizador -- (Calcular rota otimizada)
roteirizador -- (Emitir Ordem de Entrega)
roteirizador -- (Emitir Relatórios de utilização e de operação)

(Calcular rota otimizada) ..> (Verificar Capacidade do CD) : <<include>>
(Calcular rota otimizada) ..> (Verificar a Disponibilidade de frota) : <<include>>

(Emitir Ordem de Entrega) ..> (Registrar Histórico de Entegas) : <<include>>
(Registrar Histórico de Entegas) <.. (Emitir Relatórios de utilização e de operação) : <<extend>>
}

package "Entrega"{
(Emitir Ordem de Entrega) ..> (Realizar a Entrega) :<<include>>
motoristas -- (Realizar a entrega)
motoristas -- (Confirmar a entrega)

cliente -- (Confirmar a entrega)
cliente -- (Acompanhar a Entrega)
cliente -- (Avaliar serviço)

(Avaliar serviço) ..> (Confirmar a entrega) : <<extends>>
(Acompanhar a Entrega)..> (Confirmar a entrega) : <<extends>>

}


@enduml
