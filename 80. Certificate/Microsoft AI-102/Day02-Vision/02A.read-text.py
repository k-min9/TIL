'''
이미지에서 텍스트 읽기
1: Use Read API for image (Lincoln.jpg)
2: Read handwriting (Note.jpg)
'''
from dotenv import load_dotenv
import os
import time
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt

# import namespaces
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

        # Authenticate Azure AI Vision client
        cv_client = ImageAnalysisClient(
            endpoint=ai_endpoint,
            credential=AzureKeyCredential(ai_key)
        )
        

        # Menu for text reading functions
        print('\n1: Use Read API for image (Lincoln.jpg)\n2: Read handwriting (Note.jpg)\nAny other key to quit\n')
        command = input('Enter a number:')
        if command == '1':
            image_file = os.path.join('images','Lincoln.jpg')
            GetTextRead(image_file)
        elif command =='2':
            image_file = os.path.join('images','Note.jpg')
            GetTextRead(image_file)
                

    except Exception as ex:
        print(ex)

def GetTextRead(image_file):
    print('\n')

    # Open image file
    with open(image_file, "rb") as f:
            image_data = f.read()

    # Use Analyze image function to read text in image
    result = cv_client.analyze(
        image_data=image_data,
        visual_features=[VisualFeatures.READ]
    )

    # Display the image and overlay it with the extracted text
    if result.read is not None:
        print("\nText:")
    # Prepare image for drawing
    image = Image.open(image_file)
    fig = plt.figure(figsize=(image.width/100, image.height/100))
    plt.axis('off')
    draw = ImageDraw.Draw(image)
    color = 'cyan'

    for line in result.read.blocks[0].lines:
        # Return the text detected in the image
        print(f"  {line.text}")    

        drawLinePolygon = True

        r = line.bounding_polygon
        bounding_polygon = ((r[0].x, r[0].y),(r[1].x, r[1].y),(r[2].x, r[2].y),(r[3].x, r[3].y))

        # Return the position bounding box around each line
        print("   Bounding Polygon: {}".format(bounding_polygon))       


        # Return each word detected in the image and the position bounding box around each word with the confidence level of each word
        for word in line.words:
            r = word.bounding_polygon
            bounding_polygon = ((r[0].x, r[0].y),(r[1].x, r[1].y),(r[2].x, r[2].y),(r[3].x, r[3].y))
            print(f"    Word: '{word.text}', Bounding Polygon: {bounding_polygon}, Confidence: {word.confidence:.4f}")


        # Draw word bounding polygon
        drawLinePolygon = False
        draw.polygon(bounding_polygon, outline=color, width=3)

        # Draw line bounding polygon
        if drawLinePolygon:
            draw.polygon(bounding_polygon, outline=color, width=3)
    
    # Save image
    plt.imshow(image)
    plt.tight_layout(pad=0)
    outputfile = 'text.jpg'
    fig.savefig(outputfile)
    print('\n  Results saved in', outputfile)

    

if __name__ == "__main__":
    main()

'''
출력 예시
Text:
  IN THIS TEMPLE
   Bounding Polygon: ((328, 171), (477, 169), (477, 184), (328, 186))
    Word: 'IN', Bounding Polygon: ((328, 171), (342, 171), (342, 187), (328, 187)), Confidence: 0.9930
    Word: 'THIS', Bounding Polygon: ((357, 171), (397, 170), (397, 185), (357, 186)), Confidence: 0.9910
    Word: 'TEMPLE', Bounding Polygon: ((407, 170), (474, 170), (474, 184), (407, 185)), Confidence: 0.9930
  AS IN THE HEARTS OF THE PEOPLE
   Bounding Polygon: ((240, 193), (564, 188), (564, 203), (240, 210))
    Word: 'AS', Bounding Polygon: ((241, 194), (262, 194), (262, 210), (241, 211)), Confidence: 0.9950
    Word: 'IN', Bounding Polygon: ((270, 193), (284, 193), (284, 210), (270, 210)), Confidence: 0.9980
    Word: 'THE', Bounding Polygon: ((298, 193), (332, 192), (332, 208), (298, 209)), Confidence: 0.9930
    Word: 'HEARTS', Bounding Polygon: ((340, 192), (410, 191), (410, 207), (340, 208)), Confidence: 0.9940
    Word: 'OF', Bounding Polygon: ((420, 190), (444, 190), (444, 206), (420, 206)), Confidence: 0.9930
    Word: 'THE', Bounding Polygon: ((452, 190), (487, 189), (487, 205), (452, 206)), Confidence: 0.9930
    Word: 'PEOPLE', Bounding Polygon: ((495, 189), (562, 188), (562, 204), (495, 205)), Confidence: 0.9960
  FOR WHOM HE SAVED THE UNION
   Bounding Polygon: ((237, 214), (568, 208), (569, 224), (237, 231))
    Word: 'FOR', Bounding Polygon: ((238, 214), (271, 213), (271, 231), (237, 231)), Confidence: 0.9950
    Word: 'WHOM', Bounding Polygon: ((281, 213), (339, 212), (339, 229), (281, 230)), Confidence: 0.9880
    Word: 'HE', Bounding Polygon: ((355, 212), (378, 212), (378, 228), (354, 229)), Confidence: 0.9980
    Word: 'SAVED', Bounding Polygon: ((388, 212), (441, 211), (440, 227), (388, 228)), Confidence: 0.9940
    Word: 'THE', Bounding Polygon: ((455, 211), (491, 210), (490, 226), (455, 227)), Confidence: 0.9930
    Word: 'UNION', Bounding Polygon: ((501, 210), (560, 209), (559, 225), (500, 226)), Confidence: 0.9970
  THE MEMORY OF ABRAHAM LINCOLN
   Bounding Polygon: ((226, 235), (575, 229), (576, 245), (226, 252))
    Word: 'THE', Bounding Polygon: ((228, 235), (260, 235), (260, 252), (228, 252)), Confidence: 0.9980
    Word: 'MEMORY', Bounding Polygon: ((268, 235), (349, 234), (349, 250), (268, 251)), Confidence: 0.9960
    Word: 'OF', Bounding Polygon: ((358, 234), (382, 234), (381, 250), (357, 250)), Confidence: 0.9990
    Word: 'ABRAHAM', Bounding Polygon: ((389, 233), (473, 232), (472, 248), (389, 249)), Confidence: 0.9960
    Word: 'LINCOLN', Bounding Polygon: ((488, 231), (570, 229), (570, 245), (487, 247)), Confidence: 0.9940
  IS ENSHRINED FOREVER
   Bounding Polygon: ((288, 255), (515, 253), (516, 268), (288, 271))
    Word: 'IS', Bounding Polygon: ((288, 256), (302, 256), (302, 272), (288, 272)), Confidence: 0.9960
    Word: 'ENSHRINED', Bounding Polygon: ((311, 256), (416, 255), (417, 270), (311, 272)), Confidence: 0.9930
    Word: 'FOREVER', Bounding Polygon: ((431, 255), (510, 253), (511, 268), (431, 270)), Confidence: 0.9950
'''