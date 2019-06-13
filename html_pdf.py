import requests
import pdfkit

# url = input("http://google.com")
# pdf = pdfkit.from_url(url, "file.pdf")
# path = input("D:/All_doc")
#
# print("Download starting.")
# r = requests.get(pdf)
#
# with open(path, 'wb') as f:
#     f.write(r.content)



url = input("Please enter the url of the file you want to download.")
path = input("Please enter the file path ex. C:\Jim\Desktop")
file_name = input("Please enter file name")

path_wkhmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhmltopdf)

if pdfkit.from_url(str(url), str(path + file_name),configuration=config): # Check if method from_url returned True
    print("Sucessfully created pdf from url")
else:
    print("Something went wrong")