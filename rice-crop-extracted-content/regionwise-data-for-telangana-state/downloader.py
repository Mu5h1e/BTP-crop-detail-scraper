import urllib.request

rangareddy_file_url="https://mausam.imd.gov.in/imd_latest/contents/agromet/agromet-data/district/current/english-pdf/"

with open("district_list.txt","r") as f:
    telangana_districts = f.read().splitlines()

def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url+filename+'.pdf')
    doc = open("./district_data/"+filename+".pdf", 'wb')
    doc.write(response.read())
    doc.close()
    return doc

for _ in telangana_districts:
    download_file(rangareddy_file_url, _)