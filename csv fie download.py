from urllib import request

csv_url = 'https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2018-financial-year-provisional/Download-data/annual-enterprise-survey-2018-financial-year-provisional-size-bands-csv.csv'
def download_csv(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    str_csv = str(csv)
    lines = str_csv.split("\\n")
    name_url = r'first.csv'
    fs = open(name_url, 'w')
    for line in lines:
        fs.write(line + '\n')

    fs.close()
    
download_csv(csv_url)


