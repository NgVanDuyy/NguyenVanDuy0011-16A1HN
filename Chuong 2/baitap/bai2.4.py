import xml.dom.minidom

# Tải tài liệu XML
dom = xml.dom.minidom.parse('sample.xml')

# Lấy thông tin về công ty
company_name = dom.getElementsByTagName('name')[0].firstChild.data
print(f'Tên công ty: {company_name}')

# Lấy thông tin về các nhân viên
staff_elements = dom.getElementsByTagName('staff')
print('Danh sách nhân viên:')
for staff in staff_elements:
    staff_id = staff.getAttribute('id')
    staff_name = staff.getElementsByTagName('name')[0].firstChild.data
    staff_salary = staff.getElementsByTagName('salary')[0].firstChild.data
    print(f'ID: {staff_id}, Tên nhân viên: {staff_name}, Lương: {staff_salary}')
