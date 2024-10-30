from db import Base
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__='usuario'
    
    id : Mapped[int] = mapped_column(primary_key=True)
    user_name : Mapped[str] = mapped_column(nullable=False)
    
    
    