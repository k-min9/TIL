<!-- markdownlint-disable -->
# Solution of examtopics Dumping

- 목차
  - Examtopics 333문
  - Udemy 100문
- 놓치면 안되는 주요 문제 타입
  - HOTSPOT : 드롭다운에서 선택
  - YES/NO : TF 문제
  - 3연 YES/NO : 하나의 주제에 대한 연속 YES/NO
  - DRAG-DROP : 문제가 그대로 나올 가능성이 높음.
  - NOT be able to return : Same Scenario에 관해 연속적인 질문, 답변 하면 돌아올 수 없음.
- 버리거나 없어진 타입
  - Simulation

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
21. need to add more contributors.
    1. the Access control (IAM) page for the authoring resources in the Azure portal
22. query volume steadily increased.
    1. Solution -You migrate to a Cognitive Search service that uses a higher tier. : YES!
23. DRAG-DROP
    1. Detect incoming language : Speach to Text
    2. Respond in caller's own language : Text to Speech 
24. extract data from the receipts by using Form Recognizer and the SDK with prebuilt model.
    1. FormRecognizerClient client (inference client)
    2. StartRecognizeReceiptsFromUri method (prebuilt)
25. Azure Cognitive Search : an enrichment pipeline to perform optical character recognition (OCR) and text analytics with minimize costs.
    1. a new Cognitive Services resource that uses the S0 pricing tier
26. query volume steadily increased.
    1. solution - You add indexes. : No. 문제해결도 안되고, Index는 작을수록 최적화 됨.
27. query volume steadily increased.
    1. solution - You enable customer-managed key (CMK) encryption. : No. 데이터 저장과 보호를 위한 작업
28. app1 - vm1 - vnet1 - service1 : want app1 can connect directly to service1 without routing traffic over the public internet.
    1. solution - You deploy service1 and a private endpoint to vnet1. YES! 개별비밀엔드포인트를 별개 발매해서 해결!
29. bot1 use Language Understanding resource named lu1.  ensure that bot1 adheres to the Microsoft responsible AI principle of inclusiveness.(포괄성)
    1. Direct Line Speech - 장애인도 말로 서비스 이용 가능
30. Endpoint - an app that will process incoming email and direct messages to either French or English language support teams.
    1. eastus.api.cognitive.microsoft.com - base URL of the TExt Analytics API
    2. /text/analytics/v3.1/languages - only detect language
31. indexes purchase orders by using Form Recognizer. Microsoft Power BI. minimize development effort. What should you add to the indexer?
    1. a table projection(Flow : Purchase Orders (POs) -> Form Recognizer -> OCR -> JSON (extracted info from POs) -> Shaper skill -> JSON -> Table Projection -> JSON -> Power BI)
32. query volume steadily increased.
    1. Solution-You add replicas. : YES. 리소스 제공은 항상 옳다.
33. Pass. Simulation은 시험에 나오지 않음
34. Pass. Simulation은 시험에 나오지 않음
35. Pass. Simulation은 시험에 나오지 않음
36. Pass. Simulation은 시험에 나오지 않음
37. need to build a monitoring solution. Identify staff who have removed masks or safety glasses. minimize effort, cost, 잦은 반복
    1. Face
38. index the posts of blog posts that include a category field with Azure Cognitive Search solution
    1. Retrievable: Include the category field in the search results.
    2. Searchable: Ensure that users can search for words in the category field.
    3. Facetable: Ensure that users can perform drill down filtering based on category.
39. Pass. Simulation은 시험에 나오지 않음
40. Pass. Simulation은 시험에 나오지 않음
41. Pass. Simulation은 시험에 나오지 않음
42. Pass. Simulation은 시험에 나오지 않음
43. Pass. Simulation은 시험에 나오지 않음
44. Pass. Simulation은 시험에 나오지 않음
45. Azure IoT hub : anomaly detection across multiple correlated sensors. Identify the root cause of process stops. Send incident alerts.
    1. Azure Metrics Advisor : designed for monitoring and detecting anomalies in time-series data from multiple sources. (Anomaly Detector 아님!)
46. analyzes images by using the Computer Vision API for users who are vision impaired.(시각장애인)
    1. describeImageInStreamAsync - 이미지에 대한 자세한 내용 및 설명을 위한 문장 생성
