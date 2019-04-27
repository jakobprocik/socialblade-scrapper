



def findSFollowerIncreaseTW(preparedsoup):
    from bs4 import BeautifulSoup
    import requests
    url = requests.get(preparedsoup)
    preparedsoup = BeautifulSoup(url.content, 'html.parser')
    """
    Find the last 14 Days Follower increase but will remove the last because it's the not finished one.
    Will Return a list with the Follower Count
    :param preparedsoup:
    :return:
    """
    followerList = []
    preparedsoup = preparedsoup.find('div', attrs={'style': 'width: 1260px; margin: 20px auto; padding:'})
    subbbs = preparedsoup.find_all('div', attrs={'style': 'width: 100px; float: left;'})
    for su in subbbs:
        su = str(su)
        su = su.replace('<div style="width: 100px; float: left;"><span style="color:#41a200;">', '').replace(
            '</span></div>', "")
        followerList.append(su)
    del followerList[-1]
    return followerList



def findcurrentFollowerTW(preparedsoup):
    from bs4 import BeautifulSoup
    import requests
    url = requests.get(preparedsoup)
    preparedsoup = BeautifulSoup(url.content, 'html.parser')
    """
       Find the Follower Count of the Twitter User you are looking for, but will remove the last onr because it's the not finished one.
    Will Return a list with the Follower in Total
    :param preparedsoup:
    :return:
    """
    curFollower = []
    preparedsoup = preparedsoup.find('div', attrs={'style': 'width: 1260px; margin: 20px auto; padding:'})
    folower = preparedsoup.find_all('div', attrs={'style': 'width: 150px; float: left;'})
    for su in folower:
        su = str(su)
        su = su.replace('<div style="width: 150px; float: left;">', '').replace('</div>', "")
        curFollower.append(su)
    del curFollower[-1]
    return curFollower



def findDateTW(preparedsoup):
    from bs4 import BeautifulSoup
    import requests
    url = requests.get(preparedsoup)
    preparedsoup = BeautifulSoup(url.content, 'html.parser')
    """
    Find the dates of the counts you are looking for but will remove the last onr because it's the not finished one.
    Will Return a list with the Dates
    :param preparedsoup:
    :return:
    """
    dateList = []
    preparedsoup = preparedsoup.find('div', attrs={'style': 'width: 1260px; margin: 20px auto; padding:'})
    subbbs = preparedsoup.find_all('div', attrs={'style': 'float: left; width: 85px;'})
    for su in subbbs:
        su = str(su).replace('<div style="float: left; width: 85px;">', '').replace('</div>', '')
        dateList.append(su)
    del dateList[-1]
    return dateList

