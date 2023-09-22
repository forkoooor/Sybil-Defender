from sqlalchemy import Integer, Numeric, Column, String
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from src.database.controller import get_async_session, engine

load_dotenv()

Base = declarative_base()


class Interactions(Base):
    __tablename__ = "interactions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String, unique=False)


class Transfer(Base):
    __tablename__ = "transfers"
    tx_hash = Column(String, primary_key=True)
    sender = Column(String)
    receiver = Column(String)
    amount = Column(Numeric)
    gas_price = Column(Numeric)
    timestamp = Column(Integer)


class ContractTransaction(Base):
    __tablename__ = "contract_transactions"
    tx_hash = Column(String, primary_key=True)
    sender = Column(String)
    contract_address = Column(String)
    amount = Column(Numeric)
    timestamp = Column(Integer)
    data = Column(String)


class SuspiciousCluster(Base):
    __tablename__ = "suspicious_clusters"
    id = Column(Integer, primary_key=True, autoincrement=True)
    cluster_id = Column(Integer, nullable=False)
    address = Column(String, nullable=False)

    def __init__(self, cluster_id, address):
        self.cluster_id = cluster_id
        self.address = address

    def __repr__(self):
        return (
            f"<SuspiciousCluster(cluster_id={self.cluster_id}, address={self.address})>"
        )


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("database initialized")