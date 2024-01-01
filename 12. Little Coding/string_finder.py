# input.txt를 읽고 특정 단어를 포함한 문장만 걸러 output.txt를 만드는 파일
def filter_lines(input_file_path, output_file_path, keywords):
    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()

        filtered_lines = [line for line in lines if any(keyword in line for keyword in keywords)]

        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write('\n'.join(filtered_lines))  # 각 줄을 개행 문자로 구분하여 작성

        print('Finsihed')
    except:
        print('Failed')

if __name__ == "__main__":
    input_path = "input.txt"  # 입력 파일 경로
    output_path = "output.txt"  # 출력 파일 경로
    search_keywords = ["단어1", "단어2"]  # 찾고자 하는 단어들

    filter_lines(input_path, output_path, search_keywords)
