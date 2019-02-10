from jma_feed.xml import XmlDocument


class Report(XmlDocument):
    def __init__(self, target):
        super(Report, self).__init__(
            target,
            {
                'jmx': 'http://xml.kishou.go.jp/jmaxml1/',
                'jmx_ib': 'http://xml.kishou.go.jp/jmaxml1/informationBasis1/',
                'jmx_eb': 'http://xml.kishou.go.jp/jmaxml1/jmx.xsd',
                'jmx_add': 'http://xml.kishou.go.jp/jmaxml1/addition1/',
                'jmx_mete': 'http://xml.kishou.go.jp/jmaxml1/body/meteorology1/',
                'jmx_seis': 'http://xml.kishou.go.jp/jmaxml1/body/seismology1/',
                'jmx_volc': 'http://xml.kishou.go.jp/jmaxml1/body/volcanology1/',
            },
        )

    @property
    def control(self):
        element = self._element('jmx:Control')
        return element

    @property
    def head(self):
        element = self._element('jmx_ib:Head')
        return element

    @property
    def body(self):
        element = self._element('jmx_mete:Body', 'jmx_seis:Body', 'jmx_volc:Body')
        return element
