from seoul_crime.cctv_pop import CCTVModel


class Controller:
    def __init__(self):
        self.cctv_=CCTVModel()

    def execute(self):
        cctv=self.cctv_
        cctv.hook_process()
