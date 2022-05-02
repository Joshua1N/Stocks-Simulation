import random, time


company_dict = {"Tesla": "https://g.foolcdn.com/art/companylogos/square/tsla.png", "Apple": "APPLE_LINK", "Google": "GOOGLE_LINK"}


while True:
    for key, value in company_dict.items():
        # company_dict[key] = value
        print(value)
    print(company_dict)
    time.sleep(5)



"""
--- STEPS TO CREATE STOCK SIMULATION ---
    1. Calculate the Stock Price
    2. Get the key (Stock Name) from dictionary and put into embed msg
    3. Get the value (Stock Price) from dictionary and put into embed msg
    4. Subtract Stock Price from balance when buying a share, put amount of shares of each stock in embed msg
    5. Loop through the dictionary to show various stocks and their prices
"""

while True:
    for i in company_list:
        print(f"Company: {i}\nStock Price: {random.randint(1, 10)}")
    time.sleep(5)