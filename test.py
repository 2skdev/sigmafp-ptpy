import requests
import json

ret = requests.post(
    'http://127.0.0.1:10080/api/cam_data_group1_dummy',
    json={'Aperture': 0}
)
print(ret.content)
