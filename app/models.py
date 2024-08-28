from typing import List, Optional
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Nonprofit(Base):

    __tablename__ = "nonprofit"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nonprofit_name: Mapped[str]  
    description: Mapped[Optional[str]]
    demand: Mapped[List["Resource"]] = relationship(back_populates="nonprofit")
    

class Resource(Base):

    __tablename__ = "resource"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    item: Mapped[str]  
    description: Mapped[Optional[str]]
    quantity: Mapped[int] = mapped_column(default=1)
    last_updated: Mapped[str] = mapped_column(server_default=func.now(), onupdate=func.now())
    
    non_profit: Mapped[Nonprofit] = relationship(back_populates="demand")