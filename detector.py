from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials

from PIL import Image, ImageDraw, ImageFont
import numpy as np

ENDPOINT = "PASTE_YOUR_CUSTOM_VISION_TRAINING_ENDPOINT_HERE"
prediction_key = "PASTE_YOUR_CUSTOM_VISION_PREDICTION_SUBSCRIPTION_KEY_HERE"
prediction_resource_id = "PASTE_YOUR_CUSTOM_VISION_PREDICTION_RESOURCE_ID_HERE"
publish_iteration_name = 'PASTE_YOUR_CUSTOM_VISION_Iteration_NAME'  #e.g. 'Iteration1'
image_filename = "PASTE_LOCATION_OF_FILE"
image_save_localisation = "PASTE_YOUR_FINAL_LOCATION"
treshold = 0.8

prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

with open(image_filename, "rb") as image_contents:
    results = predictor.detect_image(
        project_id, publish_iteration_name, image_contents.read())

    bounding_boxes= []
    for prediction in results.predictions:
        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))
        if(prediction.probability > 0.80):
            bounding_boxes.append((prediction.bounding_box, prediction.probability))

    img = Image.open(image_contents)
    font = ImageFont.truetype("arial.ttf", 15)
    draw = ImageDraw.Draw(img)
    for b_box, pred in bounding_boxes:
        top_left = (b_box.left* img.width, b_box.top* img.height) 
        bottom_right = ((b_box.left + b_box.width)*img.width, (b_box.top + b_box.height)* img.height)
        draw.rectangle([top_left, bottom_right], outline="black",  width=3)
        draw.text((top_left[0], top_left[1]-20), str(np.round(pred,2)*100),(0,0,0), font=font)
    img.show()
    img.save(image_save_localisation)