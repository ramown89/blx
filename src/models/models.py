from pydantic import BaseModel

from typing import Optional, List

class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    meus_produtos: List[Produto]
    minhas_vendas: List[Pedido]
    minhas_compras: List[Pedido]

class Produto(BaseModel):
    id: Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = True
    local: str
    observacao: Optional[str] = ''
