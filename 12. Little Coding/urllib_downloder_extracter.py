import urllib.request
import os
import zipfile
from tqdm import tqdm

def download_with_progress(url, output_file):
    with urllib.request.urlopen(url) as response, open(output_file, 'wb') as out_file:
        file_size = int(response.info().get('Content-Length', -1))
        block_size = 1024  

        with tqdm(total=file_size, unit='B', unit_scale=True, desc=output_file, ncols=80) as pbar:
            while True:
                buffer = response.read(block_size)
                if not buffer:
                    break
                out_file.write(buffer)
                pbar.update(len(buffer))

def extract_file(path, name):
    with zipfile.ZipFile(path, 'r') as zip_ref:
        total_size = sum(item.file_size for item in zip_ref.infolist())

        with tqdm(total=total_size, unit='B', unit_scale=True, desc=f"Extracting {os.path.basename(path)}", ncols=80) as pbar:
            for item in zip_ref.infolist():
                zip_ref.extract(item, name)
                pbar.update(item.file_size)

        print(f"Contents of {path} extracted to {name}")

    # Attempt to forcibly remove the downloaded ZIP file after extraction
    os.remove(path)

# URL and output file name
url = "https://huggingface.co/mingu4969/windows-archive-dist/resolve/main/whisper.zip?download=true"
output_file = "whisper.zip"

# Download the file
download_with_progress(url, output_file)

# Check if the downloaded file has a .zip extension
if output_file.lower().endswith('.zip'):
    # Extract the contents of the ZIP file and remove it
    extracted_dir = "whisper_extracted"
    extract_file(output_file, extracted_dir)
else:
    print(f"The downloaded file {output_file} does not have a .zip extension.")
