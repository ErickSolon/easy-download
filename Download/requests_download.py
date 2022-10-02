import requests
import os

class Requests_Download():
    def download_file(url):
        local_filename = url.split('/')[-1]

        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(os.path.join("executaveis/", local_filename), 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        r.close()
        f.close()
        return local_filename
