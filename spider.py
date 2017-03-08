import lxml.html
import urllib.request
def test1():    
    broken_html = '<ul class=country><li>Area<li>Population</ul>'
    tree = lxml.html.fromstring(broken_html)
    fixed_html = lxml.html.tostring(tree, pretty_print=True)
    print(fixed_html)
def test2():
    url="http://example.webscraping.com/places/view/UnitedKingdom239"
    html=urllib.request.urlopen(url).read()
    tree = lxml.html.fromstring(html)
    x = tree.xpath('/html/body/div[2]/section/div/form/table/tr[*]/td[1]/label/text()')
    print(x)
def test3():
    html='<html><body><x>TEXT<br/>TAIL1</x><y>TEXT<br/>TAIL</y></body></html>'
    tree = lxml.html.fromstring(html)
    print(tree)
    x = tree.xpath("/html/body/x/text()")
    print(x)
def test4():
    import json
    url="http://example.webscraping.com/ajax/search.json?&search_term=d&page_size=10&page=0"
    html=urllib.request.urlopen(url).read()
    json_string=json.dumps(str(html))
    ajax = json.loads(json_string)['num_pages']
if __name__ == '__main__':
   while True:
       x=1/0
       try:
           x=1/0
       except:
           print("xxx")


