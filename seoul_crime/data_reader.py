import pandas as pd
import numpy as np
import json
import googlemaps

class DataReader:
    def __init__(self):
        self.context_ =None
        self.fname_=None

    @property
    def context(self)->str:
        return self.context_
    @context.setter
    def context(self,context):
        self.context_=context

    @property
    def fname(self) -> str:
        return self.fname_

    @fname.setter
    def fname(self, fname):
        self.fname_ = fname

    def new_file(self)->str:
        return self.context_+self.fname_
    def csv_to_dframe(self)->object:
        file=self.new_file()
        return pd.read_csv(file, encoding='UTF-8', thousands=',')

    def xls_to_dframe(self,header,usecols)->object:
        file=self.new_file()
        return pd.read_excel(file,encoding='UTF-8',header=header,usecols=usecols)

    def json_load(self):
        file=self.new_file()
        return json.load(open(file,encoding='UTF-8'))

    def create_gmaps(self):
        gmaps= googlemaps.Client(key='')
        return

