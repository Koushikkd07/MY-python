import json
import requests
import sys


"""                                     _________REQUESTS________
The requests package in Python is primarily used for making HTTP requests. It includes several key functions that cover most common HTTP request methods. Here are the primary functions:

**requests.get(url, params=None, kwargs)
Sends a GET request.

**requests.post(url, data=None, json=None, kwargs)
Sends a POST request.

**requests.put(url, data=None, kwargs)
Sends a PUT request.

**requests.delete(url, kwargs)
Sends a DELETE request.

**requests.head(url, kwargs)
Sends a HEAD request, which retrieves the headers only.

**requests.options(url, kwargs)
Sends an OPTIONS request, which asks the server for supported HTTP methods.

**requests.patch(url, data=None, kwargs)
Sends a PATCH request, which is used for partial updates.

                                                    Other Utility Functions:
                                In addition to the above, requests also provides the following utility functions:

**requests.request(method, url, kwargs)
Constructs and sends a Request. This is the lower-level interface that the other HTTP methods use internally. You can use it to send requests with any HTTP method.

requests.Session()
A session object allows you to persist certain parameters across requests, like cookies and headers, which can improve performance.

requests.utils.get_unicode_from_response(response)
Returns the text of a Response object in the proper Unicode encoding.

requests.utils.get_encoding_from_headers(headers)
Extracts the encoding from a given HTTP header.

                                            Other Commonly Used Attributes:
requests.Response: Represents the response to a request, which includes data like status code, headers, and content.
requests.Timeout: Specifies a timeout for the request.
    """
    
    
# Example usage of the requests library
if len(sys.argv)!=2:
    sys.exit()
    
response= requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
data=response.json()
for result in data["results"]:
    print(result["trackName"])
