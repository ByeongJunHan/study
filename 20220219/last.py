menu = {'후라이드':18000, '양념치킨':19000, '윙봉세트':21000, '스페셜파닭':22000}
print(menu)
for i in menu:
    price = menu[i]
    if price < 20000 :
        price = price + 3000
    print (i + "의 배달가격은 "+str(price)+"입니다.")
