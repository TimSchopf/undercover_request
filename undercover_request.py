from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import requests

"""

@param url: the url string from which the request object is wanted
@param request_type: get or post request
@param params: parameters sent to the url
@param timeout: waiting for a response after a given number of seconds 
@return: returns a requests.Response object from given url with random user agent and random proxy
"""

# returns a request object from given url with random user agent and random proxy
def request(url:str,request_type='get',params={},timeout=1) -> requests.models.Response:
    
    # check parameter requirements
    if request_type != 'get' and request_type != 'post':
        raise ValueError("request_type must be 'get' or 'post' of type str")
        
    if type(params) is not dict:
        raise ValueError("post_params must be of type dict()")
        
    if not isinstance(timeout, int):
        raise ValueError("timeout must be of type 'int")
    
    #  disable ANY annoying exception with a fallback to default user agent if anything goes wrong
    ua = UserAgent(fallback = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-HK) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5')

    # update saved database of user agents
    # fake_useragent stores collected data at os temp dir
    print('update user agent database')
    try: 
        ua.update()
    except:
        print('user agent database update failed')
    
    print('get proxy list')
    # will contain proxies [ip, port]
    proxies = []

    # retrieve latest proxies from website
    proxies_req = requests.get(url='https://www.sslproxies.org/', headers={'user-agent': ua.random})
    proxies_req.encoding = 'utf-8'

    # create beatifulsoup instance, parse html and get section with proxy list of website
    parsed_html = BeautifulSoup(proxies_req.text, 'html.parser')
    proxies_table = parsed_html.find(id='proxylisttable')

    # save proxies from proxy list of website in the array
    for row in proxies_table.tbody.find_all('tr'):
        proxies.append({
        'ip':   row.find_all('td')[0].string,
        'port': row.find_all('td')[1].string
      })
        
    # retrieve a random index proxy
    def random_proxy_idx():
        return random.randint(0, len(proxies) - 1)
    
    print('try proxies')
    # try if proxy server is running, if not try other random proxy and user agent, try maximum x times then exit loop
    proxy_is_good = False
    i = 0
    x = 20
    while not proxy_is_good:
    
        # get dict for random proxy 
        random_proxy = proxies[random_proxy_idx()]
        random_proxy_dict = {'http': 'http://' + random_proxy['ip'] + ':' + random_proxy['port'],
                        'https': 'https://' + random_proxy['ip'] + ':' + random_proxy['port']}
        # select random user agent
        user_agent = ua.random
    
        # try to get request object from url with random user agent and random proxy
        try:
            if request_type == 'get':
                req = requests.get(url=url, headers={'user-agent': user_agent},proxies=random_proxy_dict,data=params,timeout=timeout)
            elif request_type == 'post':
                req = requests.post(url=url, headers={'user-agent': user_agent},proxies=random_proxy_dict,data=params,timeout=timeout)
            else:
                raise ValueError("request_type must be 'get' or 'post' of type str")
                
        # if anything goes wrong try again with differnt user agent and proxy
        except:
            print('ERROR','Proxy:',random_proxy,'User Agent:',user_agent)
            if i == x:
                print('All',i,'proxies are not reachable. Try again later')
                break
            i += 1
        # if everything goes right, end loop and return request object
        else:
            proxy_is_good = True
            print('SUCCESS','Proxy:',random_proxy,'User Agent:',user_agent)
    return req