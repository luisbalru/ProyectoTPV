import json
import time
import os

class TPV():
    """Clase para el microservicio TPV"""

    def __init__(self):
        self.__gananciasDia = 0
        try:
            if os.path.exists('data/mesas.json'):
                with open('data/mesas.json', 'r') as f:
                    self.mesas = json.load(f)
            else:
                raise IOError("No se encuentra 'mesas.json'")

            if os.path.exists('data/precios.json'):
                with open('data/precios.json', 'r') as f:
                    self.precios = json.load(f)
            else:
                raise IOError("No se encuentra 'precios.json'")

            if os.path.exists('data/stock.json'):
                with open('data/stock.json', 'r') as f:
                    self.stock = json.load(f)
            if os.path.exists('data/ganancias.json'):
                with open('data/ganancias.json', 'r') as f:
                    self.ganancias = json.load(f)
            else:
                raise IOError("No se encuentra 'stock.json'")

        except IOError as fallo:
             print("Error {} leyendo *.json".format( fallo ) )

    def CuantasMesas(self):
        return len(self.mesas)

    def GetMesas(self):
        return json.dumps(self.mesas)

    #Reduce la cantidad de stock disponible
    def ReducirStock(self,nMesa):
        if len(self.mesas) > nMesa and nMesa >=0:
            self.stock["bebidas"] -= self.mesas[nMesa]["bebidas"]
            self.stock["raciones"] -= self.mesas[nMesa]["raciones"]
            self.stock["pan"] -= self.mesas[nMesa]["pan"]
            return True
        else:
            return False

    #La cantidad de mesas no varia, o estan libres(todo a 0) o estan ocupadas
    def VaciarMesa(self,nMesa):
        if len(self.mesas) > nMesa and nMesa >=0:
            self.mesas[nMesa]["bebidas"] = 0
            self.mesas[nMesa]["raciones"] = 0
            self.mesas[nMesa]["pan"] = 0
            return True
        else:
            return False

    #Añadir a la cuenta los nuevos pedidos, no se añaden mesas, las mesas
    #son las que hay, si están a 0 todos paramatros es que estan vacias
    def Apuntar(self,nMesa,bebidas=None,raciones=None,pan=None):
        if nMesa >= self.CuantasMesas(): return False
        if bebidas:
            if type(bebidas) != int: return False
            if (self.stock["bebidas"]-bebidas) < 0:
                return False
            else:
                self.mesas[nMesa]["bebidas"] += bebidas
        if raciones:
            if type(raciones) != int: return False
            if (self.stock["raciones"]-raciones) < 0:
                return False
            else:
                self.mesas[nMesa]["raciones"] += raciones
        if pan:
            if type(pan) != int: return False
            if (self.stock["pan"]-pan) < 0:
                return False
            else:
                self.mesas[nMesa]["pan"] += pan

        return True

    def ReponerStock(self,pan=0,raciones=0,bebidas=0):
        #suponiendo que no se gastan todas, se añaden a las que quedan
        if pan >= 0 and raciones >= 0 and bebidas >= 0:
            self.stock["bebidas"] += bebidas
            self.stock["raciones"] += raciones
            self.stock["pan"] += pan
            return True
        else:
            return False

    def Cuenta(self,nMesa):
        if len(self.mesas) > nMesa and nMesa >=0:
            return (self.mesas[nMesa]["bebidas"]*self.precios["bebidas"] +
            self.mesas[nMesa]["pan"]*self.precios["pan"]+
            self.mesas[nMesa]["raciones"]*self.precios["raciones"])
        else:
            return False

    def mod11_cuenta_bancaria(self,numero):
        if len(numero)!=10:
            return False
        cifras = [1,2,4,8,5,10,9,7,3,6]
        chequeo = 0
        for i in range(10):
            chequeo += int(numero[i])*cifras[i]

        chequeo = 11 - (chequeo%11)
        if chequeo == 11:
            chequeo = 0
        if chequeo == 10:
            chequeo = 1
        return chequeo

    def ValidarTarjeta(self,entidad,oficina,dc,cuenta):
        if len(entidad) != 4:
            return False
        if len(oficina) != 4:
            return False
        if len(dc) != 2:
            return False
        if len(cuenta) != 10:
            return False
        cadena = "00"+entidad+oficina
        print(cadena)
        if self.mod11_cuenta_bancaria(cadena)!=int(dc[0]):
            return False
        if self.mod11_cuenta_bancaria(cuenta) !=int(dc[1]):
            return False
        return True

    def Cobrar(self,numeroMesa,esTarjeta=False,entidad=None,oficina=None,dc=None,cuenta=None):
        if len(self.mesas) > numeroMesa and numeroMesa >=0:
            self.ReducirStock(numeroMesa)
            total = self.Cuenta(numeroMesa)
            self.VaciarMesa(numeroMesa)
            if esTarjeta:
                if self.ValidarTarjeta(entidad,oficina,dc,cuenta):
                    self.__gananciasDia += total
                    return total
                else:
                    print("Numero de tarjeta incorrecto")
                    return False
            else: #efectivo
                self.__gananciasDia += total
                return total
        else:
            return False

    #devuelve las ganancias del dia y restaura el valor de las ganancias
    def HacerCaja(self):
        fecha = time.strftime("%d/%m/%Y")
        #si la ultima fecha es la misma que la actual quiere decir que seguimos en
        #el mismo día por lo que sumamos las ganancias, no creamos un nuevo indice
        if fecha == self.ganancias[len(self.ganancias)-1]["fecha"]:
            self.ganancias[len(self.ganancias)-1]["ganancias"] += self.__gananciasDia
        else:
            self.ganancias.append({"fecha":fecha,"ganancias":self.__gananciasDia})
        self.__gananciasDia = 0
        return self.ganancias[len(self.ganancias)-1]["ganancias"]
