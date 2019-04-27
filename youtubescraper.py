def findSubsIncreasefewDaysYT(preparedsoup):
    """
    Find the last 14 Days Subscriber increase but will remove the last because it's the not finished one.
    Will Return a list with the Subscriber Count
    :param preparedsoup:
    :return:
    """
    from bs4 import BeautifulSoup
    import requests
    url = requests.get(preparedsoup)
    preparedsoup = BeautifulSoup(url.content, 'html.parser')
    lastfewSubscriber = []
    preparedsoup = preparedsoup.find('div', attrs={'style': 'width: 860px; float: left; font-size: 8pt;'})
    subs = preparedsoup.find_all('div', attrs={'style': 'width: 65px; float: left;'})
    for su in subs:
        su = str(su)
        su = su.replace('<div style="width: 65px; float: left;"><span style="color:#41a200;">', "").replace(
            "</span></div>", "")
        lastfewSubscriber.append(su)
    del lastfewSubscriber[-1]
    return lastfewSubscriber


def findSubsIncreaseMonthlyYT(preparedsoup):
    """
    Find the last like 30 Days Subscriber but will remove the last because it's the not finished one.
    Will Return a list with the Subscriber Count
    :param preparedsoup:
    :return:
    """
    from bs4 import BeautifulSoup
    import requests
    url = requests.get(preparedsoup)
    preparedsoup = BeautifulSoup(url.content, 'html.parser')
    lastmonthlysubs = []
    lastmonthsub = preparedsoup.find('div', attrs={'style': 'width: 880px; float: left;'})
    subs = lastmonthsub.find_all('div', attrs={'style': 'width: 65px; float: left;'})
    for su in subs:
        su = str(su)
        su = su.replace('<div style="width: 65px; float: left;"><span style="color:#41a200;">', "").replace(
            "</span></div>", "")
        lastmonthlysubs.append(su)
    del lastmonthlysubs[-1]
    return lastmonthlysubs

def findDateYT(preparedsoup):
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
    datecontainer = preparedsoup.find('div', attrs={'style': 'width: 880px; float: left;'})
    dates = datecontainer.find_all('div', attrs={'style': 'float: left; width: 95px;'})
    for su in dates:
        su = str(su)
        su = su.replace('<div style="float: left; width: 95px;">', '').replace("</div>", '').replace('\n','')
        dateList.append(su)
    del dateList[-1]
    return dateList


def findcurrentSubsYT(preparedsoup):
    """
       Find the Subscriber Count of the Youtuber you are looking for, but will remove the last onr because it's the not finished one.
    Will Return a list with the Subscribers in Total
    :param preparedsoup:
    :return:
    """
    from bs4 import BeautifulSoup
    import requests
    url = requests.get(preparedsoup)
    preparedsoup = BeautifulSoup(url.content, 'html.parser')
    currentSubsList = []
    subsContainer = preparedsoup.find('div', attrs={'style': 'width: 880px; float: left;'})
    subs = subsContainer.find_all('div', attrs={'style': 'width: 140px; float: left;'})
    for su in subs:
        su = str(su)
        su = su.replace('<div style="width: 140px; float: left;">', '').replace('</div>', '').replace('\n','')
        currentSubsList.append(su)

    del currentSubsList[2-1::2]
    del currentSubsList[-1]
    return currentSubsList

def findadditionalVideoViewsYT(preparedsoup):
    """
        Find the  + Video Views of the Days you are looking for, but will remove the last onr because it's the not finished one.
    Will Return a list with the additional VideoViews in Total
    :param preparedSoup:
    :return:
    """
    from bs4 import BeautifulSoup
    import requests
    url = requests.get(preparedsoup)
    preparedsoup = BeautifulSoup(url.content, 'html.parser')
    videoViewsList = []
    videoContainer = preparedsoup.find('div', attrs={'style': 'width: 880px; float: left;'})
    videoviews = videoContainer.find_all('div', attrs={'style': 'width: 85px; float: left;'})
    for vi in videoviews:
        vi = str(vi)
        vi = vi.replace('<div style="width: 85px; float: left;"><span style="color:#41a200;">', '').replace('</span></div>', '')
        videoViewsList.append(vi)
    del videoViewsList[-1]
    return videoViewsList





def findcurrentVideoViewsYT(preparedsoup):
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
    currentVideoViewsList = []
    videoViews = preparedsoup.find('div',attrs={'style':'width: 880px; float: left;'})
    views = videoViews.find_all('div',attrs={'style':'width: 140px; float: left;'})
    for su in views:
        su = str(su)
        su = su.replace('<div style="width: 140px; float: left;">', '').replace('</div>', '')
        currentVideoViewsList.append(su)

    del currentVideoViewsList[::2]
    del currentVideoViewsList[-1]
    return currentVideoViewsList


