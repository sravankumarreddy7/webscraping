from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Vivo').text
soup = BeautifulSoup(html_text, 'lxml')

phones = soup.find_all('div', class_='_3pLy-c row')
phone = phones[0]
filename = "phonnnee.csv"
f = open(filename, "w")
headers = "model, rating, performance\n"
f.write(headers)

for phone in phones:
    model_text = phone.div.div.text.replace(","," ")
    ratings = phone.find('span', class_='_2_R_DZ')
    rating_text = ratings.text.replace(","," ")
    performance = phone.find('div', class_='fMghEO')
    performance_text = performance.ul.li.text.replace(","," ")

    print("model_text: " + model_text)
    print("rating_text :" + rating_text)
    print(" performance_text :" +  performance_text)

    f.write(model_text + "," + rating_text + "," + performance_text +"\n")
f.close()