47. DRAG-DROP. export the model for use on a network that is disconnected from the internet. answer in sequence.
    1. Change Domains to General (compact) - 리소스 제한 디바이스용
    2. Retain model - 변경 도메인 내에서 효과적으로 작동하기 위한 모델 재훈련
    3. Export model - 인터넷 연결이 끊긴 네트워크에서 사용
48. Sentiment Analysis with Microsoft responsible AI principles.
    1. Add a human review and approval step before making decisions that affect the staff's financial situation.
49. ensure that only resources in vnet1 can access ta1 resource.
    1. the virtual network settings for ta1
50. monitoring system that will analyze engine sensor data(rotation speed, angle, temperature, and pressure...). must generate an alert in response to atypical values.
    1. Multivariate Anomaly Detection(다변량 이상탐지). 여러변수의 상호종속성을 고려한 이상탐지
51. identify anomalies in a time series data stream. App1 in a location that has limited connectivity. The solution must minimize costs.
    1. the Docker Engine - 다른것도 해결 가능하지만, 싸고, 애초에 기본적으로 설치해야 함.
52. HOTSPOT.
    1. Create Private Endpoint : To prevent access from the internet
    2. Use Azure Roles : To limit access to quries / ROLE에 의한 역할과 권한 정의
53. detect anomalies in sensor data from the previous 24 hours. 일괄감지.
    1. batch : scans the entire dataset, at the same time(!), for anomalies.
54. DRAG-DROP(동사 대칭중 세개 선택). Do stream, confidential documents remain on-premises. provision an Azure Cognitive Services resource. can make requests to the Language service endpoint.
    1. Provision on-premise k8 cluster that is connected to Internet : confidential doc
    2. Pull image from MCR : Azure Cognitive Services의 image는 Microsoft Container Registry에 있음
    3. Run container and specify API key and endpoint URL of Cognitive Services Services : Language service endpoint
55. HOTSPOT. REST API. sentiment analysis and OCR. have Subscription ID & Tenant ID
    1. subscriptions/8d3591aa-96b8-4737-ad09-00f9b1ed35ad : 문제에 답이 나옴. You need to use an HTTP request to create the resource in the subscription.
    2. Microsoft.CognitiveServices : Single key를 가지는 endpoint는 전부 이거라고 봐도 됨.
56. Server1에서 Anomaly Detector resource를 이용한 service를 host할때의 docker run command
    1. Billing. 서비스 사용을 인증하고 허가하기 위해 청구 정보를 제공해야 컨테이너와 Azure 서비스가 원활히 상호작용
57. Microsoft Azure Active Directory (Azure AD) 토큰.
    1. custom subdomain.
    2. private endpoint.
58. HOTSPOT. template that ensure that the resource can respond to 600 requests per minute.
    1. capacity, 100 : 600 RPM needs 100000 TPM which translates to capacity 100
59. DRAG-DROP. Sentiment Analysis API. managed feedback remains on your company’s internal network.
    1. Provision the Language service resource in Azure. : 언제나 Provision 먼저! 그래야 API Key and Endpoint URI가 생기므로 이건 공통사항이고, provision 선택지도 이것 뿐.
    2. Deploy a Docker container to an on-premises server. : can run the Sentiment Analysis API locally, ensuring that the feedback data does not leave your internal network.
    3. Identify the Language service endpoint URL and query the prediction endpoint. : querying the prediction endpoint
60. HOTSPOT. Azure OpenAI resource(AI1) with three deployments of the GPT 3.5 model.
    1. API key : Provide access to AI1 by using
    2. A Deployment Name : Connect to the deployment by using
61. bot from Microsoft Bot Framework SDK. how to validate the bot before connect?
    1. Bot Framework Emulator : Desktop att to test and debug bot locally
62. information for connecting OpenAI model(AI1)-Web APP
    1. Endpoint(URL), KEY, DEPLOYMENT NAME(AI1) : 모델정보는 deploy에 있으니 필요 없음
63. to process sensitive customer data. only specific Azure processes can access the Language service.
    1. virtual network rules
64. IoT sensor data from 100 industrial machines. have 5,000 time series datasets per minute. identify unusual values in each time series to help predict machinery failures.
    1. Azure AI Anomaly Detector
