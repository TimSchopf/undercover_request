# 'undercover_request' Module
Returns a requests.Response instance  of an url and uses a random proxy and a random user agent for anonymization

## Install
The `undercover_request` module can be installed from GitHub using `pip`:

`pip install git+https://github.com/TimSchopf/undercover_request`

## Usage

```python 
import undercover_request
```

@param url: the url from which the request object is wanted  (type str)  
@param request_type: 'get' or 'post' request (type str)  
@param params: parameters sent to the url (type dict())  
@param json: parameters sent to the url, parsed to json (type dict())  
@param timeout: function is waiting for a response for a given number of seconds (type int)   
@param print_status: if True print status updates (boolean)  
@return: returns a requests.Response instance from given url with random user agent and random proxy   

#### Example

```python
In[1]:

params = {
    'P_QTE_CODE': 'ENG',
    'P_QTE_PGM_CODE': '7500',
    'P_LAST_NAME': 'smith',
    'P_FIRST_NAME': '',
    'P_INITIAL': '',
    'P_LICENSE_NUM': '',
    'P_CITY': '',
    'P_COUNTY': 'LOS ANGELES',
    'P_RECORD_SET_SIZE': '50',
    'Z_ACTION': 'Find'
}

response = undercover_request.request('http://www2.dca.ca.gov/pls/wllpub/WLLQRYNA$LCEV2.ActionQuery', request_type='post', params=params,timeout=1)


Out:
update user agent database
get proxy list
try proxies
SUCCESS [Number of attempts: 2] Proxy: {'ip': '167.99.7.198', 'port': '8080'} User Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36
```
## Remark

`proxylist = number of proxies on https://www.sslproxies.org/`  

The module randomly tries a maximum of `x=len(proxylist)` proxies and then interrupts if none of the servers is reachable to avoid an endless loop. If this is the case, the request can simply be restarted shortly afterwards. It can sometimes happen that the proxies are not reachable for a short time.  

In rare cases an IndexOutOfRangeException may occur. This happens if the website of the proxylist could not be reached.  If this is the case, the request can simply be restarted shortly afterwards.

