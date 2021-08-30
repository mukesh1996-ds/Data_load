import pandas as pd
import logging as lg

lg.basicConfig(filename="load_data.log", level=lg.DEBUG, format="%(asctime)s, %(message)s")

lg.info("This help in loading the data.")

def load_csv(filepath):
    try:
        lg.info("check for the path of data.")
        data =  []
        col = []
        checkcol = False
        with open(filepath) as f:
            for val in f.readlines():
                val = val.replace("\n","")
                val = val.split(',')
                if checkcol is False:
                    col = val
                    checkcol = True
                else:
                    data.append(val)
        df = pd.DataFrame(data=data, columns=col)
        return df
    except Exception as e:
        lg.error("The type of error occour is:",e)

