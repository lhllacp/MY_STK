from multiprocessing import pool

from CommonAPI.StockInfo import get_A_stock_code_dict, stock_real_time_data


class StockMinuteData(object):
    