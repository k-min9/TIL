'''
1. 크롤링한 A.html를 읽고 
2. BeautifulSoup로 Parsing하여
3. 테이블을 찾고, 루프하여
4. 지정해둔 키워드가 포함된 열을 찾아
5. 특정 번째 column을 알맞게 반환하여
6. A.txt로 저장함
'''
from bs4 import BeautifulSoup

######################
filename = 'A'
######################
output_file_name = filename + ".txt"  # 출력 파일 이름

# HTML 파일 읽어오기
with open(filename+'.html', 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

# BeautifulSoup으로 HTML 파싱
soup = BeautifulSoup(html_content, 'html.parser')

# 출력할 키워드 목록 설정
target_keywords = ["키워드1", "키워드2", "키워드3", "키워드4", "없는키워드"]  # 여기에 원하는 키워드 추가

# 텍스트 파일 열고 데이터 기록하기
with open(output_file_name, 'w', encoding='utf-8') as output_file:
    for target_keyword in target_keywords:
        content_found = False
        
        # 조건(예시는 클래스)을 만족하는 모든 테이블 탐색하여 반복
        for table in soup.find_all('table', class_='wikitable limitwidth-1024'):
            for row in table.find_all('tr'):
                if target_keyword in row.get_text():
                    columns = row.find_all('td')
                    
                    # 키워드가 정확하게 일치할 때만 해당 내용을 찾음
                    if len(columns) >= 3 and columns[0].get_text().strip() == target_keyword:
                        paragraphs = columns[2].find_all('p')
                        
                        # 모든 <p> 요소의 내용을 합쳐서 하나의 문자열로 만듦
                        content = " ".join(paragraph.get_text() for paragraph in paragraphs)
                        
                        # 키워드와 내용을 '|'로 구분하여 텍스트 파일에 기록
                        output_line = f"{target_keyword}|{content}\n"
                        output_file.write(output_line)
                        content_found = True
                        break
                        
        # 키워드에 해당하는 내용이 없는 경우 "Not found" 메시지를 기록
        if not content_found:
            output_file.write(f"{target_keyword}|Not found\n")
