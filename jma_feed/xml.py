import urllib.request
import xml.etree.ElementTree as ET


class XmlDocument:
    def __init__(self, target, ns_map):
        self.ns_map = ns_map

        if isinstance(target, ET.Element):
            self.root = target
        elif isinstance(target, str):
            try:
                xml_text = urllib.request.urlopen(target).read()
                self.root = ET.fromstring(xml_text)
            except ValueError:
                pass
        else:
            raise ValueError('target parameter can take only Element or URL.')

    def _element(self, *xpaths):
        for xpath in xpaths:
            element = self.root.find(xpath, self.ns_map)
            if element is not None:
                return element
        return None

    def _elements(self, *xpaths):
        for xpath in xpaths:
            elements = self.root.findall(xpath, self.ns_map)
            if elements:
                return elements
        return None

    def _element_text(self, xpath):
        element = self._element(xpath)
        if element == None:
            return None
        return element.text

    def _element_attr(self, xpath, attr_name):
        element = self._element(xpath)
        if element == None:
            return None
        return element.get(attr_name)
