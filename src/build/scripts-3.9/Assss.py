#!/usr/bin/python3
import optparse, os, sys, urllib.request, re  # Python 3 required

# Import BeautifulSoup module from bs4 package.
from bs4 import BeautifulSoup 

NAME, VERSION, AUTHOR, LICENSE = "ASSSS - simple vulnerability scanner", "0.1a", "TheSenPie (@TheSenPie), Sergaebi (@SergKirk)", "Public domain (FREE)"

def getAllUrl(url):
    # Get the input url web page HTML content.
    html_data = urllib.request.urlopen(url).read().decode("utf-8")
    # Create an instance of BeautifulSoup with the above HTML data.
    soup = BeautifulSoup(html_data, features='html.parser')
    # Get all HTML a tag on the web page in a list.
    tag_list = soup.find_all('a')

    full = ""

    # Loop the above tag list.
    for tag in tag_list:
        # Get the HTML a tag href attribute value.
        href_value = str(tag.get('href'))
        
        # Print out the a tag link url.
        full += f'{url}{href_value.strip()}'
    
    list = re.split(r"http", full)

    full = ""
    for a in range(1, len(list)):
        full += f'http{list[a]}\n'
    return full

def scan_page(url, output, aggression):
    if (output is None):
        output = 'output.xml'
    if (aggression is None):
        aggression = 1


    aggression = max(1, min(int(aggression), 4))
    risk = max(1, min(int(aggression), 3))

    os.system(f'whatweb -a {aggression} --log-xml={output} -q {url}')

    full = getAllUrl(url)

    with open("/tmp/endpoints", "w") as f:
        print(full, file=f)

    os.system(f'python3 ./sqlmap/sqlmap.py --forms --level {aggression} --risk {risk} --batch -m /tmp/endpoints --answers "Do you want to keep testing the others (if any)?=Y" --crawl 1')

    os.system(f'python3 ./xsstrike/xsstrike.py --seeds /tmp/endpoints --crawl -l {aggression}')

    return 'Done!'

if __name__ == "__main__":
    print("%s #v%s\n by: %s\n" % (NAME, VERSION, AUTHOR))
    parser = optparse.OptionParser(version=VERSION)
    parser.add_option("-u", "--url", dest="url", help="Target URL (e.g. \"http://www.target.com/page.php?id=1\")")
    parser.add_option("-o", "--output", dest="output", help="Output filepath.\")")
    parser.add_option("-a", "--aggression", dest="aggression", help="Output filepath.\")")

    options, _ = parser.parse_args()
    if options.url:
        result = scan_page(options.url, options.output, options.aggression)
        print("\nscan results: %s" % (result))
    else:
        parser.print_help()