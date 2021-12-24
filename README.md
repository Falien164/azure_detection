# azure_detection
Kidney glomeruli detection on Azure Cloud

### Requirements
```
azure-cognitiveservices-vision-customvision
PIL
Numpy
```
### How to use
Detector.py is endpoint application and firstly it's necessary to publish trained model on page customVision.ai. Next step is to set key and other variables in detector.py like:
```
ENDPOINT = "PASTE_YOUR_CUSTOM_VISION_TRAINING_ENDPOINT_HERE"
prediction_key = "PASTE_YOUR_CUSTOM_VISION_PREDICTION_SUBSCRIPTION_KEY_HERE"
prediction_resource_id = "PASTE_YOUR_CUSTOM_VISION_PREDICTION_RESOURCE_ID_HERE"
publish_iteration_name = 'PASTE_YOUR_CUSTOM_VISION_Iteration_NAME'  #e.g. 'Iteration1'
image_filename = "PASTE_LOCATION_OF_FILE"
image_save_localisation = "PASTE_YOUR_FINAL_LOCATION"
```


### Results 
First image is from quick test from customVision.ai website. Next two are from app.

<img src="https://github.com/Falien164/azure_detection/blob/main/images/quick_test_1.png" width="400" height="400">
<img src="https://github.com/Falien164/azure_detection/blob/main/images/output.png" width="400" height="400">
<img src="https://github.com/Falien164/azure_detection/blob/main/images/output2.png" width="400" height="400">
