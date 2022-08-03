import requests
from bs4 import BeautifulSoup

def extract_data():
    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        date_time = soup.find('span', {'class':'waktu'})
        date = date_time.text.split(', ')[0]
        time = date_time.text.split(', ')[1]

        element_left = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = element_left.findChildren('li')
        i = 0
        magnitude = None
        depth = None
        lu = None
        bt = None
        location = None
        source = None

        for res in result:
            if i == 1:
                magnitude = res.text
            elif i == 2:
                depth = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                lu = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                location = res.text
            elif i == 5:
                source = res.text
            i = i + 1

        update = dict()
        update["date"] = date #"7 April 2022"
        update["time"] = time #"16:52:58"
        update["magnitude"] = magnitude
        update["depth"] = depth
        update["location"] = {"LU": lu, "BT": bt}
        update["source"] = source
        return update
    else:
        return None



def visualize_data(result):
    if result is None:
        print("No se pueden encontrar los datos")
        return
    print("Latest Earthquake of Indonesia")
    print(f"Date : {result['date']}")
    print(f"Time : {result['time']}")
    print(f"Magnitude : {result['magnitude']}")
    print(f"Depth : {result['depth']}")
    print(f"Location : LU = {result['location']['LU']}, BT = {result['location']['BT']}")
    print(f"Source : {result['source']}")