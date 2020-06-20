# ree_data

ree_data permite descargar los datos en formato ".csv" Red Electrica de España (REE) desde la web https://demanda.ree.es/visiona/seleccionar-sistema 

## Requisitos

    pip install urllib3
    pip install pandas

## Lugares disponibles
* Peninsula
* IslasBaleares
* Mallorca
* Menorca
* Ibiza
* Formentera
* Tenerife
* ElHierro
* GranCanaria
* Lanzarote-Fuerteventura
* Fuerteventura
* LaGomera
* Lanzarote
* LaPalma

## Parámetros requeridos
La funcion permite usar cuatro parametros:
* Lugar.
* Fecha de inicio. (Formato: YYYY MM DD)
* Fecha final. (Formato: YYYY MM DD)
	### Parametro opcional
	* Si opt = 0 (default), La tabla a descargar contiene la siguiente cabecera:
		* ts: Hora.
		* dem: Demanda real.
		* car: Carbón.
		* die: Motores diesel.
		* gas: Turbina de gas.
		* cc: Ciclo combinado.
		* cb: Enlace peninsular.
		* fot: Solar fotovoltaica.
		* tnr: Resto reg. esp.
		* trn: Solar térmica.
		* eol: Eólica.
		* emm: Enlace Mallorca-Menorca
		* emi: Enlace Mallorca-Ibiza
		* otrRen: Otras renovables.
		* resid: Residuos.
		* genAux: Generación auxiliar.
		* cogen: Cogeneración.
		* eif: Enlace Ibiza-Formentera
	* Si opt = 1:
		* ts: Hora.
		* pro: Demanda programada.
		* pre: Demanda prevista.
## Uso
**Para obtener el detalle de la generación de energías:**

    > python main.py Peninsula 2020-02-01 2020-02-05 0
    o
    > python main.py Peninsula 2020-02-01 2020-02-05
**Para obtener el detalle de la demanda de las energías:**

    > python main.py Peninsula 2020-02-01 2020-02-05 1
