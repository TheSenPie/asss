# asss
Cool scanner that can scan hosts for potential vulnerabilities.

Goal of the project:

We are planning to make a vulnerability scanning tool for scanning web applications. At its core, it will be a local server that will perform the scans. The scanner will perform port scanning to determine which hosts are alive and which ports are open on those hosts. Then it has a service detection, which will find out which applications are running on those ports, the version number, and their names. Then we have the vulnerability identification, where the scanner will compare what it discovers about each service detected on each host and compare against a database of known vulnerabilities of those applications and version numbers. Based on that information, the scanner will further identify if there are false positives or if that vulnerability actually exists. In a sense, it will try to look up for top 10 OWASP vulnerabilities ( but for now, finding XSS and SQLi vulnerabilities will suffice ). Finally, if time allows, the scanner will also have a GUI component in the browser where the user can see the report in a beautiful format.

We plan to use nmap under the hood to perform a host scan. Afterward, we will use public vulnerability databases to compare the application versions and see if they contain a threat. Afterward, to find XSS and SQLi issues on the host, we will use crawler apps and scrappers to play with the host's request and see if we can inject any malicious input, which will result in a different response by the host. Finally, for the GUI, we plan to use HTML and JS and make a simple browser app where all the reports will be presented.

Recources:
Vulnerability Database - https://security.snyk.io/

Vulnerability Database - https://vuldb.com/

Inspiration - https://www.tenable.com/products/nessus

Inspiration - https://subgraph.com/vega/

Tools - https://nmap.org/

Java

JS
