#!/usr/bin/python3
import optparse, os, sys  # Python 3 required

NAME, VERSION, AUTHOR, LICENSE = "ASSSS - simple vulnerability scanner", "0.1a", "TheSenPie (@TheSenPie), Sergaebi (@SergKirk)", "Public domain (FREE)"

def scan_page(url, output, aggression):
    if (output is None):
        output = 'output.xml'
    if (aggression is None):
        aggression = 1
    os.system(f'whatweb -a {aggression} --log-xml={output} -q {url}')
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