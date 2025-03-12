# Solution of examtopics Dumping

- 목차
  - Examtopics 333문
  - Udemy 100문

## Solving

출처 : <https://www.examtopics.com/exams/microsoft/ai-102/>
문제수 : 333문(250228기준)

1. Language Understanding
   1. (await client.Features.)AddPharseListAsync
   2. PhraselistCreateObject : C# new면 Object
2. container Deploy
   1. Select v1.1
   2. Export
   3. Run and mount
3. chatbot
   1. chit-chat, knowledge base and multilingual models > QnA Maker
   2. sentiment(감정) analysis
   3. Selects the best language model automatically > Dispatch
4. extract top-level information from the receipts
   1. Form Recognizer : 현 시점에서 시험범위 외
5. HTTP Request for OCR
   1. PUT : Azure에서 리소스 만들때 요청은 PUT
   2. CognitiveServices : 웹 API로 바로사용할 수 있는 ai 부품
6. Microsoft AI 6대 원칙
   1. fairness :  results regardless of the user's location or background.
   2. inclusiveness(포용성) : 청각, 시각, 기타 장애 있는 사람들을 위한 역량 강화
7. containerized versions of the Anomaly Detector API : 도커허브푸쉬나 이미지빌드따위 하지 않음
   1. Pull the Anomaly Detector container image.
   2. Create a custom Dockerfile
   3. Push the image to an Azure container registry.
   4. Distribute the docker run script
8. Deploy a containerized version of an Azure Cognitive Services
   1. mcr.microsoft.com/azure-cognitive-services/textanalytics/sentiment < sentiment 서비스
   2. <https://contoso.cognitiveservices.azure.com> < billing for ENDPOINT_URI
   3. Full Link  
        docker run --rm -it -p 5000:5000 --memory 8g --cpus 1 \
        mcr.microsoft.com/azure-cognitive-services/textanalytics/sentiment:{IMAGE_TAG} \
        Eula=accept \
        Billing={ENDPOINT_URI} \
        ApiKey={API_KEY}  
9. create_resource(client, "res1", "ComputerVision", "F0", "westus")
    1. client
    2. "res1" : kind
    3. "ComputerVision" : generate captions of images automatically.
    4. "westus" : region location
10. HTTP request.
    1. D. The secondary subscription key was reset. << regenerateKey, Body{"keyName": "Key2"}
11. training the model
    1. training for 50MB below, sevice for 500MB below
    2. supported type : JPG, PNG, BMP, PDF (text or scanned), or TIFF
12. enable a server-side encryption and use customer-managed keys (CMK)
    1. The index size will increase.
    2. Query times will increase.
    3. Azure Key Vault is required.
13. Microsoft AI 6대 원칙
    1. transparency(투명성) : notify users that their data has been processed by the sales system. 자신의 데이터가 어떻게 사용되고 보관되고 액세스 되는지 확인 명확해야 함
14. vm1, app1 connect directly service1
    1. No. should create a private link with private endpoint
15. What about Firewall?
    1. No. use vnet1 with private endpoint
16. public endpoint + network security group (NSG) for vnet1?
    1. No. use vnet1 with private endpoint
17. predictive maintenance.
    1. A. Anomaly Detector : identify unusual values in each time series
18. STT
    1. AudioStreamFormat.GetCompressedFormat : streaming Speech To Text
    2. SpeechRecognizer
19. QnA Maker-AppServiceplan : automatically created(memorize)
    1. Azure Cognitive Search / Q-C
    2. Azure App Service M / A-A
20. Language Understanding (LUIS) : to add more contributors to a Language Understanding (classic) resource
    1. B. the Access control (IAM) page for the authoring resources in the Azure portal

## AI-102 Azure AI Engineer 100% Original Practice Exam OCT'24

출처 : U-demy
문제수 : 100문제

1. data loss prevention in Azure
   1. restrictOutboundNetworkAccess : control the outbound network traffic
   2. approved urls to the allowedFqdnList property : control the outbound network traffic
