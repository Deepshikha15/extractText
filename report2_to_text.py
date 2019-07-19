import json

from PIL import Image
import pytesseract

im = Image.open("report2.jpg")
text =pytesseract.image_to_string(im)
print(text)
result={}
result['Report2']=text

txt =json.dumps(result, indent=4)

print ( txt)
print (type(txt))

try:
    json_object = json.loads(txt)
    print ("Is valid json? true")
except ValueError as e:
    print ("Is valid json? false")
