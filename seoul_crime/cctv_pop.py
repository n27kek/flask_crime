import numpy as np
import pandas as pd
from seoul_crime.data_reader import DataReader
'''
population_in_seoul.xls(['자치구', '계', '계.1', '계.2', '65세이상고령자'], dtype='object')
cctv_in_seoul.csv(['기관명', '소계', '2013년도 이전', '2014년', '2015년', '2016년'], dtype='object')
'''


class CCTVModel:
    def __init__(self):
        self.dr=DataReader()

    def hook_process(self):
        print('--------1.CCTV 파일로 DF 생성 --------------')
        self.get_cctv()

    def get_cctv(self):
        self.dr.context='./data/'
        self.dr.fname='cctv_in_seoul.csv'
        cctv=self.dr.csv_to_dframe()
        self.dr.fname='population_in_seoul.xls'
        pop=self.dr.xls_to_dframe(2,'B,D,G,J,N')

        print(cctv.columns)

