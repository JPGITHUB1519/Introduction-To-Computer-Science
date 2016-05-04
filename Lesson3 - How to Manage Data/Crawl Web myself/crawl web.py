
# leer pagina
def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''

#buscar links

def get_next_target(page):

     start_link = page.find('<a href=')

     #no encontro link

     if start_link == -1:

        return None,0

     start_quote= page.find('"',start_link)
     end_quote = page.find('"',start_quote+1)
     url = page[start_quote +1 : end_quote]

     return url, end_quote

def get_all_links(page):
    
    links = []

    while True:
        url, endpos = get_next_target(page)

        if url : 

            links.append(url)
            page = page[endpos:]
        else:

            break

    return links

def test (crawled, page) :

    if page not in crawled :

        return True

    else :

        return False



def crawl_web(seed) :

    tocrawl = [seed]
    crawled = []

    cont = 0

    while len(tocrawl) > 0 :

        if test(crawled, tocrawl[cont]) :

            crawled.append(tocrawl[cont])
            aux = tocrawl[cont]

            tocrawl.pop(cont)

            tocrawl = tocrawl + get_all_links(getpage(tocrawl[cont]))
    return crawled          










page2 = 'this <a href="Link1.html"> es una prueba <a href="Link2.html"> jaja <a href="Link3.html"> jajjaj'


print get_all_links(page2)
