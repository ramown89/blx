# APP BLX

App para anúncio e vendas de produtos na vizinhança(no seu bairro ou povoado)

## Funcionalidades

- Qualquer pessoa poderá anunciar produtos
- Qualquer pessoa poderá fazer pedidos dos produtos anunciados
- Uma pessoa tem:
  - nome
  - telefone
- Um produto tem:
  - nome
  - detalhamento
  - preço
  - disponível
  - fotos (?)
- Um pedido tem:
  - Produto
  - Pessoa que está pedindo
  - Quantidade
  - Local de entrega
  - Entrega ou retirada
  - observações (sabor, horário de entrega, troco, ...)
- Cada usuário terá uma lista de pedidos recebidos(minhas vendas) e pedidos feitos(minhas compras)
- O pedido deverá ser aceito pelo vendedor
- O comprador poderá acompanhar seus pedidos
  - status (feito, aceito)

##Arquitetura e ferramentas
- Python + FastAPI + Poetry
- Será uma API REST
- Banco de Dados: postgres e/ou MongoDB(firebase firestore)
- Docker para o Postgress
- MVC
- DDD e Arquitetura Limpa (Clean Arch.)
