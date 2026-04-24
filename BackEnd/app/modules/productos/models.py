from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone

if TYPE_CHECKING:
    from app.modules.productos.models import Categoria, ProductoCategoria
    from app.modules.ingredientes.models import Ingrediente, ProductoIngrediente


class ProductoCategoria(SQLModel, table=True):
    """Tabla intermedia para la relación Muchos a Muchos entre Producto y Categoria."""
    __tablename__ = "producto_categoria"

    producto_id: Optional[int] = Field(default=None, foreign_key="productos.id", primary_key=True)
    categoria_id: Optional[int] = Field(default=None, foreign_key="categorias.id", primary_key=True)

class ProductoIngrediente(SQLModel, table=True):
    __tablename__ = "producto_ingrediente"

    producto_id: Optional[int] = Field(default= None, foreign_key="productos.id", primary_key=True)
    ingrediente_id: Optional[int] = Field(default=None, foreign_key="ingredientes.id", primary_key=True)


class Producto(SQLModel, table=True):
    """Tabla productos en la base de datos."""
    __tablename__ = "productos"

    id: Optional[int] = Field(default=None, primary_key=True)
    
    nombre: str = Field(max_length=150, unique=True, index=True)
    descripcion: Optional[str] = None
    precio: float = Field(ge=0.0) 
    stock: int = Field(default=0)
    imagen_url: Optional[str] = None

    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    deleted_at: Optional[datetime] = None


    categorias: List["Categoria"] = Relationship(
        back_populates="productos", 
        link_model=ProductoCategoria
    )

    ingredientes: List["Ingrediente"] = Relationship(
        back_populates ="productos",
        link_model = ProductoIngrediente
    )