import http.server
import re
import urllib.request

from bs4 import BeautifulSoup


def add_tm(soup):
    pattern = re.compile(r"\b([a-zA-Z]{6})\b")
    for string in list(soup.strings):
        if string.parent.name not in ["code", "pre"]:
            tm = "\u2122"
            new_string = pattern.sub(r"\1" + tm, string)
            string.replace_with(new_string)


def format_text(body):
    soup = BeautifulSoup(body, "html.parser")
    add_tm(soup)
    return str(soup).encode()


class Proxy(http.server.SimpleHTTPRequestHandler):
    base_url = "https://news.ycombinator.com"

    def do_GET(self):
        resp = urllib.request.urlopen(self.base_url + self.path)
        self.send_response(resp.status)
        self.send_header("Content-Type", resp.headers["Content-Type"])
        self.end_headers()

        if "text/html" in resp.headers["Content-Type"]:
            body = resp.read().decode()
            formated_body = format_text(body)
            self.wfile.write(formated_body)
        else:
            self.copyfile(resp, self.wfile)


if __name__ == "__main__":
    port = 8232
    httpd = http.server.HTTPServer(("", port), Proxy)
    print(f"Hacker News proxy is served at http://localhost:{str(port)}")
    httpd.serve_forever()
