import requests

url = 'https://www.qantas.com/hotels/_next/data/-FOfZ_-9zDDMcluxyaI2K/properties/95606.json?adults=2&checkIn=2024-01-26&checkOut=2024-01-28&children=0&infants=0&location=Timisoara%2C+Romania&page=1&payWith=cash&searchType=list&sortBy=popularity&propertyid=95606'
#url = 'https://www.qantas.com/hotels/api/ui/properties/95606/availability?checkIn=2024-01-23&checkOut=2024-01-24&adults=2&children=0&infants=0&payWith=cash'
#url = 'https://www.qantas.com/hotels/api/ui/member-details/1982368431'
#url = 'https://www.qantas.com/hotels/api/ui/properties/95606/availability?checkIn=2024-01-23&checkOut=2024-01-24&adults=2&children=0&infants=0&payWith=cash'
# Make a GET request to the website
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ro-RO,ro;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 'qh_hide_welcome_message=true; pbe_user_id=722c944f-03d7-4dae-b731-8e0ceb94e9dd; qh_user_id=10eee6b4-7302-48b7-9d2c-9176ab79aaff; qh_check_in=2024-02-07; qh_check_out=2024-02-08; qantas_isDevice=type#desktop|os#Windows NT; _hjSessionUser_1001219=eyJpZCI6IjQxMWUxNWJlLWJiNGItNTFkMy1iZTc5LTIyYjIzYzFlZGQ4NiIsImNyZWF0ZWQiOjE3MDU5Mzg5MTUzOTcsImV4aXN0aW5nIjp0cnVlfQ==; _gcl_au=1.1.715739736.1705938916; _gid=GA1.2.1018717316.1705938917; _y2=1%3AeyJjIjp7fX0%3D%3AMTc0OTg2MjMwNA%3D%3D%3A99; usercontext=region#AU|country#AU|locale#en|dep#SYD; check=true; AMCVS_11B20CF953F3626B0A490D44%40AdobeOrg=1; s_ecid=MCMID%7C27322442258814258583695330248298100707; s_cc=true; aam_uuid=27165091198063273633679555568403249762; OptanonAlertBoxClosed=2024-01-22T19:18:33.898Z; QF_VALUE=072072020189075224241197094176055113051055109159; split_user_id=13b218e6-90fb-4c84-916f-00ba53174e99; _fbp=fb.1.1705953030141.436529799; amdfa=done; mobile_app_template=false; QF_LOGINSTATE=hard%20login; qff_info_banner_current_item=0; qff_info_banner_views=2; QSI_SI_basUy0AhxkGRao6_intercept=true; _hjSessionUser_1694601=eyJpZCI6ImQzNDk2ZTIwLTY3MWUtNWU2NS05ZDQ4LWQ3MzU4YTQ0NjcxOSIsImNyZWF0ZWQiOjE3MDYwMDk4Njc2OTcsImV4aXN0aW5nIjp0cnVlfQ==; AMCV_11B20CF953F3626B0A490D44%40AdobeOrg=-432600572%7CMCIDTS%7C19745%7CMCMID%7C27322442258814258583695330248298100707%7CMCAAMLH-1706630801%7C6%7CMCAAMB-1706630801%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1706033201s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.5.2%7CMCCIDH%7C-208009458; mbox=PC#a5e60f11432e4bbc891023b87ca37911.37_0#1769270802|session#2078954cb1d84a0c931ce0b381d952bc#1706027862; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Jan+23+2024+18%3A06%3A42+GMT%2B0200+(Ora+standard+a+Europei+de+Est)&version=202301.2.0&isIABGlobal=false&hosts=&consentId=44813c48-5af9-46a4-99a9-06428c254941&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=RO%3BBV&AwaitingReconsent=false; s_plt=4.43%2Cau%3Aen%3Afrequent-flyer%3Alog-in.html; _ga_R8JNV0W5NK=GS1.1.1706026002.3.0.1706026012.0.0.0; _ga=GA1.2.687491019.1705938917; qtspersisted=_6831c67d8f3b4331a0a8fa7865bf4141_1e53d575995f47fc9a538102a87be576_1705938917402_9007199351268933_1706081826909_10; _abck=B3BDFAA50E02CCA4C6E51B560B5BC1A6~0~YAAQP2d7XK8QNvqMAQAARoxnOgs2RylSZcrjV74ZSSXa69MRLZjWuTzdZrd+gXTJKfs0XXN/yYK9XFlVnco4SnK3cJhY+6fkhkdppBB7eyYjHywnIWqmMb1T1vpH2Jd8leaVA/uwrsF0r7weTCTA4Yqfl1qsi2UI70AAylm+RXOgbm3HfGeyltBoo5X4dy+bQvNUTfn3uJuk06Mt1yC4Ou6R85IQS45+ggi6LrHJ4VdQP4U9PQBFPlgafgSLph7MagbD445Bw+eE4q1QPOZ2YoYIkAfh6rWy3DV7ZtloLYJxmlIH0aUXREqJHazLI67GaaUrfWyp2ccR76srt3vUy3w/kiysrOaOsFz9jJMKxDsP/N+PUX4/AHYUepkDJN5uGMgIsWZ27iAFPO4s4yJgFsxoyWD8TeUu~-1~-1~-1; bm_sz=ADF536BF74500258C0850151AA2407CA~YAAQP2d7XLEQNvqMAQAARoxnOhZ16G1xCCQA2iWuHYQVWHp0v7V/WOHxFnI9onSfnePLq43la+tJVpCHxJfOg3Omg5qJ4AqC2Okro+1zR4PoAXLOFeSelKJCIHI8J1ZrnijVn96ODxgJO3cj4LFbV4tUEsiKVvtxpmBuRdTAT2hL+Dgn/JxiQy5VrSt/+Tp3uI9XGN67pMkhWKG3+Fyw0kxDI9ONggus6EFjWWQ0voGdaxcToGsQhgpw7ltJndRoyTAiUoii2EKg9z/t9xkT1fylbBw4yw3MWSnOQSoFZ6phsIqtJ6gSmTVfX0szg3cv2b6bfGEqqehew81YkQ==~4339778~3617330; lsl_auth_data=1982368431|undefined; qtssession=9007199351268933_1706082729313_1706081826909_6502_53ce4518bc4b4170abcef221b6a75d29; _hjSession_1001219=eyJpZCI6IjZlZGVmNTczLWE0OTktNGEzMC05NTVjLTlkNDI5MWM3ZTIxMyIsImMiOjE3MDYwODcyMjMyOTUsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; AKA_A2=A; bm_mi=A58F79A874C5BE792FB0DB0167134A81~YAAQTWd7XFbYPPWMAQAAlRy5OhYIblwzOwRsXI5EjhQ4AZew7knv+w3rwfOTS1JXuUCRYC1+MEN1bJsYptDGdzq/Mn4ze5IiNQUeYgkooBA3mrGS6QxEEhMHNo6HG4O35duh8pZxmTjZHYabBsc8UltpLM0OFK8gfq1zEgQJ8PmpexD7aErKIyVndTzIXJvg4iCid+xiCBtjUwJTcBOne7ay5ma0ureX8QUN3uTZF1dYwY4RdNuJTOVw+ELbIwVnq2+Rj9yQ5pRmDZttTBloEiJjy67EpN93OiyJ9SMgI/ohcqSn62jyFeDMXwekmJN+TLTQihrMOjKqgCNmYW1rqOLhUTTP~1; ak_bmsc=0A226C1410805234D1051DB21C1CC685~000000000000000000000000000000~YAAQTWd7XLrYPPWMAQAAfB+5OhYNCDELdGticxtylfZ/AezPUHvgN4e2OljhktkUOkQhXqQDumSZlz5PioCKHfNV/RtxjJWuJCAAh9qZR2uFbSFVLd9jP75FDnxRtFNk0om+2CDwkbAAGKjuSY0Bo9uhTUNn4xVwOP/NKLfetJGEgyL1f0seVOHilEQvYBP1KwFnezN2oTEvWMabM+SSdceocvi1HwfRF6/R/rg5Ubcb8Sknvhrv4mAnxkqlFsdASg7u9wWdLSEOQAc1nMjEZSoFj5jf+33bkZfYjZNBidp+3tnXIkO1TwcLziZWJBUuh/N6C1mjUAduV4urZDMch3gkjs8fn1gt6TKRRJkMZTErI9xyQamI1I+zFRXaUnH3lBQz9DVHIZqZpeVkY3EScJ4qb3bL78vchocssrR3x4TGw5Zz3752xodLBwaVkM8eFrSovA1YlY76r1qaRkdNzz6to+TonKzc0Z6Btt678FOrXMfrkjQ3YlxKR6skaz2O78VrFsie5sR8txLHncPfNbju43mncModLgxzba8gWPkBKyPMFXP9sYko2qKtrQ==; initalReferrerHotels=https://www.qantas.com/hotels/search/list?adults=2&checkIn=2024-02-09&checkOut=2024-02-11&children=0&infants=0&location=Sibiu%2C+Romania&page=1&payWith=cash&sortBy=promotion; RT="z=1&dm=www.qantas.com&si=84358328-857c-4105-998e-fe1acb891630&ss=lrrka7bj&sl=1&tt=1wr&bcn=%2F%2F0217991c.akstat.io%2F"; bm_sv=F2BFA4D525A67DAAED012AF2C08319E9~YAAQTWd7XJfaPPWMAQAAEy25OhboLqKepmvpmgHiWEskNR/VgOzGiQ/U62VBUdvw9cqIK02hYRokzXg7vDxbfmdw/Ahnw4qZVydBTBAz1Dy7hO54YiHlHQO2fAHc5oZALIl8XPLKkH2xK7mejpkenODS9f38rOdQ097hxmy0I/02MP0zQmo7CWYWiOvRue6DO8aOcv6NSu4zCJzeOixkgLBNcnMjzXR0RC2Wb9HBq3E1wAsAVXFjjGtDsyuPNYKw~1; _yi=1%3AeyJsaSI6bnVsbCwic2UiOnsiYyI6MywiZWMiOjE4NCwibGEiOjE3MDYwODcyMjk1OTMsInAiOjMzLCJzYyI6MzMyNX0sInUiOnsiaWQiOiIzNzM0MzNjYi1mYjUxLTQyZjMtYmExNS1iODYwNWRiNGQwNTciLCJmbCI6IjAifX0%3D%3ALTE4MDY5MDc0ODg%3D%3A99',
    'Qh-Meta':
