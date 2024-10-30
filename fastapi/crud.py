from models import User
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select

class CRUD:
    async def get_all(self, async_session: async_sessionmaker[AsyncSession]):
        async with async_session() as session:
            statement = select(User).order_by(User.id)
            result = await session.execute(statement)
            
            return result.scalars()
        
    async def add(self, async_session:async_sessionmaker[AsyncSession],user:User):
        async with async_session() as session:
            session.add(user)
            await session.commit()
            
    async def get_by_id(self, async_session:async_sessionmaker[AsyncSession],user_id:int):
        async with async_session() as session:
            user_id = int(user_id)
            statement = select(User).filter(User.id == user_id)
            result = await session.execute(statement)
            
            return result.scalars().one()
            
    async def update(self, async_session:async_sessionmaker[AsyncSession],user_id, data):
        async with async_session() as session:
            user_id = int(user_id)
            statement = select(User).filter(User.id == user_id)
            result = await session.execute(statement)
            
            user = result.scalars().one()
            
            user.user_name = data['user_name']
            
            await session.commit()
            return user
            
    async def delete(self, async_session:async_sessionmaker[AsyncSession],user:User):
        async with async_session() as session:
            await session.delete(user)
            await session.commit()