# 'undercover_request' Module
Returns an requests.Response instance  of an url and uses a random proxy and a random user agent for anonymization

## Install
The `undercover_request` module can be installed from GitHub using `pip`:

`pip install git+https://github.com/TimSchopf/undercover_request`

## Usage

```python 
import undercover_request
```

@param url: the url string from which the request object is wanted  
@param request_type: get or post request  
@param params: parameters sent to the url  
@param timeout: waiting for a response after a given number of seconds   
@return: returns a requests.Response object from given url with random user agent and random proxy  

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
SUCCESS Proxy: {'ip': '31.192.138.224', 'port': '53281'} User Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36
```
## Remark

The module randomly tries a maximum of `x=20` proxies and then interrupts if none of the servers is reachable to avoid an endless loop. If this is the case, the request can simply be restarted shortly afterwards. It can sometimes happen that the proxies are not reachable for a short time. 


