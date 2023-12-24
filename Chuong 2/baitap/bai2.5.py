import xml.dom.minidom

# Tải tài liệu XML
dom = xml.dom.minidom.parse('sample.xml')

# Lấy danh sách các phần tử
elements = dom.getElementsByTagName('*')

# In ra tên của từng phần tử
for element in elements:
    print(f'Tên phần tử: {element.tagName}')
