import cv2
import numpy as np

from ptpy import PTPy
import sigma

import struct

camera = PTPy(extension=sigma.Sigma, idVendor=0x1003, idProduct=0xc432)

# for ope in camera.__dict__['_PTP__device_info']['OperationsSupported']:
#     try:
#         print(hex(int(ope)))
#     except:
#         print(ope)

with camera.session():

    camera.config_api()

    ret = camera.get_cam_data_group_focus()
    # ret[0].Value = 1
    camera.set_cam_data_group_focus(ret)

    # while True:
    #     c = camera.get_view_frame()
    #     frame = c['Data'][10:] # ignore top 10 byte, remain jpeg format
        
    #     img = cv2.imdecode(np.frombuffer(frame, np.uint8), cv2.IMREAD_COLOR)

    #     cv2.imshow('', img)

    #     key = cv2.waitKey(1) & 0xff
    #     if key == ord('q'):
    #         break
