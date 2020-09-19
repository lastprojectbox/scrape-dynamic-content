import requests, re, json

session = requests.Session()
url = 'https://www.aliexpress.com/item/4000714495996.html'
r = session.get(url)
match = re.search(r'data: ({.+})', r.text).group(1)
data = json.loads(match)
title = data['pageModule']['title']
product_id = data['commonModule']['productId']
price = data['priceModule']['formatedPrice']
rating = data['titleModule']['feedbackRating']['totalValidNum']
orders = data['titleModule']['tradeCount']

goal = {
    'title': title,
    'product_id': product_id,
    'price': price,
    'rating': rating,
    'orders': orders,
}

with open('results/{}.json'.format(product_id), 'a') as json_file:
    json.dump(goal, json_file)
