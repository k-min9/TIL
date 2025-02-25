'''
이미지 인식 및 표시 SDK 후 jpg 저장

python image-analysis.py images/street.jpg
python image-analysis.py images/person.jpg
python image-analysis.py images/building.jpg
'''
from dotenv import load_dotenv
import os
from PIL import Image, ImageDraw
import sys
from matplotlib import pyplot as plt
from azure.core.exceptions import HttpResponseError
import requests

# Import namespaces
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

def main():
    global cv_client

    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')
        
        # Get image
        image_file = 'images/street.jpg'
        if len(sys.argv) > 1:
            image_file = sys.argv[1]

        with open(image_file, "rb") as f:
            image_data = f.read()

        
        # Authenticate Azure AI Vision client
        cv_client = ImageAnalysisClient(
            endpoint=ai_endpoint,
            credential=AzureKeyCredential(ai_key)
        )
        
        # Analyze image
        AnalyzeImage(image_file, image_data, cv_client)
        
    except Exception as ex:
        print(ex)


def AnalyzeImage(image_filename, image_data, cv_client):
    print('\nAnalyzing image...')

    try:
        # Get result with specified features to be retrieved
        result = cv_client.analyze(
            image_data=image_data,
            visual_features=[
                VisualFeatures.CAPTION,
                VisualFeatures.DENSE_CAPTIONS,
                VisualFeatures.TAGS,
                VisualFeatures.OBJECTS,
                VisualFeatures.PEOPLE],
)
        
    except HttpResponseError as e:
        print(f"Status code: {e.status_code}")
        print(f"Reason: {e.reason}")
        print(f"Message: {e.error.message}")

    # Display analysis results
    # Get image captions
    if result.caption is not None:
        print("\nCaption:")
        print(" Caption: '{}' (confidence: {:.2f}%)".format(result.caption.text, result.caption.confidence * 100))
    '''
    caption 결론 예시
    
    Caption:
        Caption: 'a man walking a dog on a leash on a street' (confidence: 82.05%)
    '''

    # Get image dense captions
    if result.dense_captions is not None:
        print("\nDense Captions:")
        for caption in result.dense_captions.list:
            print(" Caption: '{}' (confidence: {:.2f}%)".format(caption.text, caption.confidence * 100))
    '''
    dense_captions 결론 예시
    
    Dense Captions:
        Caption: 'a man walking a dog on a leash on a street' (confidence: 82.05%)
        Caption: 'a man walking on a street' (confidence: 69.03%)
        Caption: 'a yellow car on the street' (confidence: 78.17%)
        Caption: 'a black dog walking on the street' (confidence: 75.33%)
        Caption: 'a blurry image of a blue car' (confidence: 82.01%)
        Caption: 'a yellow taxi cab on the street' (confidence: 72.42%)
    '''

    # Get image tags
    if result.tags is not None:
        print("\nTags:")
        for tag in result.tags.list:
            print(" Tag: '{}' (confidence: {:.2f}%)".format(tag.name, tag.confidence * 100))
    '''
    tags(추천캡션) 결론 예시    
    
    Tags:
        Tag: 'outdoor' (confidence: 99.87%)
        Tag: 'land vehicle' (confidence: 99.02%)
        Tag: 'vehicle' (confidence: 98.89%)
        Tag: 'building' (confidence: 98.55%)
        Tag: 'road' (confidence: 95.98%)
        Tag: 'wheel' (confidence: 95.14%)
        Tag: 'street' (confidence: 94.71%)
        Tag: 'person' (confidence: 93.01%)
        Tag: 'clothing' (confidence: 91.19%)
        Tag: 'taxi' (confidence: 90.95%)
        Tag: 'car' (confidence: 84.01%)
        Tag: 'dog' (confidence: 82.68%)
        Tag: 'yellow' (confidence: 77.08%)
        Tag: 'walking' (confidence: 74.11%)
        Tag: 'city' (confidence: 64.80%)
        Tag: 'woman' (confidence: 57.53%)
    '''
    
    # Get objects in the image
    if result.objects is not None:
        print("\nObjects in image:")

        # Prepare image for drawing
        image = Image.open(image_filename)
        fig = plt.figure(figsize=(image.width/100, image.height/100))
        plt.axis('off')
        draw = ImageDraw.Draw(image)
        color = 'cyan'

        for detected_object in result.objects.list:
            # Print object name
            print(" {} (confidence: {:.2f}%)".format(detected_object.tags[0].name, detected_object.tags[0].confidence * 100))

            # Draw object bounding box
            r = detected_object.bounding_box
            bounding_box = ((r.x, r.y), (r.x + r.width, r.y + r.height)) 
            draw.rectangle(bounding_box, outline=color, width=3)
            plt.annotate(detected_object.tags[0].name,(r.x, r.y), backgroundcolor=color)

        # Save annotated image
        plt.imshow(image)
        plt.tight_layout(pad=0)
        outputfile = 'objects.jpg'
        fig.savefig(outputfile)
        print('  Results saved in', outputfile)
    '''
    Objects(이미지에서 개체 감지 및 찾기) 결론 예시  
    
    Objects in image:
        car (confidence: 72.40%)
        taxi (confidence: 77.00%)
        person (confidence: 78.10%)
        dog (confidence: 54.40%)   
    '''

    # Get people in the image
    if result.people is not None:
        print("\nPeople in image:")

        # Prepare image for drawing
        image = Image.open(image_filename)
        fig = plt.figure(figsize=(image.width/100, image.height/100))
        plt.axis('off')
        draw = ImageDraw.Draw(image)
        color = 'cyan'

        for detected_people in result.people.list:
            # Draw object bounding box
            r = detected_people.bounding_box
            bounding_box = ((r.x, r.y), (r.x + r.width, r.y + r.height))
            draw.rectangle(bounding_box, outline=color, width=3)

            # Return the confidence of the person detected
            print(" {} (confidence: {:.2f}%)".format(detected_people.bounding_box, detected_people.confidence * 100))

        # Save annotated image
        plt.imshow(image)
        plt.tight_layout(pad=0)
        outputfile = 'people.jpg'
        fig.savefig(outputfile)
        print('  Results saved in', outputfile)
    '''
    people(이미지에서 사람 감지 및 찾기) 결론 예시  
    
    People in image:
        {'x': 241, 'y': 109, 'w': 155, 'h': 399} (confidence: 94.99%)
        {'x': 396, 'y': 264, 'w': 23, 'h': 58} (confidence: 24.93%)
        {'x': 699, 'y': 262, 'w': 20, 'h': 33} (confidence: 22.45%)
        {'x': 138, 'y': 230, 'w': 28, 'h': 31} (confidence: 6.96%)
        {'x': 129, 'y': 188, 'w': 15, 'h': 26} (confidence: 1.09%)
        {'x': 146, 'y': 188, 'w': 16, 'h': 25} (confidence: 1.02%)
        {'x': 405, 'y': 263, 'w': 15, 'h': 28} (confidence: 0.96%)
        {'x': 164, 'y': 187, 'w': 17, 'h': 25} (confidence: 0.84%)
        {'x': 176, 'y': 187, 'w': 13, 'h': 25} (confidence: 0.45%)
        {'x': 139, 'y': 186, 'w': 42, 'h': 29} (confidence: 0.19%)
        {'x': 510, 'y': 262, 'w': 17, 'h': 10} (confidence: 0.12%)
        {'x': 247, 'y': 247, 'w': 141, 'h': 121} (confidence: 0.11%)
    '''

if __name__ == "__main__":
    main()
