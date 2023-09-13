import requests
import os.path
import os

def download_url(_url, output_path):
    print("downloading: ", _url)
    # assumes that the last segment after the / represents the file name
    # if url is abc/xyz/file.jpg, the file name will be file.jpg
    file_name_start_pos = _url.rfind("/") + 1
    file_name = _url[file_name_start_pos:]
    r = requests.get(_url, stream=True)
    if r.status_code == requests.codes.ok:
        with open(os.path.join(output_path, file_name), 'wb') as f:
            for data in r:
                f.write(data)
    return os.path.exists(file_name)

if not os.path.isdir('output'):
    os.mkdir('output')

file1 = open('download.txt', 'r')
Lines = file1.readlines()
for line in Lines:
    download_url(line, 'output')