65. HOTSPOT. sentiment analysis. docker 명령어
    1. ~~/sentiment : 우선 서비스 정의
    2. https://contoso.cognitiveservices.azure.com : Billing 뒤에는 ENDPOINT
66. monitor temperature data from a data stream. generate an alert in response to atypical values.
    1. Univariate Anomaly Detection : 단변량(온도뿐) 이상 징후 탐지. 거기에 minimize development effort까지...
67. index File1.avi(20GB, OneDrive) by using the Azure Video Indexer website.
    1. From OneDrive, create a sharing link for File1.avi, and then copy the link to the Azure AI Video Indexer website. 다른 OneDrive는 잘 보면 다운로드 링크를 공유함...
68. CSAccount1(resource)-VNet1(virtual network). ensure only specific resources can access CSAccount1
    1. In VNet1, enable a service endpoint for CSAccount1 : 엔드포인트는 VNet1에만
    2. In CSAccount1, modify the virtual network settings. : 그리고 그렇게 만들어진 VNet 설정을 리소스에
69. monitor a video stream of the user and detect when the user(camera, microphone) asks an instructor a question
    1. speech-to-text in the Azure AI Speech service
70. Pipeline1 includes a step that will create an Azure AI services account. command to add a step to Pipeline1 that will identify the created Azure AI services account.
    1. az cognitiveservices account show : Azure Cognitive Services 계정의 이름, 리소스 그룹, 설정 등의 자세한 정보가 포함되어있음.
71. HOTSPOT. not consistent layout 1000 sccanned images of hand-written. for extract data, where to upload image and what model use?
    1. Azure Storage Account : image를 여기에 올리면 Azure AI Document Intelligence가 효율적으로 추출 가능. 
    2. Custom neural : 일관적이지 않은 손글씨 이미지에 사용하기 좋은 모델
72. 3연 YES/NO. code of Computer Vision client library.
    1. The code will perform face recognition.
       1. No. ComputerVisionClient은 Face Recognize라기보다는 Tags에 대한 Description
    2. The code will list tags and their associated confidence.
       1. Yes. Results.Tags를 반복하여 tag.Name과 tag.Confidence를 반복하는 문장 있음.
    3. The code will read a file from the local file system.
       1. Yes. File.OpenRead(localImage)
73. Code 고치기. 비동기(GetReadResultAsync)가 전부 읽기 전에 후행 작업 > 반복하며 상태확인
    1. Add code to verify the results.Status value.
    2. Wrap the call to GetReadResultAsync within a loop that contains a delay.
74. HOTSPOT. complete the API URL for contoso1(resource hosted in West US), to make a different size of a product photo by using the smart cropping feature.
    1. https://contoso1.cognitiveservices.azure.com : contoso1에 west-us 정보 있음
    2. generateThumbnail : smart cropping feature.
75. DRAG-DROP. Azure Video Analyzer complete URL
    1. widgets=people, keywords / controls=search
    2. showcaptions=true / captions=en-US
76. DRAG-DROP. 
    1. Change the model domain = Retail(compact)
    2. Retrain
    3. Publish
77. 3연 YES/NO. recognize employees' faces by using the Face Recognition API.
    1. YES. add_face는 face_image를 person_group의 person_object에 넣는 코드이다.
    2. YES. 다만 프리티어는 피플그룹하나에 1000명이므로 그룹id도 함께 변경해야 함
    3. YES. add_face는 하나의 사람에 대해 여러번 호출 되어 여러 얼굴 이미지를 넣을 수 있음.
78. DRAG-DROP : Custom Vision resource(acv*) dev to prod - Iteration, Update가 없는 것이 핵심!
    1. GetProjects on acvDEV
    2. ExportProjects on acvDEV
    3. ImportProjects on avcPROD
79. DRAG-DROP. Custom Vision API. recognize faults in components produced on a factory production line.(specific)
    1. Create a project
    2. Upload and tag images
    3. Train a classifier model
80. HOTSPOT. whether the images is of a cat or a dog in IOS
    1. Classification
    2. Multiclass (single tag per image)
    3. General (compact) - IOS!
81. Azure Video Analyzer for Media : videos based on who is present in the video.
    1. Create a person model and associate the model to the videos.
