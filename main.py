#!/usr/bin/python3
import argparse
import requests
from datetime import timedelta, datetime
import pandas as pd
from pandas import json_normalize
import json

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

with open('places.json', 'r') as fp:
    loc_dict = json.load(fp)

parser = argparse.ArgumentParser(description='Place to get the data: Peninsula \n IslasBaleares \n Mallorca \n Menorca \n Ibiza \n Formentera \n Tenerife \n ElHierro \n GranCanaria \n Lanzarote-Fuerteventura \n Fuerteventura \n LaGomera \n Lanzarote \n LaPalma')
parser.add_argument('-p', '--place', type=str, required=True, help='Place to get the data: Peninsula \n IslasBaleares \n Mallorca \n Menorca \n Ibiza \n Formentera \n Tenerife \n ElHierro \n GranCanaria \n Lanzarote-Fuerteventura \n Fuerteventura \n LaGomera \n Lanzarote \n LaPalma')
parser.add_argument('-sd', '--start_date', required=True, type=lambda s: datetime.strptime(s, '%Y-%m-%d'), help='Place the start date: YYYY-MM-DD')
parser.add_argument('-ed', '--end_date', required=True, type=lambda s: datetime.strptime(s, '%Y-%m-%d'), help='Place to end date')
parser.add_argument('-o', '--opt', type=int, required=True, help='0=Consumtion, 1=Forecast')
args = parser.parse_args()

def download_data(place, start_date, end_date, opt):
    url = loc_dict['loc_dict'].get(place)[opt]
    for single_date in daterange(start_date, end_date):
        address = url + "{}".format(single_date.strftime("%Y-%m-%d"))
        try:
            r = str(requests.get(address).content)
        except:
            pass
        inicial = r.find("{")
        #Json file
        #f=open("{}.json".format(single_date.strftime("%Y-%m-%d")),"w")
        f=open("temp.json","w")
        f.write(r[inicial:-3])
        f.close()

        df = pd.read_json('temp.json')
        #print(json_normalize(df['valoresHorariosGeneracion']))
        json_normalize(df['valoresHorariosGeneracion']).to_csv("{}.csv".format(single_date.strftime("%Y-%m-%d")))


# python main.py Peninsula 2020-02-10 2020-03-05 0
# python main.py Mallorca 2020-02-10 2020-03-05 1
if __name__ == '__main__':
    try:
        download_data(args.place, args.start_date, args.end_date, args.opt)
    except IndexError:
        print("No se puede hayar")

