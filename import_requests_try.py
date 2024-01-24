import json
import requests
#import re

# Replace 'https://example.com' with the URL of the website you want to scrape
url = 'https://www.qantas.com/hotels/properties/95606?adults=2&checkIn=2024-01-23&checkOut=2024-01-24&children=0&infants=0&location=Timisoara%2C%20Romania&page=1&payWith=cash&searchType=list&sortBy=popularity'

# Make a GET request to the website
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ro-RO,ro;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Cookie': 'qh_hide_welcome_message=true; pbe_user_id=9372df62-cfe4-4f4c-921f-5b4b0e3165ff; qh_user_id=1bb29cfb-5af0-4f80-af07-55207b258684; qh_check_in=2024-01-23; qh_check_out=2024-01-24; qantas_isDevice=type#desktop|os#Windows NT; _hjSessionUser_1001219=eyJpZCI6IjQxMWUxNWJlLWJiNGItNTFkMy1iZTc5LTIyYjIzYzFlZGQ4NiIsImNyZWF0ZWQiOjE3MDU5Mzg5MTUzOTcsImV4aXN0aW5nIjp0cnVlfQ==; _gcl_au=1.1.715739736.1705938916; _gid=GA1.2.1018717316.1705938917; _y2=1%3AeyJjIjp7fX0%3D%3AMTc0OTg2MjMwNA%3D%3D%3A99; usercontext=region#AU|country#AU|locale#en|dep#SYD; check=true; AMCVS_11B20CF953F3626B0A490D44%40AdobeOrg=1; s_ecid=MCMID%7C27322442258814258583695330248298100707; s_cc=true; aam_uuid=27165091198063273633679555568403249762; OptanonAlertBoxClosed=2024-01-22T19:18:33.898Z; QF_VALUE=072072020189075224241197094176055113051055109159; split_user_id=13b218e6-90fb-4c84-916f-00ba53174e99; _fbp=fb.1.1705953030141.436529799; amdfa=done; mobile_app_template=false; QF_LOGINSTATE=hard%20login; qff_info_banner_current_item=0; qff_info_banner_views=2; QSI_SI_basUy0AhxkGRao6_intercept=true; _hjSessionUser_1694601=eyJpZCI6ImQzNDk2ZTIwLTY3MWUtNWU2NS05ZDQ4LWQ3MzU4YTQ0NjcxOSIsImNyZWF0ZWQiOjE3MDYwMDk4Njc2OTcsImV4aXN0aW5nIjp0cnVlfQ==; qtspersisted=_6831c67d8f3b4331a0a8fa7865bf4141_1e53d575995f47fc9a538102a87be576_1705938917402_9007199351075172_1706023189522_6; bm_sz=2B6EDB71749528C95F227971C36F7D83~YAAQTWd7XMIh+/SMAQAAtPf6NhaTGBg9DT8vPCDs5RFijXmyouT4Tr+v614LbDpbCRppQsnIZqYkm5bhiEfDOF8d8nDf/WouvmYmEsS+0mhI7YQXxuJW+mD8kzz3SEQR3VV4aveznhhuQRJOrbg6kQ3rMP4ij/9ayXwTaaS3f7rTRsTvvNTWvqMhYcIw/KLPgBeIe+vNsULcY71AVV6ynj6yzOsbMWKSD2R2W/PWWtUnRpKs6v46xt9pRnF4CmTK2DVjITzleYWl+Gvphw+IaTDYO4WfQEJHkbD32vIpsr344tH3zG14cppm0v502m/29j6kKHpsFk9q8B3ZuOY0cwS1iKrPoL5MZbqJOdNiHzZipbCXOg==~4404018~4273475; bm_mi=E8EEAC7C286159534A5483DA84CF76D2~YAAQTWd7XHmr/fSMAQAApp4PNxbPcWt6fSCDi6f9WeavIimoEe+MrPTKEW9CJTZ/PgDB1G8nsHQMEQZmHRQ4polJ4JOWPJxi8d3djdEblXRky2/tvQJzK37a8b6w2DSd0k8K+CdeP+Zyy9OYxuprCeUj1ce3DY/n/V9oo8PulBnDKp3UeiYlMrW15VH/OTvNhd4ENBzc3rNB3JM8/1f2Kcsd8M58QPlod1tIt3vlJbWq0Lu6QK7WT1u/sexTAcSANQOvimw/T/hnlI9gOgu1xh91fF0DBrcIz4taQKz9+3rvB7k/Hp8pRpJJr3At1fALo1+CKFyhKUwqlPEXRHAl29oYcwr+JA==~1; bm_sv=E6B7937F3C1D66E697F84EC24897CFF3~YAAQTWd7XO+x/fSMAQAAs80PNxZ66gI6AM0TQqrfARwy3QLWz0UPIaRtEnr/UiNrdyUrruD8+PR5rcsQ+uLFRUCSLWe6/Yg4PdHJF+luQo0AODNjlWHJe89K45z643nivOQEP9NMWkOd2pmrjMrbgHzvNyhfSLxQ9nEAX0266G4SE+a4PIgTK9ZFPDeCoy/HB5AE0TAlgxqRvZJ594tKQew7HhlMkdouf56wME+Fj176tlaIE0Y6eFBXBpg8TsITAaE=~1; ak_bmsc=AFA9D542B94D75AD7DCE35B147A23243~000000000000000000000000000000~YAAQTWd7XNq2/fSMAQAAsPMPNxYXjdtWGPT2d3LrlurGxVLzpcUUBpGzHdss3aVrCtQ89KNtwJdH32too1KZDOn8urkk/bgst+ZgTvGCeR8CSfzIrVohtf862DwlDInK8lM8ZlVjS3aC2FQmNmpavSHTXtLl3eId8Owq3WR5AKyVZw1OAj+02deJphznkVF265SIAJvgdm1XIzzDxc7g/4wUQpdwjIrctkazYV0la2Gz12ismoVtMK0+wzcX2fBDpbpwEdt326evH8gDpLeBcbBLomz+UmdUO9hy4V4XdWCn/ogOXyaa0igmcfs3FG9ygKUlXQyl9lS5NaycS/XggfMS0yZ5EmbCTrHZxhAT4cIonotUEDJhv64DOth1TLrheby788A5gVCyx3ada2uF6sXnu6TvNoAWQEi44uxAeqQp0r8FXtXHmwryIq3ka27viWNJXiMrTm7s6XyFGgHT0OVHtQbtMZ+218CXcwAb+dUJGtePozI5e8dWTxYCANX9uTr8pemZbNuCxTMnRHCx9ndQ3CBgqITHuMumS1WiY9eusteQ7gqjBZTNNQ4=; AMCV_11B20CF953F3626B0A490D44%40AdobeOrg=-432600572%7CMCIDTS%7C19745%7CMCMID%7C27322442258814258583695330248298100707%7CMCAAMLH-1706630801%7C6%7CMCAAMB-1706630801%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1706033201s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.5.2%7CMCCIDH%7C-208009458; mbox=PC#a5e60f11432e4bbc891023b87ca37911.37_0#1769270802|session#2078954cb1d84a0c931ce0b381d952bc#1706027862; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Jan+23+2024+18%3A06%3A42+GMT%2B0200+(Ora+standard+a+Europei+de+Est)&version=202301.2.0&isIABGlobal=false&hosts=&consentId=44813c48-5af9-46a4-99a9-06428c254941&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=RO%3BBV&AwaitingReconsent=false; s_plt=4.43%2Cau%3Aen%3Afrequent-flyer%3Alog-in.html; _ga_R8JNV0W5NK=GS1.1.1706026002.3.0.1706026012.0.0.0; _ga=GA1.2.687491019.1705938917; _hjSession_1001219=eyJpZCI6IjA5OTUxY2RkLTA3MjMtNDc2MC05YWFhLWQxYzZjZDljYjNhMyIsImMiOjE3MDYwMjYwMzQzNzYsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; initalReferrerHotels=; AKA_A2=A; qtssession=9007199351075172_1706028234335_1706023189522_6502_ffbc9a50ba004711b92e8824df671dee; _gat_UA-32359880-1=1; _gat_UA-259752839-1=1; _abck=B3BDFAA50E02CCA4C6E51B560B5BC1A6~0~YAAQTWd7XE4fAvWMAQAAsys1NwtFLxQcHQLsRWCe3xYdumhO3xCAsiVW8Bug+vcsLGrE7Q5f+D5Bh5n3mR0vFkt+2htE4fVGWk4Rj1o0SXThfR84HRNAGAp+0j0L/qVWTUQVeqqHLI7QsELiJx9fCgMnVsvYEMxeYXPmyaezDgcEmoT1BDBTT30c42X4zhqlkE+UxOUm77NiM9FEcjCE1gu+zOUzp9SYmhfbALl0lwsJxkDrB0YMVF90cz10QSNO+K4lC+VfawlRuB6X18mIsIbh+rCkS18NS3rYCT6an+MOyOBie553onC+/QT4unYygZncoSaIksQzSvbAZnU3037euVcIP+I1hNDEIdWF1j9sfjiNj4jRIbEiSQAzEQ==~-1~-1~-1; _yi=1%3AeyJsaSI6bnVsbCwic2UiOnsiYyI6MywiZWMiOjI5MCwibGEiOjE3MDYwMjgyNDkzNzcsInAiOjQ3LCJzYyI6Njg0OH0sInUiOnsiaWQiOiIzNzM0MzNjYi1mYjUxLTQyZjMtYmExNS1iODYwNWRiNGQwNTciLCJmbCI6IjAifX0%3D%3ALTE4MDY5MDc0ODg%3D%3A99; RT="z=1&dm=www.qantas.com&si=84358328-857c-4105-998e-fe1acb891630&ss=lrqiwkif&sl=4z&tt=417u&bcn=%2F%2F0217991a.akstat.io%2F&obo=1&ld=29i9v&ul=29lqh"',
    'Qh-Meta':
'1bb29cfb-5af0-4f80-af07-55207b258684',
'Referer':
'https://www.qantas.com/hotels/properties/95606?adults=2&checkIn=2024-01-26&checkOut=2024-01-28&children=0&infants=0&location=Timisoara%2C%20Romania&page=1&payWith=cash&searchType=list&sortBy=popularity',
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

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Find the JSON data within the script tag
    script_start = response.text.find('<script id="__NEXT_DATA__" type="application/json">') + len('<script id="__NEXT_DATA__" type="application/json">')
    script_end = response.text.find('</script>', script_start)
    
    
    # Extract and load JSON data
    json_data = json.loads(response.text[script_start:script_end])

    # Access information within the JSON structure
    room_name = json_data['props']['pageProps']['initialState']['property']['property']['roomTypes'][0]['name']
    cancellation_policy = json_data['props']['pageProps']['initialState']['property']['property']['policyDescription']
    adults = json_data['query']['adults']
    children = json_data['query']['children']

    # Print or use the extracted information
    print("Room_name:", room_name)
    print("Cancellation Policy:", cancellation_policy)
    print("Number Of Guests:", adults, "adults and", children, "children")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

