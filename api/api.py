import time 
from flask import Flask, render_template, request
import json 
import werkzeug
import requests
from requests.structures import CaseInsensitiveDict
#own files and classes
from visitor_data import Visitorflow


app =  Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time':time.time()}

@app.route('/data', methods=['GET']) 
def init_data_from_swagger():

    url = ('https://besucherstromanalyse_hs.data.thethingsnetwork.org/api/v2/query?last=1d')

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "key ttn-account-v2.8Kmm3rcp_YVL4u6j7EKxubrdxzPnt9oozHqmi8nDcvE"

    req = requests.get(url, headers=headers)

    if req == {"no content"}:
        return "Error ",400 
    else: 
        pass

    #data from swagger in json format 
    data_swagger = json.loads(req.text)
    #call class and instance 
    besucher = Visitorflow()
    formated_data = besucher.get_data(data_swagger)

    #get data in arrays back
    #buffer1
    mac_buffer_1 = formated_data[0]
    wifi_counter_1 = formated_data[1]
    #buffer 2
    mac_buffer_2 = formated_data[2]
    wifi_counter_2 = formated_data[3]
    #buffer 3
    mac_buffer_3 = formated_data[4]
    wifi_counter_3 = formated_data[5]

    macs_analyzer = Visitorflow() 

    data_inside = macs_analyzer.mac_data_inside(mac_buffer_1,mac_buffer_2,mac_buffer_3)
    procent_of_visitor = macs_analyzer.mac_data_front(mac_buffer_1,mac_buffer_2,mac_buffer_3)
    data_campus = macs_analyzer.mac_data_campus(mac_buffer_1,mac_buffer_2,mac_buffer_3)

    return {"Response": 200, 
            "Message":"Data from Swagger",
            "all_visitor": data_campus[0],
            "mss1_left_side": data_campus[2],
            "mss3_right_side" : data_campus[3],
            "all_unique_macs" : data_inside[0],
            "macs_inside" : data_inside[1],
            "mss2_inside" : data_inside[2], 
            "procent_visitors" : procent_of_visitor[2]
    }


@app.route('/jsondata', methods = ['GET'])
def json_return():
    return {
        "userID":1,
        "title": ['1','2','3','4'],
        "completed":False
        }


