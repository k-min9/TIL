'''
대댓글까지는 수집해주지 않지만 기본적인 정보는 수집해줍니다.
'''
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
from dotenv import load_dotenv
load_dotenv()

# 유튜브 API 키 설정
API_KEY = os.environ.get('YOUTUBE_DATA_API_KEY')

# 유튜브 API 클라이언트 초기화
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)

def get_video_comments(video_id):
    comments = []

    # 영상 댓글 리스트 요청
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        textFormat='plainText',
    )

    while request:
        response = request.execute()

        # 댓글을 리스트에 추가
        for item in response['items']:
            author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(f'[작성자 : {author}] {comment}')

        # 다음 페이지가 있는 경우 다음 페이지로 이동
        request = youtube.commentThreads().list_next(request, response)

    return comments

def save_comments_to_file(comments, filename='comments.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for comment in comments:
            file.write(comment + '\n')

def main():
    video_id = 'YOUR_VIDEO_ID'  # 여기에 가져올 유튜브 영상의 ID를 넣어주세요
    comments = get_video_comments(video_id)

    # 댓글 출력 및 파일에 저장
    for i, comment in enumerate(comments, start=1):
        print(f'{i}. {comment}')

    save_comments_to_file(comments)

if __name__ == '__main__':
    main()
