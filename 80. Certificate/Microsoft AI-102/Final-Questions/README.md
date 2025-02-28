# Solution of examtopics Dumping

출처 : <https://www.examtopics.com/exams/microsoft/ai-102/>
문제수 : 333문(250228기준)

## Solving

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

## 기타

- Language Understanding
- Embedded applications : AI 기술지식 없이 build 지원
