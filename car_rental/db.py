from sqlmodel import Session, create_engine

from car_rental import models
from car_rental.config import settings

# Ao inves de passar a string passamos o a conf que esta no settings.toml

# Para usar esse parametro tem que importar o config.py onde possui uma implementacao usando o Dynaconf
engine = create_engine(settings.development.url, echo=False)  # NEW

# Ou pode passar a url direto
# engine = create_engine("sqlite:///car.db", echo=False)
models.SQLModel.metadata.create_all(engine)


# NEW
def get_session():
    return Session(engine)