'1bb29cfb-5af0-4f80-af07-55207b258684',
'Referer':
'https://www.qantas.com/hotels/auth?error=login_required&state=l6llfTFQE24sZo7TcOE1QSq9plrDBb0kCuL49NoE',
'Sec-Ch-Ua':
'"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
'Sec-Ch-Ua-Mobile':
'?0',
'Sec-Ch-Ua-Platform':
'Windows',
'Sec-Fetch-Dest':
'empty',
'Sec-Fetch-Mode':
'cors',
'Sec-Fetch-Site':
'same-origin',
'Sentry-Trace':
'ac4255d6668f4ed7b2301dbee8134b69-a5e77b084e1ca523-1',
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
with requests.Session() as session:
    session.headers.update(headers)
    response = session.get(url)
response = requests.get(url, headers=headers, allow_redirects=True)


# Check if the request was successful (status code 200)
if response.status_code == 200:
    content_type = response.headers.get('Content-Type', '')
    print(content_type)

    # Print the JSON content of the page
    data = response.json()
    print(data)

    #Extracting the information fields
    rates = []
    for roomTypes in data['pageProps']['initialState']:
        rate = {
            "room_name" : data['pageProps']['initialState']['property']['property']['roomTypes'][0]['name'],
            #'Rate_name': data['pageProps']['initialState']['property']['property'],
            #'Number_of_Guests': data['pageProps']['initialState']['property']['property'],
            'Cancellation_Policy': data['pageProps']['initialState']['property']['property']['policyDescription'],
            #'Price': data['pageProps']['initialState']['property']['property'],
            #'Is_Top_Deal': data['pageProps']['initialState']['property']['property'],
            #'Currency': data['pageProps']['initialState']['property']['property'],
        }
        rates.append(rate)
    print(rates)
        
else:
     print(f"Failed to retrieve the page. Status code: {response.status_code}")
