import requests
import time

url = 'https://www.nyckel.com/v1/functions/dvmz5hiywiv8pr2c/invoke'
headers = {
    'Authorization': 'Bearer ' + 'eyJhbGciOiJSUzI1NiIsInR5cCI6ImF0K2p3dCJ9.eyJuYmYiOjE2NzQ5Nzg4NTMsImV4cCI6MTY3NDk4MjQ1MywiaXNzIjoiaHR0cHM6Ly93d3cubnlja2VsLmNvbSIsImNsaWVudF9pZCI6IjFhN2xhNm05OTZ0c2N6Z3J2Y2k4bzk3cTlxMWRodDBpIiwianRpIjoiRkUxRjRFNjI4RTAxMkJERDBCQTQ0OUQwMDFFNzcyQjEiLCJpYXQiOjE2NzQ5Nzg4NTMsInNjb3BlIjpbImFwaSJdfQ.TRouSEiDXejJfd620GsFZafUKU26NFpll0R-kINEAa66wh-ExSeWxT0CYwQ35T3ClVLEmhh5RKdUEeEzHG6zcUEk6vR3RWRGnOImT6pi3WBjgyJgGopX0Gc-D36ouWDT5CC5Ktd3ZDFHPbWF3seukYH2gcU3P0n2xVEsxUykw0LB3hio3ZOwomRFx7CYX5Hgl_Yu49NnzaTyj9RP-YHzU2kjppApIt9Bhl6CIjvmsozTfRa7pFYPeSBtzgpXGxrwyb-nqPDVOXx9_gxwtGTi57WCM_JOlGEF_Q_WC1BhkhAdWZUaOV0JDAgfq2vXA9OcHizeyhH590poBOje6NgPog',
}

# HTTP request to get the image_dir
image_dir = ""
with open(image_dir, 'rb') as f:
  start = time.time()
  result = requests.post(url, headers=headers, files={'data': f})
  end = time.time()
  print(end-start)
print(result.text)







