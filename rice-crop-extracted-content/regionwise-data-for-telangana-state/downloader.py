import urllib.request

rangareddy_file_url="https://mausam.imd.gov.in/imd_latest/contents/agromet/agromet-data/district/current/english-pdf/"

telangana_districts=[""] * 28
telangana_districts[0] = "Adilabad"
telangana_districts[1] = "Bhadradri%20Kothagudem"
telangana_districts[2] = "Jagtiyal"
telangana_districts[3] = "Jangaon"
telangana_districts[4] = "Jayashankar%20Bhupalpally"
telangana_districts[5] = "Jogulamba"
telangana_districts[6] = "Kamareddy"
telangana_districts[7] = "Karimnagar"
telangana_districts[8] = "Khammam"
telangana_districts[9] = "Kumurambheem%20Asifabad"
telangana_districts[10] = "Mahabubabad"
telangana_districts[11] = "Mahabubnagar"
telangana_districts[12] = "Mancherial"
telangana_districts[13] = "Medak"
telangana_districts[14] = "Medchal%20Malkajgiri"
telangana_districts[15] = "Nagarkurnool"
telangana_districts[16] = "Nalgonda"
telangana_districts[15] = "Nagarkurnool"
telangana_districts[16] = "Nirmal"
telangana_districts[17] = "Nizamabad"
telangana_districts[18] = "Peddapalle"
telangana_districts[19] = "Rajanna%20Sircilla"
telangana_districts[20] = "Rangareddy"
telangana_districts[21] = "Sangareddy"
telangana_districts[22] = "Siddipet"
telangana_districts[23] = "Suryapet"
telangana_districts[24] = "Vikarabad"
telangana_districts[25] = "Wanaparthy"
telangana_districts[26] = "Warangal%20Rural"
telangana_districts[27] = "Warangal%20Rural"

def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url+filename+'.pdf')
    doc = open(filename+".pdf", 'wb')
    doc.write(response.read())
    doc.close()
    return doc

for _ in telangana_districts:
    download_file(rangareddy_file_url, _)