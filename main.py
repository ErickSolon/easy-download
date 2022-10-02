import lista
import os

from Download.requests_download import Requests_Download
from Download.selenium_download import Selenium_Download

if(os.path.exists(path="executaveis")):
    for list_dir in os.listdir("executaveis"):
        os.remove(os.path.join("executaveis/", list_dir))
    
    os.rmdir("executaveis")
else:
    os.mkdir("executaveis")

for download_files in lista.links:    
    Requests_Download.download_file(download_files)
    
download_selenium = Selenium_Download()
download_selenium.Download_Kanban_Tasker()
download_selenium.Download_Postman()
download_selenium.Download_VS()
download_selenium.Download_Vscode()
    
    


