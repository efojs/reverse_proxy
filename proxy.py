import http.server
import re
import urllib.error
import urllib.request

from bs4 import BeautifulSoup


def add_tm(soup):
    tm = "\u2122"
    pattern = re.compile(rf"\b([a-zA-Z]{{6}})(?=[^{tm}])\b")
    for string in list(soup.strings):
        if string.parent.name not in ["code", "pre"]:
            new_string = pattern.sub(r"\1" + tm, string)
            string.replace_with(new_string)
    return soup


def remove_base_url(body_str):
    base_url = Proxy.base_url
    base_url_pattern = re.compile(
        re.sub(r"(https)(://)(.*[^/])(/$)?", r"\1?\2\3/?", base_url)
    )
    return re.sub(base_url_pattern, "/", body_str)


def format_text(body):
    soup = BeautifulSoup(body, "html.parser")
    soup = add_tm(soup)
    formatted_body = remove_base_url(str(soup))
    return formatted_body.encode()


class Proxy(http.server.SimpleHTTPRequestHandler):
    base_url = "https://news.ycombinator.com"

    def do_GET(self):
        try:
            resp = urllib.request.urlopen(self.base_url + self.path)
            self.send_response(resp.status)
            self.send_header("Content-Type", resp.headers["Content-Type"])
        except urllib.error.HTTPError as e:
            self.send_error(e.code)
            return

        if "text/html" in resp.headers["Content-Type"]:
            if "charset" not in resp.headers["Content-Type"]:
                self.send_header("Content-Type", "text/html; charset=utf-8")
            body = resp.read().decode()
            formatted_body = format_text(body)
            self.end_headers()
            self.wfile.write(formatted_body)
        else:
            self.end_headers()
            self.copyfile(resp, self.wfile)


if __name__ == "__main__":
    port = 8232
    httpd = http.server.HTTPServer(("", port), Proxy)
    print(f"Hacker News proxy is served at http://localhost:{str(port)}")
    httpd.serve_forever()
