import urllib.request
import zipfile
import os
from tqdm import tqdm

url = 'https://huggingface.co/mingu4969/windows-archive-dist/resolve/main/assets.zip?download=true'
save_path = 'assets.zip'
extracted_path = 'assets'

# Check if the file already exists and delete it
if os.path.exists(save_path):
    os.remove(save_path)
    print(f'Deleted existing file: {save_path}')

# Download the file with a progress bar
with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc='Downloading') as t:
    urllib.request.urlretrieve(url, save_path, reporthook=lambda blocknum, blocksize, total_size: t.update(blocksize))

print(f'Downloaded: {url} => {save_path}')

# Extract the zip file
with zipfile.ZipFile(save_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_path)

print(f'Extracted: {save_path} => {extracted_path}')

# Delete the zip file
os.remove(save_path)
print(f'Deleted: {save_path}')

# Wait for user input
input('작업 종료... Press Enter to exit.')
