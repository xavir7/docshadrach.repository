import urllib
from xbmctorrent import plugin
from xbmctorrent.scrapers import scraper
from xbmctorrent.ga import tracked
from xbmctorrent.caching import cached_route
from xbmctorrent.utils import ensure_fanart
from xbmctorrent.library import library_context


BASE_URL = plugin.get_setting("base_btdigg")
HEADERS = {
    "Referer": BASE_URL,
}
SORT_RELEVANCE = 0
SORT_POPULARITY = 1
SORT_ADDTIME = 2
SORT_SIZE = 3
SORT_FILES = 4


@scraper("[COLOR yellow]BTDigg - DHT Search Engine [Pulsar mod][/COLOR]", "%s/logo.png" % BASE_URL)
@plugin.route("/btdigg")
@ensure_fanart
@tracked
def btdigg_index():
    plugin.redirect(plugin.url_for("btdigg_search"))


@plugin.route("/btdigg/search/<query>/<sort>/<page>")
@library_context
@ensure_fanart
@tracked
def btdigg_page(query, sort, page):
    from bs4 import BeautifulSoup
    from xbmctorrent.utils import url_get

    html_data = url_get("%s/search" % BASE_URL, headers=HEADERS, params={
        "order": sort,
        "q": query,
        "p": page,
    })
    soup = BeautifulSoup(html_data, "html5lib")
    name_nodes = soup.findAll("td", "torrent_name")
    attr_nodes = soup.findAll("table", "torrent_name_tbl")[1::2]

    for name_node, attr_node in zip(name_nodes, attr_nodes):
        attrs = attr_node.findAll("span", "attr_val")
        title = "%s (%s, DLs:%s)" % (name_node.find("a").text, attrs[0].text, attrs[2].text)
        magnet_link = urllib.quote_plus(attr_node.find("a")["href"].encode("utf-8"))
        yield {
            "label": title,
            "path": "plugin://plugin.video.pulsar/play?uri=" + magnet_link,
            # "path": plugin.url_for("play", uri=attr_node.find("a")["href"]),
            "is_playable": True,
        }
    yield {
        "label": ">> Next page",
        "path": plugin.url_for("btdigg_page", query=query, sort=sort, page=int(page) + 1),
        "is_playable": False,
    }


@plugin.route("/btdigg/search")
@tracked
def btdigg_search():
    query = plugin.request.args_dict.pop("query", None)
    if not query:
        query = plugin.keyboard("", "XBMCtorrent - BTDigg - Search")
    if query:
        plugin.redirect(plugin.url_for("btdigg_page", query=query, sort=SORT_POPULARITY, page=0, **plugin.request.args_dict))
