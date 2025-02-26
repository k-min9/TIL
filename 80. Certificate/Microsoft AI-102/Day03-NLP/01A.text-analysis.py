'''
pip install azure-ai-textanalytics==5.3.0
pip install python-dotenv

엔터티(Entity) : 사람, 장소, 조직, 날짜, 숫자, 제품명 등 의미 있는 개체
'''
from dotenv import load_dotenv
import os

# import namespaces
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        # Create client using endpoint and key
        credential = AzureKeyCredential(ai_key)
        ai_client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)


        # Analyze each text file in the reviews folder
        reviews_folder = 'reviews'
        for file_name in os.listdir(reviews_folder):
            # Read the file contents
            print('\n-------------\n' + file_name)
            text = open(os.path.join(reviews_folder, file_name), encoding='utf8').read()
            print('\n' + text)

            # Get language 언어검색
            detectedLanguage = ai_client.detect_language(documents=[text])[0]
            print('\nLanguage: {}'.format(detectedLanguage.primary_language.name))


            # Get sentiment 감정평가
            sentimentAnalysis = ai_client.analyze_sentiment(documents=[text])[0]
            print("\nSentiment: {}".format(sentimentAnalysis.sentiment))


            # Get key phrases 핵심 구 판별
            phrases = ai_client.extract_key_phrases(documents=[text])[0].key_phrases
            if len(phrases) > 0:
                print("\nKey Phrases:")
                for phrase in phrases:
                    print('\t{}'.format(phrase))


            # Get entities(엔터티(-사람, 장소, 기간)를 추출)
            entities = ai_client.recognize_entities(documents=[text])[0].entities
            if len(entities) > 0:
                print("\nEntities")
                for entity in entities:
                    print('\t{} ({})'.format(entity.text, entity.category))


            # Get linked entities
            entities = ai_client.recognize_linked_entities(documents=[text])[0].entities
            if len(entities) > 0:
                print("\nLinks")
                for linked_entity in entities:
                    print('\t{} ({})'.format(linked_entity.name, linked_entity.url))



    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
    
