import cv2
import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
# from tensorflow.keras.applications.mobilenet import MobileNet, preprocess_input, decode_predictions

model = ResNet50(weights='imagenet')
# model = MobileNet(weights='imagenet')

img_path = 'img.png'  
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = model.predict(x)
decoded_preds = decode_predictions(preds, top=3)[0]

print("Predictions:")
for i, pred in enumerate(decoded_preds):
    print(f"{i+1}. {pred[1]}: {round(pred[2]*100, 2)}%")

img_cv = cv2.imread(img_path)
label = decoded_preds[0][1]
cv2.putText(img_cv, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
cv2.imshow('Prediction', img_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()
