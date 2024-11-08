import xml.dom.minidom as minidom


xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
valute_dict = {}

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'NumCode':
                if child.firstChild.nodeType == 3:
                    NumCode = child.firstChild.data
            if child.tagName == 'CharCode':
                if child.firstChild.nodeType == 3:
                    CharCode = child.firstChild.data
    valute_dict[NumCode] = CharCode

#for key in books_dict.keys():
    #print(key, books_dict[key])

print(valute_dict)


xml_file.close()