2. monitor comments : negative posts
   1. sentiment analysis
3. Azure Key Vault : for granting secret permissions
   1. Using either Azure CLI or Azure PowerShell to assign access policies efficiently
4. customer-managed keys (CMK) instead of the default encryption method
   1. Use the Key Identifier URI value in your Azure AI services Key URI. : for encrypt and decrypt
   2. recommended to use Azure Key Vault for storing Customer Managed Keys (CMK)
   3. obtain a key from the key vault
5. pricing tier of an Azure AI Search
   1. pricing tier determines the maximum number of search units
   2. Customer-managed encryption keys are not offered on the free tier
   3. IP firewall access is not offered on the free tier
   4. query latency is higher on the storage-optimized tier than on the standard tier
6. policyRule : enforcing network traffic restrictions.
   1. Deny
   2. Microsoft.CognitiveServices/accounts/networkAcls.defaultAction
7. ensure connection is secure and does not rely on public internet routes.
   1. a private endpoint within the Azure Virtual Network
8. two features utilized by Azure AI Immersive Reader to enhance reading accessibility
   1. Translation : Different language
   2. Text-to-speech
9. OCR container : docker command

   ``` bash
   docker run --rm -it -p 5000:5000 --memory 18g --cpus 8 \
    mcr.microsoft.com/azure-cognitive-services/vision/read:3.2 \
    Eula=accept \
    Billing={ENDPOINT_URI} \
    ApiKey={API_KEY}
   ```

10. image moderation solution
    1. Image submission : step for analyze and classify the content of the images accurately
11. Generate Thumbnail : change the aspect ratio to make a thumbnail image with a specific width and height.
    1. smartCropping = True
12. Azure AI Video Indexer : detect and track the movement of a person - response JSON
    1. key : id, thumbnailID, instances
13. PersonGroups : recognition models of the Azure AI Face service "first execution"
    1. recognition _01 : default recognition model
    2. recognition _02~04 : latest model for comparison / "another execution"
14. image classification : upload and tag the images
    1. CustomVisionTrainingClient : for train and publish custom vision model
15. AI Document Intelligence service : manage your custom model order
    1. Establish your training dataset
    2. Use the Azure Blob container to upload training data.
    3. Train the model.
    4. Test the model using a dataset not used in training.
    5. Manage your custom models.
16. Azure AI Video Indexer : blocking Adult Content
    1. visualContentModeration
17. read a large number of files with high accuracy : handwritten text, some in English and some in multiple languages.
    1. Read API : OCR
18. Azure Language Detection - response JSON
    1. deteted language
       1. confidence score : 0.0~1.0
       2. iso6391name : fr, (Unknown)
       3. name : French, (Unknown)
19. Azure AI Speech
    1. No POST use CREATE
20. Language Understanding (LUIS) : step to get the container image and use it on your host computer
    1. docker pull
    2. Export the trained or published application package using the Language Understanding (LUIS)
    3. Move the package file into the required input directory on the host computer
    4. Run the container
    5. Query the container's prediction endpoint
    6. Import the endpoint logs for active learning
    7. Log user queries to enable active learning
21. multi-turn conversation : waterfall dialog or push a new instance of the referenced dialog 
    1. begin, prompt
22. ask for user input and return a result in a bot conversation
    1. Prompt dialog
23. text to speech output
    1. wav : new SpeechSynthesizer(speechConfig, audioConfig)
    2. speaker : new SpeechSynthesizer(speechConfig)
    3. in-memory stream : new SpeechSynthesizer(speechConfig, null)
24. pronunciation and volume of the speech in text-to-speech conversion
    1. SSML(Speech Synthesis Markup Language)
25. advanced algorithms for processing images and text to flag potentially offensive, dangerous, or unwanted content.
    1. Azure AI Content Safety
