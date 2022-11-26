'''
ProxyGenerator by InternalJava
github.com/InternalJava
'''

# Import required libraries
import os
import time
import random
import requests
import sys

# Generator functions
def generate_proxy(filename : str):
    proxy_url_list = [
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000&country=all&ssl=yes&anonymity=all",
    "https://www.proxy-list.download/api/v1/get?type=socks5",
    "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=5000&country=all&ssl=yes&anonymity=all"
    ]
    proxy_url = random.choice(proxy_url_list)
    try:
        proxy_file = open("bin/" + filename, "wb")
        req = requests.get(proxy_url)
        proxy_file.write(req.content)
        proxy_file.close()
        #result = open(filename).readlines()
        return "Proxy has been generated as: '{0}'".format(filename)
    except:
        return "Failed to generate proxy"

def read_proxy(filename : str):
    global proxies
    try:
        proxies = open(filename).readlines()
        return "File: '{0}' has been set as proxylist".format(proxies)
    except:
        return "Failed to get: '{0}' as list".format(filename)

def set_proxy(proxy_list : str, proxy_set : str):
    global proxy
    try:
        proxy = random.choice(proxy_set).strip().split(":")
        return "'{0}' has been splitted".format(proxy_list)
    except:
        return "Unable to set: '{0}'".format(proxy_list)

# Main functions
def main():
    try:
        filename = sys.argv[1]
        if filename.find(".") != -1:
            gen = generate_proxy(filename)
            print(gen)
            time.sleep(2)
            rd = read_proxy("bin/{0}".format(filename))
            print(rd)
        else:
            print("Input a valid file format.")
            return
    except:
        print("Usage: main.py filename (insert format in the name.)")

# Start the functions
if __name__ == "__main__":
    main()