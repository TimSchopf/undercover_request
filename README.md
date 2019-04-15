# 'undercover_request' Package
Returns the request object of an url and uses a random proxy and a random user agent for anonymization

## Install
The `undercover_request` package can be installed from GitHub using `pip`:

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