82. Custom Vision service to build a classifier. two metrics for evaluate
    1. recall : 재현율. 효율성 평가 지표.
    2. precision : 정밀도. 데이터 집합에서 관련 인스턴스만 올바르게 식별하는 능력 측정.
83. DRAG-DROP : api that find similar faces from an existing list.
    1. LargeFaceListId : 60000 이미지면 large
    2. matchFace : find similar face (not person!)
84. find photos of a person based on a sample image by using the Face API.
    1. findsimilars
    2. matchPerson : 아는 사람의 다른 사진 찾기 (임계값 통과 사진들 반환, matchFace는 임계값 낮더라도 닮은 얼굴의 순위를 반환)
85. 3연 YES/NO. for brand in image_analysis.brans:
    1. The code will return the name of each detected brand with a confidence equal to or higher than 75 percent.
       1. YES. confidence 0.75이상이니 75% 이상
    2. The code will return coordinates for the top-left corner of the rectangle that contains the brand logo of the displayed brands.
       1. YES. 좌상의 xy좌표에서 weight, height인 rectangle
    3. The code will return coordinates for the bottom-right corner of the rectangle that contains the brand logo of the displayed brands.
       1. NO. 좌상의 xy좌표에서 weight, height인 rectangle
86. HOTSPOT. add multiple images to a person group.
    1. Stream
    2. AddFaceFromStreamAsync
87. solution to detect faces in uploaded images fails to detect faces in blurred images and in images that contain sideways faces.
    1. change the detection model. (detection_01 to detection_02, 03 ...)
88. 9번과 중복. call the function to create a free Azure resource in the West US Azure region. to generate captions of images automatically.
    1. create_resource("res1", "ComputerVision", "F0", "westus") > 
89. 73번과 중복.
90. HOTSPOT. 목적달성을 위한 API
    1. Automatically suggest alt text for the images.
       1. https://westus.api.cognitive.microsoft.com/vision/v3.2/analyze/?visualFeatures=Adult,Description : Description 이용
    2. Detect inappropriate images and block them.
       1. https://westus.api.cognitive.microsoft.com/vision/v3.2/analyze/?visualFeatures=Adult,Description : Adult(+Description 이용)
91. OCR the sensitive documents. NOT be deployed to the public cloud.
    1. Host the Computer Vision endpoint in a container on an on-premises server. : 애저서비스엔드포인트+온프리미스
92. plan to index the collection(handwritten letters stored as JPEG files). ensure queries can be performed on the contents of the letters.
    1. OCR
93. HOTSPOT. tag the thousands of images as photographs, drawings, or clipart.
    1. Service endpoint : Computer Vision analyze image
    2. Property : imageType
94. Captures live video of exam candidates. service to validate that the subjects of the videos are real people.
    1. Call the face detection API repeatedly and check for changes to the FaceAttributes.HeadPose attribute. 움직임(HeadPose)으로 감지!
95. HOTSPOT. Facetesting Result
    1. detects face : API에도 적혀있음
    2. 797, 201 : quality high의 faceRectangle left, top 좌표
96. AI enrichment pipeline. need to index the 10GB of documents and images in the storage account. minimize how long it takes.
    1. From the Azure portal, configure parallel indexing.
97. DRAG DROP. analyze video content to identify any mentions of specific company names.
    1. Sign in to Azure Video Analyzer for Media website
    2. From Content model customization, select Brands
    3. Add specific company names to include list
98. mobile app that manages printed forms. send images of the forms directly to Forms Recognizer. image files must not be stored in the cloud.
    1. raw image binary. : to send images to the Form Recognizer API endpoint without storing them in the cloud, use RAW
99. app that generate a list of tags for uploaded images. Generate tags in a user's preferred language. Support English, French, and Spanish.
    1. Computer Vision Image Analysis. 태그를 포함한 포괄적 기능제공. 비용 도외시 최소한의 노력이므로 이게 맞음
100. 85번과 중복. 3연 YES/NO 
101. DRAG DROP. Custom Vision model that will identify defects in packaging.
     1. Project type : Object detection : 여러 객체 식별 및 위치 전송이기 때문에 Classification으로는 부족
     2. Domain : General (compact) : 제한된 장치 + 로컬
