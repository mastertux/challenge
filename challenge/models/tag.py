from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from challenge.db.base_class import Base


association_table = Table(
    "users_tags",
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)


class Tag(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    users = relationship("User", secondary=association_table, backref="tags")
