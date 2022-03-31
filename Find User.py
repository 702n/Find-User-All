try:
    import sys
    import requests
    import time
except Exception as e:
    print(e)
rs = requests.session()

print("instagram [ @Rad.out\@207u1 ] Follow Me <3")
print("=================================")
user = input("[?] Enter The Username : ")
if user == "":
    print("Enter Something Pls..,")
    sys.exit()
else:
    print("_"*40)
    def TikTok():
        url = f'https://www.tiktok.com/@{user}?lang=ar'

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
            "Connection": "close",
            "Host": "www.tiktok.com",
            "Accept-Encoding": "gzip, deflate",
            "Cache-Control": "max-age=0"
        }

        re = rs.get(url, headers=headers)
        if re.status_code == 404:
            print(f"[+] [ TikTok ] --> Available [{user}]")
        elif re.status_code == 200:
            print(f"[-] [ TikTok ] --> Not Available [{user}]")


    # ------------------------------------------------------------------------------------------------------------------------------------------------------
    def Tellonym():
        url = f'https://tellonym.me/{user}'

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': '__cfduid=d0ffc45fa1efa9e0d736b1c14bb6c594a1605979176; _ga=GA1.2.821290333.1605979177; G_ENABLED_IDPS=google; __gads=ID=c7705da3c1f492a3:T=1606880061:S=ALNI_MZomN5KxOkG_i59jEZaJOEsiBQi6g; _gid=GA1.2.725225671.1606979880; cf_clearance=dcd41d1895597ca22ffa90136382f60ddea9e6e2-1606979881-0-150; __rtgt_sid=ki8ibzq4bp1k2d; _gat=1',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        re = rs.get(url, headers=headers)
        if re.status_code == 404:
            print(f"[+] [ Tellonym ] --> Available [{user}]")
        elif re.status_code == 200:
            print(f"[-] [ Tellonym ] --> Not Available [{user}]")


    # ------------------------------------------------------------------------------------------------------------------------------------------------------
    def GitHub():
        url = f'https://github.com/{user}'

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': '_octo=GH1.1.757675268.1606661116; _device_id=f629b81e5083a13fa7ff014a68f146ad; tz=Asia%2FDubai; tz=Asia%2FDubai; user_session=1_webWJdC6-KCRvLPP8kCdYXseBBDeWd-uLbw5B1PN8iGaqg; __Host-user_session_same_site=1_webWJdC6-KCRvLPP8kCdYXseBBDeWd-uLbw5B1PN8iGaqg; logged_in=yes; dotcom_user=w89X; has_recent_activity=1; _gh_sess=EjdS347LjhnAHcdI%2B7aLQV9xGe0exyfegs3osnq3UdiDl8rOC8td4pKGZ%2Fp0qpn6xGlE2Apl2BuZgSYL9rUGuBHBzcJ%2Fi05RwIMeoWi%2BxGRWFWUeZp5O38PUCLx3sJ%2BYTJRxjs0NC84iYLcNpygCph5UNw2mHR4WD96F5jMTUNVj5wQH4ntWGHeAtvcDXF9h4sS1k4iLZ%2Bxj97PDOg8PpyhWTaOiQK7awdm2V9AGKcRsdhpkZ4Y5%2BtK1ytFCA9FlLUsshiHc2eBp8eE8kS03rhh1UeFgyeywoOJOYCID2cM%2BmYszXQxkAMbsGay8youvQzxL128%2B4kgG%2FCLX8insdoEZjsSxPFEge7F1myY5IBxDjeOui8skQfY3qjWQ1qWz%2Fpz4ort3tL8jfkN8H7ZYP3%2BL1n9AHayFw4ehNLlnJWyVSicbcxq7T1IqdpGrqiFHDTOhN%2Fg9A0zqK%2FLt%2FNAsplwVcRtwVMBsfynjEKVd3tYJXytFccDS3uGI1uUtahGYHspepz3gWL1tGuM88%2BsvBG6ao%2Bv1Jeg91LziNDgqrFzA4rTFdMHhLzhzBoaZXbK4w%2F4sUMZrz7QdSjJ7Cgy6E%2BkGzuAFX7Y9qyFPTa0b%2BO2flxg7oJIHAk%2B%2Bl0I4LC8fBXeT0q2th6mzki%2F3oqS38AL1ZRDm8hTZhzAv%2FvNc7amwOHCjveVnU1N0rfEOPHyX24JF3clZggLB0ptgfcFmkW9u%2FlBNDAZSOzwjXG5l6a18TV%2FtR6HoX2V5tViSqspjpurMiE2%2F7oWKoMWDa6eZe89o9QMtuj2FDi1txY18WbSlJmfUSSfERCvzL00KyVgj47l00bPFtgD7y2WkGFEYO2S9CTMkvX2P6og2igbY5LRqL94K9cEXd5vTvdLMF3cp%2FMgCXGQ%2FmRwPYIVRmQRlzySV1%2FgaMVufn46k05Ubvl%2FmqPWr0A2BNfHARB%2F%2F31w5OeQAHIKWTqSThMmuZ3D2BGRXVm0%2FnpnYl2XUW%2Fo%2BtApuJ9KRQYKngVHOg5vu0U6hJx58Z7i09cB9tKisIY8q43kFfK%2FHkOjwfSdzUEaiRO6vqOBYS1sSUyRUMiJdbijkdIfN7dQVaUNXeMbY--epk8IbZB8LCR3S32--4y%2FdnK2SoukkzGXhhv245Q%3D%3D',#t8pr
            # t8pr
            'if-none-match': 'W/"38bd103a9925fd49af948e551ca81125"',
            'referer': f'https://github.com/berliv',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        re = rs.get(url, headers=headers)
        if re.status_code == 404:
            print(f"[+] [ GitHib ] --> Available [{user}]")
        elif re.status_code == 200:
            print(f"[-] [ GitHub ] --> Not Available [{user}]")


    # ------------------------------------------------------------------------------------------------------------------------------------------------------
    def Twitch():
        twitch_url = f"https://m.twitch.tv/{user}"
        headers = {
            'Host': 'm.twitch.tv',
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
            "Accept-Language": "en-us",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://m.twitch.tv/service-worker.js",
            'Connection': 'keep-alive'
        }

        re = rs.get(twitch_url, headers=headers)
        if re.status_code == 404:
            if len(user) >= 4:
                print(f"[+] [ Twitch ] --> Available [{user}]")
            else:
                print(f"[-] [ Twitch ] --> Less Than 4 [{user}]")
        elif re.status_code == 200:
            print(f"[-] [ Twitch ] --> Not Available [{user}]")


    # ------------------------------------------------------------------------------------------------------------------------------------------------------
    def Twitter():
        url = f'https://tweeterid.com/ajax.php'
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ar,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'Connection': 'keep-alive',
            'Content-Length': '22',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': '__utma=116903043.1720803994.1612504548.1612504548.1612504548.1; __utmc=116903043; __utmz=116903043.1612504548.1.1.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=116903043.1.10.1612504548; __gads=ID=88cfb7beeee2c10b-22d6173bbfa600bb:T=1612504549:RT=1612504549:S=ALNI_MZ6nNZgByoGcMcYOoxsJhmoIAX2fg',
            'Host': 'tweeterid.com',
            'Origin': 'https://tweeterid.com',
            'Referer': 'https://tweeterid.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        data = {
            'input': user
        }
        re = rs.post(url, data=data, headers=headers).text
        if ('error') in re:
            print(f"[+] [ Twitter ] --> Available [{user}]")
        else:
            print(f"[-] [ Twitter ] --> Not Available [{user}]")


    # ------------------------------------------------------------------------------------------------------------------------------------------------------
    def Reddit():
        url = f'https://www.reddit.com/user/{user}'
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'cookie': 'csv=1; edgebucket=XLi4dckGsH3ZzbBPkm; __aaxsc=1; recent_srs=t5_2riqp%2Ct5_37dnc%2C; G_ENABLED_IDPS=google; reddit_session=774396530106%2C2021-02-15T11%3A01%3A57%2C3ea6ea9fe7630a960e0d5bd7e82707205938ac26; loid=00000000009vr3p6t6.2.1610997412710.Z0FBQUFBQmdLbFNsQ2JhU0tkMFdSaGpna3lNb2RoSGNXcWduUWR0aFY5OVBjRjVUZF8wVmdNUEhuU1RLRjdnOW5aRTVZTUlUVjdDSVB5THJRVUVHRmdFUUNGUVhXdEVhVWlpZnBtTDlLUzdabGhJZXFZMmpmUjRmU0RjSVIyamR3bHR5V25ZSXBQeDM; token_v2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTMzOTAzOTcsInN1YiI6Ijc3NDM5NjUzMDEwNi1yak1sUVJNNy1XODdBWXBuSTVWLXBFdmx6RDAiLCJsb2dnZWRJbiI6dHJ1ZSwic2NvcGVzIjpbIioiLCJlbWFpbCJdfQ.r4tOKmu4JR0mx9Nde2ztjAMBMINyS88e-R8tq9PeZnc; Puzzleheaded-Bit-529_recentclicks2=t3_3fytv0; USER=eyJwcmVmcyI6eyJnbG9iYWxUaGVtZSI6IlJFRERJVCIsImNvbGxhcHNlZFRyYXlTZWN0aW9ucyI6eyJmYXZvcml0ZXMiOmZhbHNlLCJtdWx0aXMiOmZhbHNlLCJtb2RlcmF0aW5nIjpmYWxzZSwic3Vic2NyaXB0aW9ucyI6ZmFsc2UsInByb2ZpbGVzIjpmYWxzZX0sIm5pZ2h0bW9kZSI6dHJ1ZSwicnBhbkR1RGlzbWlzc2FsVGltZSI6bnVsbCwidG9wQ29udGVudERpc21pc3NhbFRpbWUiOm51bGwsInRvcENvbnRlbnRUaW1lc0Rpc21pc3NlZCI6MH19; session_tracker=kkoilgqmkmagbhfjqj.0.1613387003522.Z0FBQUFBQmdLbFQ3clNqY0NNQ21qalRGbEhQR0pYbmsxbXBaWkJkd3BLajBRXy1zbjJRamZGMnNyNlJZTng4NnY0ZnFIQVkzeGFaVUQzbG5fdE9pVnotMTB0dXVXTFlic25uYXB5bFIyVXhsS2Y1bXFtWW1NbGJuRmRGVUVpTnE1TXFtbmhZRnQwN0M; session=676cbfbb8c2881ee93584adfdda78b7dffe4cd5fgASVSQAAAAAAAABK/1QqYEdB2AqVDgxHGn2UjAdfY3NyZnRflIwoZDBmYjAwNzQyN2Q5MzM4ODY3N2Y2ZjdjM2FjMjFiY2VhNTdiODUyYpRzh5Qu; aasd=6%7C1613386798125',#8pr
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        }
        re = rs.get(url, headers=headers)
        if re.status_code == 404:
            if len(user) >= 3:
                print(f"[+] [ Reddit ] --> Available [{user}] ")
            else:
                print(f"[-] [ Reddit ] --> Less Than 3 [{user}] ")
        elif re.status_code == 200:
            print(f"[-] [ Reddit ] --> Not Available[{user}] ")


    # ------------------------------------------------------------------------------------------------------------------------------------------------------
    def Instagram():
        url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'

        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
            'content-length': '61',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/emailsignup/',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
            'x-instagram-ajax': '72bda6b1d047',
            'x-requested-with': 'XMLHttpRequest'

        }
        data = {
            'email': 'A@gmail.com',
            'username': f'{user}',
            'first_name': 'AAAAAA',
            'opt_into_one_tap': 'false'
        }

        re = requests.post(url, headers=headers, data=data).text

        if (
                '{"account_created": false, "errors": {"email": [{"message": "Too many accounts are using a@gmail.com.", "code": "email_sharing_limit"}], "__all__": [{"message": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}') in re:
            print(f"[-] [ Instagram ] --> Available [{user}] ")

        else:
            print(f"[-] [ Instagram ] --> Not Available [{user}] ")
    def SnapChat():

        url = f'https://accounts.snapchat.com/accounts/get_username_suggestions'

        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '57',
            'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
            'cookie': 'xsrf_token=qguFhKiP7FrimtibnGvopQ; web_client_id=6dee3ce3-db42-4fd0-b538-682cdb294f9a; _scid=482919d7-1390-46c8-8951-d3031e352b63; _sca={%22cid%22:%22e22c1577-7f73-4b69-85ff-79b72444951a%22%2C%22token%22:%22v1.key.2020-03-05_UKiB4eNE.iv.MeUzIJboKx7l+nZu.zf9r/dgUl/1vg1iBp4fz27qapzxGL1VJowr9Clna1AvHYCTUocABFHpeSMdPC2BGmfDmAfrA8eEqFPnV5qNP/QJCPISHEUpj7aGeYGpoggjapYZZ%22}; sc-cookies-accepted=true; Preferences=true; Performance=true; Marketing=true; _ga=GA1.2.148694331.1613677502; _gid=GA1.2.1609447525.1613677502; _gat_UA-41740027-4=1',
            'origin': 'https://accounts.snapchat.com',
            'referer': 'https://accounts.snapchat.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'same-origin',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        }
        data = {
            'requested_username': f'{user}',
            'xsrf_token': 'qguFhKiP7FrimtibnGvopQ',
        }
        re = requests.post(url, data=data, headers=headers)
        if re.text.find('"status_code":"OK"') >= 0:
            print(f"[+] [ SnapChat ] --> Available [{user}]")
        elif re.text.find('"status_code":"TAKEN"') >= 0:
            print(f"[-] [ SnapChat ] --> Not Available [{user}]")
        else:
            print(f"[-] [ SnapChat ] --> Banded {user}")

    Instagram() #1
    SnapChat() #2
    Tellonym() #3
    Twitter() #4
    TikTok() #5
    Twitch() #6
    GitHub() #7
    Reddit() #8

print("_"*40)
print("Find User Tool By Programmer Rad <3")
