class TwitchScrapper:
    def __init__(self, link):
        self.link = link

    def find_follower_increase_few_days(self):
        """
        Find the last Days Follower increase but will remove the last because it's the not finished one.
        Will Return a list with the Follower Count
        :param self:
        :return:
        """
        from bs4 import BeautifulSoup
        import requests
        re = requests.get(self.link, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Language": "en-US,en;q=0.5"})
        soup = BeautifulSoup(re.content, 'html.parser')
        follower_count = []
        follow = list(soup.findAll('div', attrs={'style': 'width: 100px; float: left;'}))
        for count in follow:
            count = str(count)
            if "font-weight" in count:
                count = count[count.find('-', count.find("font-weight")+7):].replace("</span></div>", "")
                follower_count.append(count)
            else:
                count = count[count.find('+'):].replace("</span></div>", "")
                follower_count.append(count)

        del follower_count[-1]
        return follower_count

    def find_current_followers_per_day(self):
        """
           Find the Follower Count of the TwitchUser you are looking for, but will remove the last onr because it's the
           not finished one.
        Will Return a list with the Follower in Total
        :param self:
        :return:
        """
        from bs4 import BeautifulSoup
        import requests
        re = requests.get(self.link, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Language": "en-US,en;q=0.5"})
        soup = BeautifulSoup(re.content, 'html.parser')
        result = list(soup.findAll('div', attrs={'style': 'width: 120px; float: left;'}))
        result = result[::2]
        follower_counter = []
        for i in result:
            i = str(i)
            i = i.replace('<div style="width: 120px; float: left;">', "").replace("</div>", "").strip()
            follower_counter.append(i)
        del follower_counter[-1]
        return follower_counter

    def find_additional_video_views(self):
        """
            Find the  + Video Views of the Days you are looking for, but will remove the last onr because it's the not
            finished one.
            Will Return a list with the additional VideoViews in Total
        :param self:
        :return:
        """
        from bs4 import BeautifulSoup
        import requests
        re = requests.get(self.link, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Language": "en-US,en;q=0.5"})
        video_views_list = []
        soup = BeautifulSoup(re.content, "html.parser")
        videoviews = soup.findAll('div', attrs={'style': 'width: 110px; float: left;'})
        for vi in videoviews:
            vi = str(vi).replace('<div style="width: 110px; float: left;"><span style="color:#41a200;">', "").replace(
                "</span></div>", '')
            video_views_list.append(vi)
        del video_views_list[-1]
        return video_views_list

    def find_current_video_views(self):
        """
        Find the Video Views of the counts you are looking for, but will remove the last onr because it's the not
        finished one.
        Will Return a list with the VideoViews in Total
        :param self:
        :return:
        """
        from bs4 import BeautifulSoup
        import requests
        re = requests.get(self.link, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Language": "en-US,en;q=0.5"})
        soup = BeautifulSoup(re.content, 'html.parser')
        video_views_list = []

        videoviews = soup.find_all('div', attrs={'style': 'width: 140px; float: left;'})
        for vi in videoviews:
            vi = str(vi).replace('<div style="width: 140px; float: left;">', "").replace("</div>", '')
            video_views_list.append(vi)
        del video_views_list[-1]
        return video_views_list

    def find_date(self):
        """
        Find the dates of the counts you are looking for but will remove the last onr because it's the not finished one.
        Will Return a list with the Dates
        :param self:
        :return:
        """
        from bs4 import BeautifulSoup
        import requests
        re = requests.get(self.link, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Language": "en-US,en;q=0.5"})
        soup = BeautifulSoup(re.content, 'html.parser')
        date_list = []
        videoviews = soup.find_all('div', attrs={'style': 'width: 80px; float: left;'})
        for vi in videoviews:
            vi = str(vi).replace('<div style="width: 80px; float: left;">', "").replace("</div>", '')
            date_list.append(vi)
        del date_list[-1]
        return date_list


class TwitterScrapper:
    def __init__(self, link):
        self.link = link

    def find_follower_increase(self):
        """
        Find the last 14 Days Follower increase but will remove the last because it's the not finished one.
        Will Return a list with the Follower Count
        :param self:
        :return:
        """
        from bs4 import BeautifulSoup
        import requests
        re = requests.get(self.link, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Language": "en-US,en;q=0.5"})
        soup = BeautifulSoup(re.content, 'html.parser')

        follower_list = []
        followers = soup.find_all('div', attrs={'style': 'width: 100px; float: left;'})
        for user in followers:
            user = str(user)
            if "font-weight" in user:
                user = user[user.find('-', user.find("font-weight")+7):].replace("</span></div>", "")
                follower_list.append(user)
            else:
                user = user.replace('<div style="width: 100px; float: left;"><span style="color:#41a200;">',
                                    '').replace(
                    '</span></div>', "")
                follower_list.append(user)
        del follower_list[-1]
        del follower_list[0]
        return follower_list

    def find_current_follower(self):
        """
           Find the Follower Count of the Twitter User you are looking for, but will remove the last onr because it's the not finished one.
        Will Return a list with the Follower in Total
        :param self:
        :return:
        """
        from bs4 import BeautifulSoup
        import requests
        re = requests.get(self.link, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Language": "en-US,en;q=0.5"})
        soup = BeautifulSoup(re.content, 'html.parser')

        currrent_follower = []
        follower = list(soup.find_all('div', attrs={'style': 'width: 120px; float: left;'}))
        for user in follower:
            user = str(user)
            user = user.replace('<div style="width: 120px; float: left;">', '').replace(" ", "").replace("</div>", "")
            currrent_follower.append(user)

        del currrent_follower[0]
        currrent_follower = currrent_follower[::2]
        del currrent_follower[0]
        del currrent_follower[-1]
        return currrent_follower

    def find_date(self):
        """
        Find the dates of the counts you are looking for but will remove the last onr because it's the not finished one.
        Will Return a list with the Dates
        :param self:
        :return:
        """
        from bs4 import BeautifulSoup
        import requests
        re = requests.get(self.link, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Language": "en-US,en;q=0.5"})
        soup = BeautifulSoup(re.content, 'html.parser')

        date_list = []
        dates = list(soup.find_all('div', attrs={'style': 'width: 80px; float: left;'}))
        for date in dates:
            date = str(date).replace('<div style="width: 80px; float: left;">', '').replace('</div>', '')
            date_list.append(date)
        del date_list[0]
        del date_list[-1]
        return date_list


class YoutubeScrapper:
    def __init__(self, link):
        self.link = link

    def sub_increase(self):
        """
        Find the last 14 Days Subscriber increase but will remove the last because it's the not finished one.
        Will Return a list with the Subscriber Count
        :param self:
        :return:
        """
        from bs4 import BeautifulSoup
        import requests
        re = requests.get(self.link, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Language": "en-US,en;q=0.5"})
        soup = BeautifulSoup(re.content, 'html.parser')

        subscriber_count = []
        subs = list(soup.find_all('div', attrs={'style': 'width: 65px; float: left;'}))
        for sub in subs:
            sub = str(sub)
            if "--" in sub:
                subscriber_count.append("+0")
            elif "color:#41a200;" in sub:
                sub = sub[sub.find('0;">', sub.find('color:#41a200;">'))+4:].replace('</span> </div>', "").replace(" ",
                                                                                                                   "")
                subscriber_count.append(sub)
            else:
                sub = sub[sub.find('600;">')+6:].replace('</span> </div>', "").replace(" ", "")
                subscriber_count.append(sub)
        return subscriber_count

    def find_date(self):
        """
        Find the dates of the counts you are looking for but will remove the last onr because it's the not finished one.
        Will Return a list with the Dates
        :param self:
        :return:
        """
        from bs4 import BeautifulSoup
        import requests
        re = requests.get(self.link, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Language": "en-US,en;q=0.5"})
        soup = BeautifulSoup(re.content, 'html.parser')
        date_list = []
        dates = soup.find_all('div', attrs={'style': 'float: left; width: 95px;'})
        for date in dates:
            date = str(date)
            date = date.replace('<div style="float: left; width: 95px;">', '').replace("</div>", '').replace('\n', '')\
                .replace(" ", "")
            date_list.append(date)
        del date_list[-1]
        return date_list

    def find_current_subs(self):
        """
           Find the Subscriber Count of the Youtuber you are looking for, but will remove the last onr because it's the
        not finished one.Will Return a list with the Subscribers in Total
        :param self:
        :return:
        """
        from bs4 import BeautifulSoup
        import requests
        re = requests.get(self.link, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Language": "en-US,en;q=0.5"})
        soup = BeautifulSoup(re.content, 'html.parser')
        current_subs_list = []
        subs = soup.find_all('div', attrs={'style': 'width: 140px; float: left;'})
        for sub in subs:
            sub = str(sub)
            sub = sub.replace('<div style="width: 140px; float: left;">', '').replace('</div>', '').replace('\n', '').\
                replace(" ", "")
            current_subs_list.append(sub)
        del current_subs_list[2 - 1::2]
        del current_subs_list[-1]
        return current_subs_list

    def find_additional_video_views(self):
        """
            Find the  + Video Views of the Days you are looking for, but will remove the last onr because it's the not
            finished one.
        Will Return a list with the additional VideoViews in Total
        :param self:
        :return:
        """
        from bs4 import BeautifulSoup
        import requests
        re = requests.get(self.link, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Language": "en-US,en;q=0.5"})
        soup = BeautifulSoup(re.content, 'html.parser')
        video_views_list = []
        videoviews = soup.find_all('div', attrs={'style': 'width: 85px; float: left;'})
        for vi in videoviews:
            vi = str(vi)
            vi = vi.replace('<div style="width: 85px; float: left;"><span style="color:#41a200;">', '').replace(
                '</span></div>', '')
            video_views_list.append(vi)
        del video_views_list[-1]
        return video_views_list

    def find_current_video_views(self):
        """
        Find the Video Views of the counts you are looking for, but will remove the last onr because it's the not finished one.
        Will Return a list with the VideoViews in Total
        :param self:
        :return:
        """
        from bs4 import BeautifulSoup
        import requests
        re = requests.get(self.link, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Language": "en-US,en;q=0.5"})
        soup = BeautifulSoup(re.content, 'html.parser')

        current_video_views_list = []
        views = soup.find_all('div', attrs={'style': 'width: 140px; float: left;'})
        for su in views:
            su = str(su)
            su = su.replace('<div style="width: 140px; float: left;">', '').replace('</div>', '')
            current_video_views_list.append(su)

        del current_video_views_list[::2]
        del current_video_views_list[-1]
        return current_video_views_list