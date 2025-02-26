'''
env 추가항목
QA_PROJECT_NAME=LearnFAQ
QA_DEPLOYMENT_NAME=production

pip install python-dotenv
pip install azure-ai-language-questionanswering

기술자료를 FAQ로 만들고 질문 답변 솔루션 만들기
'''
from dotenv import load_dotenv
import os

# import namespaces
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient

def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')
        ai_project_name = os.getenv('QA_PROJECT_NAME')
        ai_deployment_name = os.getenv('QA_DEPLOYMENT_NAME')

        # Create client using endpoint and key
        credential = AzureKeyCredential(ai_key)
        ai_client = QuestionAnsweringClient(endpoint=ai_endpoint, credential=credential)


        # Submit a question and display the answer
        user_question = ''
        while user_question.lower() != 'quit':
            user_question = input('\nQuestion:\n')
            response = ai_client.get_answers(question=user_question,
                                            project_name=ai_project_name,
                                            deployment_name=ai_deployment_name)
            for candidate in response.answers:
                print(candidate.answer)
                print("Confidence: {}".format(candidate.confidence))
                print("Source: {}".format(candidate.source))



    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()

'''
예상질답

Question:
What is a learning path?
Learning paths are collections of training modules that are organized around specific roles (like developer, architect, or system admin) or technologies (like Azure Web Apps, Power BI, or Xamarin.Forms). When you finish a learning path, you've gained a new understanding of different aspects of the technology or role you're studying. You also get an achievement trophy!
Confidence: 1.0
Source: https://learn.microsoft.com/en-us/training/support/faq?pivots=general
'''