102. HOTSPOT. performance of the model
     1. The percentage of false positives : 100 - precision = 0
     2. The value for the number of true positives by the total number of true positives and false negatives : recall = 25
103. one million scanned magazine articles stored as an image file. extract text from the images.
     1. the Read API in Computer Vision : 인쇄,글쓰기 텍스트 이미지 특화     
104. First to do to index File1.avi(20GB) by using the Azure Video Indexer website.
     1. Upload File1.avi to Microsoft OneDrive. : 참고로 Azure Video Indexer website는 2GB까지 지원
105. HOTSPOT. 이미지의 모든 텍스트 추출 후 profane(불경한) 언어가 없는지 analyze
     1. Text Extraction from Images: Azure AI Computer Vision : OCR이 여기에 포함됨
     2. Profanity Check : Content Moderator
106. Categorize the image as either a photograph or a drawing. Generate a caption for the image.
     1. image type detection in Azure AI Computer Vision : 전자
     2. image descriptions in Azure AI Computer Vision : 후자 (Caption이 Description에 포함됨)
107. train a language model to recognize industry-specific terms. file format of the industry-specific terms.
     1. TXT. 언어모델 훈련에는 범용적인 파일형식 지원 
108. DRAG DROP. need to add new products to the classifie
     1. From the Custom Vision portal, open the project
     2. Upload sample images of the new products
     3. Label the sample images
     4. Retrain the model
     5. Publish the model
109. 72번과 동일. NYY.
110. 73번, 89번과 동일. 
111. HOTSPOT. Azure AI Vision API. app to identify whether an image is clipart or a line drawing.
     1. POST, imagetype
112. HOTSPOT. need to add a custom brand and logo to the indexer and configure an exclusion for the custom brand.
     1. enabled: false
113. analyze the files by using Azure AI Video Indexer. Video Indexer website에 올릴 수 있는 영상목록.
     1. File1,2,3,4 전부. WMV, AVI, MOV, MP4 전부 지원. 6시간/2GB까지 지원
114. NOT be able to return. 연락처 목록에서 정보 검색 by using an intent named FindContact. You need to implement the phrase list in Language Understanding
     1. Solution : You create a new pattern in the FindContact intent. 
        1. No(의견 갈림). intent만으로 부족하고 example utterances(예시 발화)가 필요함
115. NOT be able to return. identify species of flowers by training a Custom Vision model. receive images of new flower species and need to add the new images to the classifier.
     1. Solution : You add the new images, and then use the Smart Labeler tool.
        1. No. Smart Labeler은 기존 tag에만 활용할 수 있음.
116. NOT be able to return. 115와 같은 시나리오.
     1. Solution : You add the new images and labels to the existing model. You retrain the model, and then publish the model.
        1. Yes. 깔끔
117. NOT be able to return. 115와 같은 시나리오.
     1. Solution : You create a new model, and then upload the new images and labels.
        1. No. 기존 모델을 버리면 어떡함.
118. HOTSPOT. 코드 완성. 영어 record Lecture을 AppendToTranscriptFile(takes translated text and a language identifier) method를 이용하여, respective language로 변환
     1. ("fr", "de", "es")
     2. TranslationRecognizer
119. Custom Vision model. need to retrain model 1,000 new images that do not have any associated data.
     1. upload all the images
     2. Get suggested tags
     3. Review the suggestions and confirm the tags
120. entity to capture billing addresses.
     1. machine learned : ML Entity with Structure
121. PASS : Create a list of FileDTO와 QnADTO 하지 말 것.
     1. Call the client.Knowledgebase.CreateAsync method.
     2. Create a CreateKbDTO object.
122. HOTSPOT. The text can be in one of many languages > translate the text to a single language. text must remain within the Americas Azure geography.
     1. api-nam/translate : North America (NAM) region within the Americas Azure geography
     2. ?to=en
123. while building a conversational language understanding model how to enable active learning.
     1. Add log=true to the prediction endpoint query. : 로깅을 해야 active 학습 가능
124. 3연 YES/NO. docker command
     1. Going to http://localhost:5000/status will query the Azure endpoint to verify whether the API key used to start the container is valid.
        1. YES. 
     2. The container logging provider will write log data.
        1. NO. Log location is not mounted.
     3. Going to http://localhost:5000/swagger will provide the details to access the documentation for the available endpoints.
        1. YES.
