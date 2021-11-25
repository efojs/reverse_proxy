# Local reverse proxy
Shows https://news.ycombinator.com at http://localhost:8232  
Adds "TM" sign to all 6-letter words.  

## [proxy.py](proxy.py)
Main tools are `http.server` and `BeautifulSoup`  

## Usage
Install and run:  
```bash
# install
$ git clone https://github.com/efojs/ivelum
$ cd ivelum
$ pipenv install

# run
$ python proxy.py # should print:
Hacker News proxy is served at http://localhost:8232

```
Visit http://localhost:8232/  

## Test
```
$ pytest
```

## Disclaimer
Made for educational purposes. Use with caution. No warranties implied
