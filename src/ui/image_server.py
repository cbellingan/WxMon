import pandas as pd
import matplotlib.pyplot as plt
import http.server
from http import HTTPStatus
import time
import socketserver
from dao.mysql import DB
import config


class Data():
    @staticmethod
    def last(x):
        # Aggregaion function that returns the last value
        return x.iloc[-1]

    @staticmethod
    def trend(x):
        # Aggregation function that returns the trend based on a threshold
        thresh = 0.2
        change = abs(x.iloc[-1] - x.iloc[-2])
        if x.iloc[-1] - x.iloc[-2] > thresh:
            return f'▲ {change:.2f}'
        elif x.iloc[-1] - x.iloc[-2] < -thresh:
            return f'▼ {change:.2f}'
        else:
            return '-'

    def gen_image_file(self):
        cnx = DB(config=config.MySqlDb).connection()
        df = pd.read_sql('select * from fulldata where ts > now() - interval 4 day order by ts asc', cnx, parse_dates='ts', index_col='ts')
        fig, ax = plt.subplots(2,1, figsize=(13, 8))
        df.groupby('host').Temp_F.plot(grid=True)
        data = df.groupby('host').agg({'Temp_C': [Data.last], 'Temp_F': [min, max, Data.last, Data.trend]}).reset_index()
        bbox=[0, 0, 1, 1]
        ax[0].table(cellText=data.values, colLabels=data.columns, bbox=bbox)
        ax[0].axis('off')
        ax[0].title.set_text(time.ctime())
        file_name = '/tmp/latest.png'
        fig.savefig(file_name)
        return file_name



class WebHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        file_name = Data().gen_image_file()
        self.send_response(HTTPStatus.OK)
        self.send_header('content-type', 'image/png')
        self.end_headers()
        with open(file_name, 'rb') as file_handle:
            self.wfile.write(file_handle.read())


def main():
    PORT_NUMBER = 8080
    with socketserver.TCPServer(("", PORT_NUMBER), WebHandler) as httpd:
        print("serving at port", PORT_NUMBER)
        httpd.serve_forever()


if __name__ == '__main__':
    main()