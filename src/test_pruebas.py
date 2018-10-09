import pytest
from pruebas import TPV

def test_inicializar_correcto():
    tpv = TPV()
    assert isinstance(tpv, TPV), "No se ha podido inicializar"

def test_numero_correcto_mesas():
    tpv = TPV()
    assert tpv.CuentasMesas()==4, "Error en el numero de mesas"

def test_reduccion_correcta_stock():
    tpv = TPV()
    assert tpv.ReducirStock(0), "La reduccion no se realiza correctamente"
    assert tpv.ReducirStock(4)==False, "La reduccion no se realiza correctamente"

def test_vaciar_mesa():
    tpv = TPV()
    assert tpv.VaciarMesa(0)
    assert tpv.VaciarMesa(4)==False

def test_apuntar_correctamente():
    tpv = TPV()
    assert tpv.Apuntar(0,bebidas=300)==False
    assert tpv.Apuntar(0,raciones=2)

def test_reponer_correctamente():
    tpv = TPV()
    assert tpv.ReponerStock(bebidas=-1)==False
    assert tpv.ReponerStock(100,200,10)==True

def test_cuenta_correcta():
    tpv = TPV()
    assert tpv.Cuenta(1)==19

def test_validar_correctamente_tarjeta():
    tpv = TPV()
    assert tpv.ValidarTarjeta("0024","6912","50","1234567891") ==True
    assert tpv.ValidarTarjeta("1210","0418","40","1234567891") ==False

def test_cobrar():
    tpv = TPV()
    assert tpv.Cobrar(2)==True
    #Comprobar con tarjeta

def test_hacer_caja():
    tpv = TPV()
    tpv.Cobrar(2) #73.5
    tpv.Cobrar(1) #19
    assert tpv.HacerCaja()==92.5,"Error en los calculos de las ganancias"
