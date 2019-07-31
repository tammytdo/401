import pytest
from app import create_app, db
from config import Config
from app.models import Chocolate, Brand


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite://"

@pytest.fixture
def client():

    # wave hand over this for now
    app = create_app(TestConfig)
    app_context = app.app_context()
    app_context.push()
    db.create_all()

    with app.test_client() as client:
        yield client

    db.session.remove()
    db.drop_all()
    app_context.pop()

# @pytest.fixture
# def sample_chocolate(client):
#     chocolate = Chocolate(name="Dark Chocolate")
#     db.session.add(chocolate)
#     db.session.commit()
#     return chocolate

# @pytest.fixture
# def sample_brand(sample_chocolate):
#     brand = Brand(name="Kit Kat", chocolate=sample_chocolate)
#     db.session.add(brand)
#     db.session.commit()
#     return brand

# @pytest.fixture
# def sample_brand2(client):
#     brand = Brand(name="Lindt")
#     db.session.add(brand)
#     db.session.commit()
#     return brand