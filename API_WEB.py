from flask import Flask,jsonify,request,Response
import sys,os.path
from flask.json import JSONEncoder
sys.path.append("src/")
from pruebas import TPV

app = Flask(__name__) #creamos la instancia
#embellecedor de JSON desactivado por defecto 
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
tpv = TPV()

@app.route("/")
def main():
    return jsonify({
    "Status": "OK",
    "ejemplos de Servicios":{
    "GetMesas":{
        "ruta":"/getMesas",
        "valor": "JSON con los apuntes de cada mesa"
    },
    "CuantasMesas":
               { "ruta": "/cuantasMesas",
                 "valor": "{ NMesa:<en mi ejemplo 4>}"},
    "Apuntar":
                {"ruta": "/apuntar?mesa=valor1<&bebidas=valor2&raciones=valor3&pan=valor4>",
                "valor": "{Apuntado: True o False}"
                },
    "Reponer":{
        "ruta":"/reponer<&bebidas=valor2&raciones=valor3&pan=valor4>",
        "valor": "{Repuesto:True o False}"
    },
    "Cobrar":{
        "ruta":"/cobrar/<mesa></esTarjeta/entidad/oficina/dc/cuenta>",
        "valor": "{Cobrado: True o False}"
    },
    "HacerCaja":{
        "ruta":"/hacer_caja",
        "valor": "{Ganancias: <ganancias del día acumuladas>}"
    }
    }
    })

    #return Response(response=ret,status=200,mimetype="application/json")

@app.route("/getMesas")
def GetMesa():
    return jsonify(tpv.GetMesas())


@app.route("/cuantasMesas")
def CuentasMesas():
    return jsonify(NMesas=tpv.CuantasMesas())

@app.route("/apuntar")
def Apuntar():
    bebidas=None
    raciones=None
    pan=None
    if request.args.get('bebidas'):
        bebidas=int(request.args.get('bebidas'))
    if request.args.get('raciones'):
        raciones=int(request.args.get('raciones'))
    if request.args.get('pan'):
        pan = int(request.args.get('pan'))
    if not request.args.get('mesa'):
        return jsonify(Error="Tiene que indicar la mesa al menos")
    else:
        mesa = request.args.get('mesa')
        return jsonify(Apuntar=tpv.Apuntar(int(mesa),bebidas,raciones,pan))

@app.route("/reponer")
def ReponerStock():
    pan=0
    raciones=0
    bebidas=0
    if request.args.get('bebidas'):
        bebidas=int(request.args.get('bebidas'))
    if request.args.get('raciones'):
        raciones=int(request.args.get('raciones'))
    if request.args.get('pan'):
        pan = int(request.args.get('pan'))
    return jsonify(Repuesto=tpv.ReponerStock(pan,raciones,bebidas))

@app.route("/cobrar/<int:mesa>/<EsTarjeta>/<entidad>/<oficina>/<dc>/<cuenta>")
@app.route("/cobrar/<int:mesa>")
def Cobrar(mesa,esTarjeta=False,entidad=None,oficina=None,dc=None,cuenta=None):
    return jsonify(Cobrado=tpv.Cobrar(mesa,esTarjeta,entidad,oficina,dc,cuenta))

@app.route("/hacer_caja")
def HacerCaja():
    return jsonify(Ganancias=tpv.HacerCaja())

@app.errorhandler(404)
def page_not_found(error):
  		return "Página no encontrada", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
