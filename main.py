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
    
visual_studio = Selenium_Download(
    driver="driver\geckodriver.exe",
    exe=lista.links[10],
    element="/html/body/div[3]/main/div/div/div/div/div[2]/div/div/div/div[1]/div[3]/div/div[1]/div[1]/div/div[3]/div/div/a/span"
)

postman = Selenium_Download(
    driver="driver\geckodriver.exe",
    exe=lista.links[11],
    element=None
)

visual_studio_code = Selenium_Download(
    driver="driver\geckodriver.exe",
    exe=lista.links[12],
    element=None
)

kanban = Selenium_Download(
    driver="driver\geckodriver.exe",
    exe=lista.links[13],
    element="/html/body/div/div[3]/div/div/div[1]/div[1]/div[2]/button/span/div/font"
)


