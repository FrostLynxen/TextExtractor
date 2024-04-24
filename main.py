import cv2
import easyocr
import matplotlib.pyplot as plt

# read image
image_path = 'resources\\Hero-Image.png'
img = cv2.imread(image_path)

# text detector
reader = easyocr.Reader(['en'], gpu=False)
textInput = reader.readtext(img)

# Output
for t in textInput:
    # print(t)
    bbox, text, score = t
    print(text)

    cv2.rectangle(img, bbox[0], bbox[2], (0,255,0), 2)
    cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