125. 120번과 거의 동일. machine learned
126. How to upload speech samples to a Speech Studio project for use in training.
     1. Upload a .zip file that contains a collection of audio files in the .wav format and a corresponding text transcript file.
127. receive the content of a webpage, and then translate the content into Greek (el). The result will also contain a transliteration that uses the Roman alphabet.
     1. textType=html
     2. to=el
     3. toScript=Latn
128. two tools for debug the chatbot(built by Microsoft Bot Framework) endpoint remotely.
     1. Framework Emulator 
     2. ngrok
129. DRAG DROP. QnA Maker service. 비슷한 질문이 같은 답변을 해야 함.
     1. Add alternative phrasing to the QnA pair. : improve the likelihood of a match to a user query.
     2. Retrain model.
     3. Republish model.
130. NOT be able to return. 114와 같은 시나리오
     1. Solution: You create a new intent for location.
        1. No. should add these phrases as utterances under the existing FindContact intent.
131. NOT be able to return. 114와 같은 시나리오
     1. Solution: You create a new entity for the domain.
        1. No(의견 갈림). Pharase list나 pattern이어야 만족.
132. training a Language Understanding model and create the first intent. how to decrease the likelihood of a false positive.
     1. Add examples to the None intent. GetContactDetails로 분류하면 안되는 쿼리를 학습하여 false positive 감소에 기여.
133. Language Understanding model for purchasing tickets. select entity type
     1. Paris : GeographyV2 
     2. email@domain.com : Email
     3. 2 audit business : machine learned : preferred entity type for building Language Understanding (LUIS)
134. deploy an Azure resource to the East US Azure region. The resource will be used to perform sentiment analysis.
     1. B. create_resource("res1", "TextAnalytics", "S0", "eastus") : S0는 Sku에서 추론 가능
135. Language Services portal. Weather.Historic entity
     1. by month : 23(startPos)~30(endPos)번째 글자 읽으면 끝. 첫글자 0, 띄어쓰기도 한 글자.
136. Text Analytics output to Text-Category-ConfidenceScore
     1. Named Entity Recognition. 엔터티를 사람, 조직, 위치, 시간 표현, 수량, 통화 가치, 백분율 등과 같은 미리 정의된 범주로 식별하고 분류
137. Pass. Simulation은 시험에 나오지 않음
138. Pass. Simulation은 시험에 나오지 않음
139. Pass. Simulation은 시험에 나오지 않음
140. need to measure the public perception(대중의 인식) of your brand on social media by using natural language processing.
     1. Language service : sentiment service가 여기에 포함됨.
141. 122와 거의 유삿. HOTSPOT.
     1. api-nam.cognitive.microsofttranslator.com
     2. /translate?to=en
142. DataSource가 Azure 사방에 흩어져 있음.
     1. Export the data in Finance to Azure Data Lake Storage. : Finance만 혼자 cloud가 아니라 on-premises에 있음.
143. Pass. Simulation은 시험에 나오지 않음
144. Pass. Simulation은 시험에 나오지 않음
145. Language Service에서 data가 analyzed 되면, input data의 persist를 막는 법
     1. loggingOptOut : 입력 데이터가 Language 서비스에 의해 기록되거나 유지되지 않게 하여 privacy나 보안 유지
146. package for App1-Model1(identifies the intent of text input)
     1. Azure.AI.Language.Conversations : C# app을 위한 패키지로 기억하기.
147. HOTSPOT. create narration(해설) to accompany the video content. The solution must use Custom Neural Voice.
     1. Custom Neural Voice : Speech Studio portal
     2. Generating Narration : Text-to-speech
148. HOTSPOT. handling system that will receive calls from French-speaking and German-speaking callers.
     1. Capture inbound voice messages as text : Speech-to-text
     2. Replay messages in English on demand : Text-to-speech and Translator
149. convert text to speech. Support messages of up to 400 characters. Provide users with multiple voice options. 음성옵션을 제공하는 API.
     1. <https://uksouth.tts.speech.microsoft.com/cognitiveservices/voices/list>
150. chatbot. multi-turn conversations.
     1. Add follow-up prompts.

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