26. face service in Azure to identify the gender and age of individuals in a particular dataset
    1. DetectWithUrlAsync : detects faces in an image specified by a URL and returns face locations, landmarks, and attributes such as gender and age.
27. Read API (OCR) : similarity score
    1. confidence
28. image classification : determine the availability of parking spots
    1. Build an image classifier using custom vision.
    2. Create an IoT Edge module to perform the query on the device's custom vision web server.
    3. Send image classifier results to IoT Hub.
29. Enabling access to digital version of the scanned text.
    1. Azure Computer Vision API : OCR
30. scan text and detect personal data while using a custom list to enforce content policies?
    1. Azure AI Content Safety API
31. ensure compliance adherence and proper storage of ML experiment documentation.
    1. Compliance Manager : 단일 ML 문서의 complience 관리 및 보관
32. speech-to-text : multi-speakers, distingish speaker
    1. Conversation Transcription
33. Detect Language API(multiple languages) - response JSON
    1. countryHint : same or unknown 상황에 활용할 힌트(using to remove ambigue)
34. TTS(output speaker) API CALL
    1. SpeechConfig
    2. SpeechSynthesizer
35. recommendation system to personalize
    1. Azure Databricks
36. Custom Vision function : OD가 더 자세함!
    1. Image classification - Performs the application of one or more labels to an image.
    2. Object detection - Performs the application of one or more labels to an image and returns image coordinates where the applied label(s) can be found.
37. Image Analysis API v4.0.
    1. jpeg, gif, png (no pdf)
    2. less then 20MB (greater than 50 x 50 pixels and less than 16,000 x 16,000 pixels)
38. facial data into a PerGroup step
    1. declare var and helper function
    2. Authorize API Call by passing subscription ID of Faceclient
    3. Create Persongroup
    4. Create person for Persongroup
    5. Add the faces to the persons
39. image classification : categorize a collection of images.
    1. CustomVisionTrainingClient : For publishing Custom Vision REST API to upload and label the images.
40. object detection and image tagging with tight deadline
    1. You can use the [Smart Labeler feature] in Custom Vision to tag images more efficiently on a trained model with the latest iteration.
41. standard pricing tier to analyze documents which is not true
    1. low letency - synchronous
    2. large set of documents with multiple features >>> smaller, managable chunks
42. Translator service REST API Call matching
    1. EZ. Pass
43. sentimental
    1. nega+pos = mixed(!)
    2. nega+neutral = nega
    3. pos+neutral = pos
44. Definition
    1. Feature : Data attriute that is observed by system and used by system to learn(시스템이 관찰하고 학습할 데이터 속성)
    2. Intent : Action that is to be performed by the user(의도한 액션)
    3. Entity : Performs data extraction at prediction runtime from the user utterance(발화에서 데이터 추출)
45. PII detection T/F question
    1. Language Studio or REST API can be used for PII detection.
    2. Data can be submitted in an unstructured format for PII detection.
    3. Wrong.
46. Snippet Question. translator from the global translator resource.
    1. api.cognitive.microsofttranslator.com/translate
47. Snippet Question. translating the english text into German and French simultaneously.
    1. <https://api.cognitive.microsofttranslator.com/translate?api-version=3.O&from=en&to=fr&to=de>
48. In Question answering, after adding new question-and-answer pairs, what should you do to ensure their utilization?
    1. Test the system
49. In Question answering, how can you make a bot more engaging in casual conversation?
    1. By adding chit-chat
50. identify personally identifiable information (PII) within a given text
    1. Azure Content Moderator API using custom functions to anonymize this data
		```JSON
		"pii":{
			"email":[
				{
				"detected":"test@domain.com",
				"sub_type":"Regular",
				"text":"test@domain.com",
				"index":21
				}
			],
			"ipa":[
				{
				"sub_type":"IPV4",
				"text":"255.255.255.255",
				"index":27
				}
			]
		}
		```

## 기타

- Language Understanding
- Embedded applications : AI 기술지식 없이 build 지원
