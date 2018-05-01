from utils.utils import calculaMEdiaFinal

def teste_media():
    assert calculaMEdiaFinal(10,10) == 10
    assert calculaMEdiaFinal(0,0) == 0
    assert calculaMEdiaFinal(10,5) == 8
    assert calculaMEdiaFinal(8,5) == 6.8
    assert calculaMEdiaFinal(5,5) == 5