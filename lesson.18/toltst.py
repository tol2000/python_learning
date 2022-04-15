import requests

j_serv = {
    "args": {
        "foo": [
            "baz",
            "bar"
        ],
        "qwe": "abc"
    },
    "data": "",
    "files": {},
    "form": {
        "foo": "bar",
        "spam": "eggs"
    },
    "headers": {
        "Accept": "*/*",
        "Content-Length": "175",
        "Content-Type": "multipart/form-data; boundary=X-INSOMNIA-BOUNDARY",
        "Host": "httpbin.org",
        "User-Agent": "insomnia/2020.4.1",
        "X-Amzn-Trace-Id": "Root=1-5f80a024-64b0f08710bc1ae3307db22f"
    },
    "json": "null",
    "origin": "188.32.239.28",
    "url": "https://httpbin.org/post?foo=baz&qwe=abc"
}

data = {
    "args": {
        "foo": [
            "baz",
            "bar"
        ],
        "qwe": "abc"
    },
    "data": "",
    "files": {},
    "form": {
        "foo": "bar",
        "spam": "eggs"
    },
    "headers": {
        "Accept": "*/*",
        "Content-Length": "175",
        "Content-Type": "multipart/form-data; boundary=X-INSOMNIA-BOUNDARY",
        "Host": "httpbin.org",
        "User-Agent": "insomnia/2020.4.1",
        "X-Amzn-Trace-Id": "Root=1-5f80a024-64b0f08710bc1ae3307db22f"
    },
    "json": "null",
    "origin": "188.32.239.28",
    "url": "https://httpbin.org/post?foo=baz&qwe=abc"
}


data1 = {
    "foo": "bar",
    "spam": "eggs"
}

data2 = {
    "foo": [
        "baz",
        "bar"
    ],
    "qwe": "abc/42"
}

data3 = {
    "foo": [f'{x+1}-{x*10}' for x in range(10)],
    "qwe": "abc/42"
}

data4 = {
    "foo": "bar",
    "qwe": "abc42"
}

headers = {
    # "Accept": "*/*",
    # "Content-Length": "175",
    # "Content-Type": "multipart/form-data",
    # "Content-Type": "application/json",
    # "User-Agent": "Tolyan",
}

a = range(100000)


def main():
    response = requests.post(url='https://httpbin.org/post?tolyan=molodets', data=data4, headers=headers)
    print(response.text)
    print(30*'-', 'data')
    print(response.json()['data'])
    print(30 * '-', 'form')
    print(response.json()['form'])


if __name__ == '__main__':
    main()
