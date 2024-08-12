import requests, argparse

parser = argparse.ArgumentParser(
                    prog='Header Tester - By Jatin Mandliya',
                    description='Displays missing security headers and present security headers with its values. Provide list consist list of URLs. Also provide cookie to test headers for URLs which are available after login')

parser.add_argument('filename')
parser.add_argument('-c','--cookie') 

args = parser.parse_args()

urls = open(args.filename,"r")

required_headers = ["strict-transport-security","x-content-type-options","x-frame-options","content-security-policy","x-content-type-options","x-xss-protection","referrer-policy","access-control-allow-origin"]

print("\nLegal disclaimer: Usage of this tool for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program")

for url in urls.readlines():
    print(f"\n\nFetching from {url}")

    response = requests.get(url,headers={"Cookie":args.cookie})

    if response.status_code == 200:
        # print(response.headers)
        print("\nMissing headers")
        for header in required_headers:
            if header not in response.headers:
                print(header)

        print("\nPresent headers with values")
        for header in required_headers:
            if header in response.headers:
                print(header+": "+response.headers[header])
    else:
        print(f"Non-success status code: {response.reason}")

urls.close()


