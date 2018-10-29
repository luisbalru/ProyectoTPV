import pytest
import sys, os.path
import json
src = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '/src/')
sys.path.append(src)
from pruebas import TPV

tpv = TPV()

def test_inicializar_correcto():
    assert isinstance(tpv, TPV), "No se ha podido inicializar"

def test_devuelve_mesas():
    assert type(tpv.GetMesas())== list, "No se han devuelto correctamente los valores"

def test_numero_correcto_mesas():
    assert tpv.CuantasMesas()==4, "Error en el numero de mesas"

def test_reduccion_correcta_stock():
    assert tpv.ReducirStock(0), "La reduccion no se realiza correctamente"
    assert tpv.ReducirStock(4)==False, "La reduccion no se realiza correctamente"

def test_vaciar_mesa():
    assert tpv.VaciarMesa(0)
    assert tpv.VaciarMesa(4)==False

def test_apuntar_correctamente():
    assert tpv.Apuntar(0,bebidas="doce")==False
    assert tpv.Apuntar(0,bebidas=300)==False
    assert tpv.Apuntar(0,raciones=2)

def test_reponer_correctamente():
    assert tpv.ReponerStock(bebidas=-1)==False
    assert tpv.ReponerStock(100,200,10)==True

def test_cuenta_correcta():
    assert tpv.Cuenta(1)==19

def test_validar_correctamente_tarjeta():
    assert tpv.ValidarTarjeta("0024","6912","50","1234567891") ==True
    assert tpv.ValidarTarjeta("1210","0418","40","1234567891") ==False

def test_cobrar():
    assert tpv.Cobrar(2)==73.5
    #Comprobar con tarjeta

def test_hacer_caja():
    #mas la mesa del test de cobrar #73.5
    tpv.Cobrar(1) #19
    tpv.HacerCaja()
    tpv.Cobrar(0) #14
    assert tpv.HacerCaja()==106.5, "Error en los calculos de las ganancias"
