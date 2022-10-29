#USAR UM BANCO DE DADOS SEPARADO PARA DATABSE

#import pytest
#from unittest.mock import patch
#from sqlmodel import create_engine
#from car_rental import models



#PARA CADA FUNCAO ELE VAI CRIAR UM TEMORARIO, ENGINE
#@pytest.fixture(autouse=True, scope="function")
#def each_test_uses_separate_database(request):
#    tmpdir = request.getfixturevalue("tmpdir")
#    test_db = tmpdir.join("car_teste_test.db")
#    engine = create_engine(f"sqlite:///{test_db}")
#    models.SQLModel.metadata.create_all(bind=engine)
    #ELE SOBESCREVE O ENGINE DO MODEL 
#    with patch("car_rental.database.engine", engine):
        #YELD E UM RETURN
#        yield