

def findFollowerIncreasefewDaysTWI(preparedsoup):
    from bs4 import BeautifulSoup
    import requests
    url = requests.get(preparedsoup)
    preparedsoup = BeautifulSoup(url.content, 'html.parser')
    """
    Find the last Days Follower increase but will remove the last because it's the not finished one.
    Will Return a list with the Follower Count
    :param preparedsoup:
    :return:
    """
    followerList = []
    preparedsoup = preparedsoup.find('div', {'id': 'socialblade-user-content'})
    folow = preparedsoup.find_all('div', attrs={'style': 'width: 100px; float: left;'})
    for su in folow:
        su = str(su)
        su = su.replace('<div style="width: 100px; float: left;"><span style="color:#41a200;">', '').replace(
            '</span></div>', "")
        followerList.append(su)
    del followerList[-1]



def findcurrentFollowerTWI(preparedsoup):
    from bs4 import BeautifulSoup
    import requests
    url = requests.get(preparedsoup)
    preparedsoup = BeautifulSoup(url.content, 'html.parser')
    """
       Find the Follower Count of the TwitchUser you are looking for, but will remove the last onr because it's the not finished one.
    Will Return a list with the Follower in Total
    :param preparedsoup:
    :return:
    """
    curFollower = []
    preparedsoup = preparedsoup.find('div', {'id': 'socialblade-user-content'})
    folow = preparedsoup.find_all('div', attrs={'style': 'width: 120px; float: left;'})
    for su in folow:
        su = str(su).replace('<div style="width: 120px; float: left;">', '').replace('</div>', '')
        curFollower.append(su)
    del curFollower[::2]
    del curFollower[-1]


def findadditionalVideoViewsTWI(preparedsoup):
    from bs4 import BeautifulSoup
    import requests
    url = requests.get(preparedsoup)
    preparedsoup = BeautifulSoup(url.content, 'html.parser')
    """
        Find the  + Video Views of the Days you are looking for, but will remove the last onr because it's the not finished one.
    Will Return a list with the additional VideoViews in Total
    :param preparedSoup:
    :return:
    """
    videoViewsList = []
    preparedsoup = preparedsoup.find('div', {'id': 'socialblade-user-content'})
    videoviews = preparedsoup.find_all('div', attrs={'style': 'width: 110px; float: left;'})
    for vi in videoviews:
        vi = str(vi).replace('<div style="width: 110px; float: left;"><span style="color:#41a200;">',"").replace("</span></div>",'')
        videoViewsList.append(vi)
    del videoViewsList[-1]


def findcurrentVideoViewsTWI(preparedsoup):
    """
    Find the Video Views of the counts you are looking for, but will remove the last onr because it's the not finished one.
    Will Return a list with the VideoViews in Total

    :param preparedsoup:
    :return:
    """
    from bs4 import BeautifulSoup
    import requests
    url = requests.get(preparedsoup)
    preparedsoup = BeautifulSoup(url.content, 'html.parser')
    videoViewsList = []
    preparedsoup = preparedsoup.find('div', {'id': 'socialblade-user-content'})
    videoviews = preparedsoup.find_all('div', attrs={'style': 'width: 140px; float: left;'})
    for vi in videoviews:
        vi = str(vi).replace('<div style="width: 140px; float: left;">', "").replace("</div>", '')
        videoViewsList.append(vi)
    del videoViewsList[-1]


def findDateTWI(preparedsoup):
    """
    Find the dates of the counts you are looking for but will remove the last onr because it's the not finished one.
    Will Return a list with the Dates
    :param preparedsoup:
    :return:
    """
    from bs4 import BeautifulSoup
    import requests
    url = requests.get(preparedsoup)
    preparedsoup = BeautifulSoup(url.content, 'html.parser')
    dateList = []
    preparedsoup = preparedsoup.find('div', {'id': 'socialblade-user-content'})
    videoviews = preparedsoup.find_all('div', attrs={'style': 'width: 80px; float: left;'})
    for vi in videoviews:
        vi = str(vi).replace('<div style="width: 80px; float: left;">', "").replace("</div>", '')
        dateList.append(vi)
    del dateList[-1]
