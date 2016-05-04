
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


page2 = 'this <a href="Link1.html"> es una prueba <a href="Link2.html"> jaja <a href="Link3.html"> jajjaj'


print get_all_links(page2)
