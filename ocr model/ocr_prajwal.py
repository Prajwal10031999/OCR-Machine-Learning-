import cv2
import numpy as np
import requests
import io
import json

img = cv2.imread("harry.jpg")

#ocr
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".jpg", img, [1,90])
file_bytes = io.BytesIO(compressedimage)

result = requests.post(url_api, files = {"harry.jpg": file_bytes}, data = {"apikey" : "enter free api key"})

result = result.content.decode()
result = json.loads(result)

text_detected = result.get("ParsedResults")[0].get("ParsedText")
print(text_detected)

cv2.imshow("Img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 