import urllib.request
import xml.etree.ElementTree as ET


class AtomFeed:
    def __init__(self, url):
        xml_text = urllib.request.urlopen(url).read()
        self.root = ET.fromstring(xml_text)
        self.ns = {'atom': 'http://www.w3.org/2005/Atom'}

    @property
    def title(self):
        return self._element_text('atom:title')

    @property
    def subtitle(self):
        return self._element_text('atom:subtitle')

    @property
    def updated(self):
        return self._element_text('atom:updated')

    @property
    def id(self):
        return self._element_text('atom:id')

    @property
    def rights(self):
        return self._element_text('atom:rights')

    @property
    def entries(self):
        elements = self.root.findall('atom:entry', self.ns)
        return [AtomFeedEntry(element) for element in elements]

    def _element_text(self, xpath):
        element = self.root.find(xpath, self.ns)
        if element == None:
            return None
        return element.text


class AtomFeedEntry:
    def __init__(self, element):
        self.entry = element
        self.ns = {'atom': 'http://www.w3.org/2005/Atom'}

    @property
    def title(self):
        return self._element_text('atom:title')

    @property
    def updated(self):
        return self._element_text('atom:updated')

    @property
    def id(self):
        return self._element_text('atom:id')

    @property
    def author(self):
        return self._element_text('atom:author/atom:name')

    @property
    def content(self):
        return self._element_text('atom:content')

    @property
    def link(self):
        return self._element_attr('atom:link', 'href')

    def _element_text(self, xpath):
        element = self.entry.find(xpath, self.ns)
        if element == None:
            return None
        return element.text

    def _element_attr(self, xpath, attr_name):
        element = self.entry.find(xpath, self.ns)
        if element == None:
            return None
        return element.get(attr_name)
