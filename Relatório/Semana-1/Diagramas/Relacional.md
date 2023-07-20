@startuml

left to right direction

class Cliente {
  E-mail_cliente (PK)

  Nome
  Idade
  Genero
  Endereco
     Rua 
     Bairro
     Cidade
     Estado
}


class Cidade {
  ID_cidade (PK)
  Nome
  Estado
}


class Hotel {
  ID_hotel (PK)

  Nome
  ID_cidade (FK)
  Dados_modelo
  Preco_diaria
  Endereco
}


class Restaurante {
  ID_restaurante (PK)

  Nome
  ID_cidade (FK)
  Dados_modelo
  ticket_medio
}


class Atracao {
  ID_atracao (PK)

  Nome
  ID_cidade (FK)
  Preco_atracao
  Endereco
}


class Rotas {
  ID_rota (PK)

  ID_cidade (FK)
  ID_hotel (FK)
  ID_restaurante (FK)
  Lucro
  Duracao
}


class RelatorioRotas {
  ID_relatorio_rota (PK)

  Data_inicial
  Data_final
  Data_emissao
  Estatistica_rotas
  Lucro_total
}


class Feedbacks {
  ID_feedback (PK)

  E-mail_cliente (FK)
  Data
}

class RelatorioFeedbacks {
  ID_relatorio_feedback (PK)

  Data_inicial
  Data_final
  Data_emissao
  Estatistica_feedback
  Lucro_total
}

class AdministradorSistema {
  ID_admin (PK)

  Nome
  Cargo
}

Cidade --{ Cliente
Rotas --{ Cliente
Feedbacks --{ Cliente

Hotel --{ Cidade
Atracao --{ Cidade
Restaurante --{ Cidade

Rotas --{ Hotel
Rotas --{ Atracao
Rotas --{ Restaurante

RelatorioRotas --{ Rotas
RelatorioFeedbacks --{ Feedbacks

AdministradorSistema --{ RelatorioRotas

AdministradorSistema --{ RelatorioFeedbacks

@enduml