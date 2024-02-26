from PIL import Image, ImageDraw
import os 

input_folder = "input_266px" # 입력 이미지가 있는 폴더
output_folder = "output_256px_circle"  # 결과 이미지 저장 폴더

# 만약 output 폴더가 없다면 생성
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# 원하는 크기
output_size = (128, 128)

# 입력 폴더의 모든 PNG 파일 가져오기
for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        input_image_path = os.path.join(input_folder, filename)
        output_image_path = os.path.join(output_folder, filename)

        # 이미지 열기
        image = Image.open(input_image_path)

        # 사이즈 축소
        new_size = (image.width // 2, image.height // 2)
        image = image.resize(new_size)

        # 입력 이미지를 원형으로 자르기
        width, height = image.size
        new_size = min(width, height, 128)
        left = (width - new_size) / 2
        top = (height - new_size) / 2
        right = (width + new_size) / 2
        bottom = (height + new_size) / 2
        image = image.crop((left, top, right, bottom))

        # 원형 마스크 생성
        mask = Image.new("L", image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, new_size, new_size), fill=255)

        # 이미지를 원형 마스크를 기반으로 자르기
        result = Image.new("RGBA", output_size)
        result.paste(image, mask=mask)

        # 원하는 크기로 이미지 크롭
        # result = result.resize(output_size, Image.LANCZOS)

        # 결과 이미지 저장
        result.save(output_image_path, "PNG")

print("전 공정 완료")
