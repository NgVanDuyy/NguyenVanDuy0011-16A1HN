import xml.etree.ElementTree as ET 

tree = ET.parse('employee.xml')
root = tree.getroot()
name = root.find('name') 
print(name.text)
expertise = root.find('expertise') 
print(expertise.attrib['name'])
city = root.find('city') 
print(city.text)
newexpertise = ET.Element('expertise')
newexpertise.attrib['name'] = 'XML' 
root.append(newexpertise)
tree.write('updated.xml') 