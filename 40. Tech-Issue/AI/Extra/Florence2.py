'''
마이크로소프트에서 배포한 OCR 까지 되는 놀라운 기술
pip install transformers
pip install einops timm
pip install requests
'''
import requests

import os
from PIL import Image
from transformers import AutoProcessor, AutoModelForCausalLM 

from unittest.mock import patch
from transformers.dynamic_module_utils import get_imports

def fixed_get_imports(filename: str | os.PathLike) -> list[str]:
    if not str(filename).endswith("modeling_florence2.py"):
        return get_imports(filename)
    imports = get_imports(filename)
    imports.remove("flash_attn")
    return imports

with patch("transformers.dynamic_module_utils.get_imports", fixed_get_imports): #workaround for unnecessary flash_attn requirement
        # model = AutoModelForCausalLM.from_pretrained("microsoft/Florence-2-base", trust_remote_code=True, cache_dir='./models/', force_download=True)
        # model = AutoModelForCausalLM.from_pretrained("microsoft/Florence-2-base", trust_remote_code=True, cache_dir='./models/', local_files_only=True)
        model = AutoModelForCausalLM.from_pretrained("microsoft/Florence-2-large", trust_remote_code=True, cache_dir='./models/', force_download=True)
        # model = AutoModelForCausalLM.from_pretrained("microsoft/Florence-2-large", trust_remote_code=True, cache_dir='./models/', local_files_only=True)  # Florence-2-base 도 있음
# processor = AutoProcessor.from_pretrained("microsoft/Florence-2-base", trust_remote_code=True, cache_dir='./models/', force_download=True)
# processor = AutoProcessor.from_pretrained("microsoft/Florence-2-base", trust_remote_code=True, cache_dir='./models/', local_files_only=True)
processor = AutoProcessor.from_pretrained("microsoft/Florence-2-large", trust_remote_code=True, cache_dir='./models/', force_download=True)
# processor = AutoProcessor.from_pretrained("microsoft/Florence-2-large", trust_remote_code=True, cache_dir='./models/', local_files_only=True)

# prompt = "<OD>"  # OBJECT DETECT
prompt = "<CAPTION>"
# prompt = "<OCR>"

# Test : 웹 이미지
# url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg?download=true"
# url = "https://upload.wikimedia.org/wikipedia/commons/2/23/The_river_effect_in_justified_text.jpg?download=true"
url = "https://i.namu.wiki/i/fxupOhyY6zM_MvbsPjCtXYDhOLX4SuoxO0Z8pQNhebRphsYF47_V2EtBrLxec1oO4LXW5nwceIcD2vx6cf7eYW_vtTMlyC3SPjutQx1-OlTwNOKQmQ3bqQJFxtlQ5NQxAGF3XL8wby6u8d0RAopaUg.webp"
# url = "https://dcimg2.dcinside.co.kr/viewimage.php?id=3fb2dc2af1da3da566bac5a6&no=63f39f2fe8d577a26fabd7e640876b305c3a6408ff5c1e1bdbd3c53484d9249711522dfa08fb7c078842078e5c82e41773a8eb42d4e72f778cf2f606e50cea36506fb2cb4a1006516f"
image = Image.open(requests.get(url, stream=True).raw)

# Test : 로컬 이미지
# url = "./image/a2.jpg"
# image = Image.open(url)

inputs = processor(text=prompt, images=image, return_tensors="pt")

generated_ids = model.generate(
    input_ids=inputs["input_ids"],
    pixel_values=inputs["pixel_values"],
    max_new_tokens=1024,
    num_beams=3,
    do_sample=False
)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=False)[0]

# parsed_answer = processor.post_process_generation(generated_text, task="<OD>", image_size=(image.width, image.height))
parsed_answer = processor.post_process_generation(generated_text, task=prompt, image_size=(image.width, image.height))

print(parsed_answer)