'''
결과 정리
-------------
review1.txt

Good Hotel and staff
The Royal Hotel, London, UK
3/2/2018
Clean rooms, good service, great location near Buckingham Palace and Westminster Abbey, and so on. We thoroughly enjoyed our stay. The courtyard is very peaceful and we went to a restaurant which is part of the same group and is Indian ( West coast so plenty of fish) with a Michelin Star. We had the taster menu which was fabulous. The rooms were very well appointed with a kitchen, lounge, bedroom and enormous bathroom. Thoroughly recommended.    

Language: English

Sentiment: positive

Key Phrases:
        The Royal Hotel
        Good Hotel
        good service
        great location
        Buckingham Palace
        Westminster Abbey
        same group
        West coast
        Michelin Star
        taster menu
        enormous bathroom
        Clean rooms
        staff
        London
        UK
        stay
        courtyard
        restaurant
        part
        plenty
        fish
        kitchen
        lounge
        bedroom

Entities
        staff (PersonType)
        Royal Hotel (Location)
        London (Location)
        UK (Location)
        3/2/2018 (DateTime)
        rooms (Location)
        Buckingham Palace (Location)
        Westminster Abbey (Location)
        stay (Event)
        courtyard (Location)
        restaurant (Location)
        Indian (Skill)
        West coast (Location)
        fish (Product)
        rooms (Location)
        kitchen (Location)
        lounge (Location)
        bedroom (Location)
        bathroom (Location)

Links
        GOOD Music (https://en.wikipedia.org/wiki/GOOD_Music)
        Hotel (https://en.wikipedia.org/wiki/Hotel)
        The Royal Hotel (https://en.wikipedia.org/wiki/The_Royal_Hotel)
        London (https://en.wikipedia.org/wiki/London)
        Buckingham Palace (https://en.wikipedia.org/wiki/Buckingham_Palace)
        Westminster Abbey (https://en.wikipedia.org/wiki/Westminster_Abbey)
        India (https://en.wikipedia.org/wiki/India)
        West Coast Main Line (https://en.wikipedia.org/wiki/West_Coast_Main_Line)
        Michelin Guide (https://en.wikipedia.org/wiki/Michelin_Guide)

-------------
review2.txt

Tired hotel with poor service
The Royal Hotel, London, United Kingdom
5/6/2018
This is a old hotel (has been around since 1950's) and the room furnishings are average - becoming a bit old now and require changing. The internet didn't work and had to come to one of their office rooms to check in for my flight home. The website says it's close to the British Museum, but it's too far to walk.

Language: English

Sentiment: negative

Key Phrases:
        The Royal Hotel
        Tired hotel
        old hotel
        poor service
        United Kingdom
        room furnishings
        office rooms
        flight home
        British Museum
        London
        changing
        internet
        website
        1950

Entities
        hotel (Location)
        Hotel (Location)
        London (Location)
        United Kingdom (Location)
        5/6/2018 (DateTime)
        hotel (Location)
        since 1950 (DateTime)
        room (Location)
        now (DateTime)
        internet (Skill)
        one (Quantity)
        office rooms (Location)
        flight (Event)
        home (Location)
        British Museum (Location)

Links
        The Royal Hotel (https://en.wikipedia.org/wiki/The_Royal_Hotel)
        London (https://en.wikipedia.org/wiki/London)
        British Museum (https://en.wikipedia.org/wiki/British_Museum)

-------------
review3.txt

Good location and helpful staff, but on a busy road.
The Lombard Hotel, San Francisco, USA
8/16/2018
We stayed here in August after reading reviews. We were very pleased with location, just behind Chestnut Street, a cosmopolitan and trendy area with plenty of restaurants to choose from. The
Marina district was lovely to wander through, very interesting houses. Make sure to walk to the San Francisco Museum of Fine Arts and the Marina to get a good view of Golden Gate bridge and the city. On a bus route and easy to get into centre. Rooms were clean with plenty of room and staff were friendly and helpful. The only down side was the noise from Lombard Street so ask to have a room furthest away from traffic noise.

Language: English

Sentiment: mixed

Key Phrases:
        Golden Gate bridge  
        The Lombard Hotel   
        The Marina district 
        San Francisco Museum
        Lombard Street      
        busy road
        Chestnut Street     
        trendy area
        interesting houses  
        Fine Arts
        good view
        bus route
        down side
        Good location       
        helpful staff       
        traffic noise       
        USA
        We
        August
        reviews
        cosmopolitan        
        plenty
        restaurants
        city
        centre
        Rooms

Entities
        staff (PersonType)
        road (Location)
        Lombard Hotel (Location)
        San Francisco (Location)
        USA (Location)
        8/16/2018 (DateTime)
        August (DateTime)
        Chestnut Street (Location)
        restaurants (Location)
        Marina district (Location)
        houses (Location)
        San Francisco Museum of Fine Arts (Location)
        Marina (Location)
        Golden Gate bridge (Location)
        city (Location)
        centre (Location)
        Rooms (Location)
        staff (PersonType)
        Lombard Street (Address)
        room (Location)

Links
        Lombardy (https://en.wikipedia.org/wiki/Lombardy)
        Hotel (https://en.wikipedia.org/wiki/Hotel)
        San Francisco (https://en.wikipedia.org/wiki/San_Francisco)
        Chestnut Street (Philadelphia) (https://en.wikipedia.org/wiki/Chestnut_Street_(Philadelphia))
        Marina District, San Francisco (https://en.wikipedia.org/wiki/Marina_District,_San_Francisco)
        Museum of Fine Arts, Boston (https://en.wikipedia.org/wiki/Museum_of_Fine_Arts,_Boston)
        Golden Gate Bridge (https://en.wikipedia.org/wiki/Golden_Gate_Bridge)
        Room (https://en.wikipedia.org/wiki/Room)
        Lombard Street (San Francisco) (https://en.wikipedia.org/wiki/Lombard_Street_(San_Francisco))

-------------
review4.txt

Very noisy and rooms are tiny
The Lombard Hotel, San Francisco, USA
9/5/2018
Hotel is located on Lombard street which is a very busy SIX lane street directly off the Golden Gate Bridge. Traffic from early morning until late at night especially on weekends. Noise would not be so bad if rooms were better insulated but they are not. Had to put cotton balls in my ears to be able to sleep--was too tired to enjoy the city the next day. Rooms are TINY. I picked the room because it had two queen size beds--but the room barely had space to fit them. With family of four in the room it was tight. With all that said, rooms are clean and they've made an effort to update them. The hotel is in Marina district with lots of good places to eat, within walking 
distance to Presidio. May be good hotel for young stay-up-late adults on a budget


Language: English

Sentiment: mixed

Key Phrases:
        two queen size beds
        busy SIX lane street
        Golden Gate Bridge
        The Lombard Hotel
        Lombard street
        San Francisco
        early morning
        cotton balls
        Marina district
        good places
        walking distance
        late adults
        good hotel
        rooms
        USA
        Traffic
        night
        weekends
        Noise
        ears
        city
        TINY
        space
        family
        effort
        lots
        Presidio
        young
        budget

Entities
        rooms (Location)
        Lombard Hotel (Location)
        San Francisco (Location)
        USA (Location)
        9/5/2018 (DateTime)
        Hotel (Location)
        Lombard street (Address)
        SIX (Quantity)
        Golden Gate Bridge (Location)
        Traffic (Skill)
        early morning until late at night (DateTime)
        weekends (DateTime)
        rooms (Location)
        cotton balls (Product)
        the next day (DateTime)
        Rooms (Location)
        room (Location)
        two (Quantity)
        beds (Product)
        room (Location)
        four (Quantity)
        room (Location)
        rooms (Location)
        hotel (Location)
        Marina district (Location)
        Presidio (Location)
        adults (PersonType)

Links
        Lombard, Illinois (https://en.wikipedia.org/wiki/Lombard,_Illinois)
        Hotel (https://en.wikipedia.org/wiki/Hotel)
        San Francisco (https://en.wikipedia.org/wiki/San_Francisco)
        Lombard Street (San Francisco) (https://en.wikipedia.org/wiki/Lombard_Street_(San_Francisco))
        Golden Gate Bridge (https://en.wikipedia.org/wiki/Golden_Gate_Bridge)
        Traffic (https://en.wikipedia.org/wiki/Traffic)
        Noise rock (https://en.wikipedia.org/wiki/Noise_rock)
        Room (https://en.wikipedia.org/wiki/Room)
        Marina District, San Francisco (https://en.wikipedia.org/wiki/Marina_District,_San_Francisco)
        Presidio of San Francisco (https://en.wikipedia.org/wiki/Presidio_of_San_Francisco)
        May (https://en.wikipedia.org/wiki/May)

-------------
review5.txt

Un hôtel agréable
L'Hotel Buckingham, Londres, UK
J’adore cet hôtel. Le personnel est très amical et les chambres sont confortables.

Language: French

Sentiment: positive

Key Phrases:
        hôtel agréable
        L'Hotel Buckingham
        Londres
        UK
        personnel
        chambres

Entities
        hôtel (Location)
        Hotel Buckingham (Location)
        Londres (Location)
        UK (Location)
        hôtel (Location)
        personnel (PersonType)
        amical (Skill)
        chambres (Location)

Links
        United Nations (https://en.wikipedia.org/wiki/United_Nations)
        L'Hôtel (https://en.wikipedia.org/wiki/L'Hôtel)
        Buckingham (https://en.wikipedia.org/wiki/Buckingham)
        London (https://en.wikipedia.org/wiki/London)
        United Kingdom (https://en.wikipedia.org/wiki/United_Kingdom)
'''