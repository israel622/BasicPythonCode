import urllib.request as urllib

def checker(url):
    print('checking connectivity')

    response = urllib.urlopen(url)


    print('status code:', response.getcode())
print('this is a site connectivity checker')
input_url = input('enter url: ')

checker(input_url)



