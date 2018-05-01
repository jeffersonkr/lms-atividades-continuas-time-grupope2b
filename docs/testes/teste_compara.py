from utils.utils import verificaCopia

def test_comparatexto():

    assert verificaCopia('Tassio', 'Tassio') == True
    assert verificaCopia('Tassio', 'Paulo') == False