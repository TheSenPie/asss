#!/usr/bin/python3
import optparse, os, sys  # Python 3 required

NAME, VERSION, AUTHOR, LICENSE = "ASSSS ( simple vulnerability scanner )", "0.1a", "TheSenPie (@TheSenPie), Sergaebi (@SergKirk) AAAASH", "Public domain (FREE)"

def scan_page(url):
    return url

# def init_options(proxy=None, cookie=None, ua=None, referer=None):
    # globals()["_headers"] = dict(filter(lambda _: _[1], ((COOKIE, cookie), (UA, ua or NAME), (REFERER, referer))))
    # urllib.request.install_opener(urllib.request.build_opener(urllib.request.ProxyHandler({'http': proxy})) if proxy else None)

if __name__ == "__main__":
    # os.system(f'echo {sys.argv[1]}')
    print("%s #v%s\n by: %s\n" % (NAME, VERSION, AUTHOR))
    parser = optparse.OptionParser(version=VERSION)
    parser.add_option("-u", "--url", dest="url", help="Target URL (e.g. \"http://www.target.com/page.php?id=1\")")
    #  parser.add_option("--data", dest="data", help="POST data (e.g. \"query=test\")")
    # parser.add_option("--cookie", dest="cookie", help="HTTP Cookie header value")
    # parser.add_option("--user-agent", dest="ua", help="HTTP User-Agent header value")
    # parser.add_option("--referer", dest="referer", help="HTTP Referer header value")
    # parser.add_option("--proxy", dest="proxy", help="HTTP proxy address (e.g. \"http://127.0.0.1:8080\")")
    options, _ = parser.parse_args()
    if options.url:
        # init_options(options.proxy, options.cookie, options.ua, options.referer)
        # init_options()
        result = scan_page(options.url)
        print("\nscan results: %s" % (result))
    else:
        parser.print_help()