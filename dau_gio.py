staff_manager = [
    {'id': 100, 'name': 'Nguyễn Xuân Hòa', 'salary': 100.00},
    {'id': 101, 'name': 'Phạm Quỳnh Anh', 'salary': 150.00}
]

choice = 0

while choice != 5:
    choice = input('''
QUẢN LÝ NHÂN SỰ - STAFF MANAGER
1. Thêm nhân viên mới
2. Danh sách nhân viên
3. Tìm kiêm nhân viên (theo mã)
4. Xóa nhân viên khỏi hệ thông
5. Thoát chương trình
=> Mời nhập lựa chọn: _''')
    
    if not choice.isdigit():
        print('Nhập số nguyên!!!')

    else:
        choice = int(choice)
        match choice:
            case 1:
                is_true = True
                max_id = 100
                for manager in staff_manager:
                    if manager['id'] > max_id:
                        max_id = manager['id']
                
                next_id = max_id + 1

                while True:
                    manager_name = input('Tên nhân viên: ').strip()

                    manager_salary = input('Nhập lương: ')

                    if manager_name != '':
                        is_true = False
                        print('Lỗi tên không được để trống!!')
                    
                    if float(manager_salary) > 0:
                        is_true = False
                        print('Lỗi lương phải lớn hơn 0')

                    if is_true == True:
                        new_manager = {'id': next_id, 'name': manager_name, 'salary': manager_salary}
                        staff_manager.append(new_manager)
                        print(f'Thêm nhân viên thành công! ID: [{next_id}]')
                        break


            case 2:
                if not staff_manager:
                    print('Chưa có dữ liệu nhân sự!')
                else:
                    print(f"{'ID':<10}|{'TÊN NHÂN VIÊN':<25}|{'MỨC LƯƠNG':<15}")

                    for i, item in enumerate(staff_manager):
                        print(f"{item['id']:<10}|{item['name']:<25}|{item['salary']:<15}")

            case 3:
                
                check_id = input('Nhập id cần tìm: ')

                while True:
                    if not check_id.isdigit():
                        print('Hãy nhập số nguyên')
                    else:
                        break

                for item in staff_manager:
                    if check_id == item['id']:
                        print(f"{item['id']:<10}|{item['name']:<25}|{item['salary']:<15}")
                    else:
                        print(f'Không tìm thấy nhân viên có ID [{check_id}]!')
            case 4:
                check_id = input('Nhập id cần tìm: ')

                while True:
                    if not check_id.isdigit():
                        print('Hãy nhập số nguyên')
                    else:
                        break

                for i, item in enumerate(staff_manager):
                    if check_id == item['id']:
                        staff_manager.pop(i)
                    else:
                        print('Không tìm thấy nhân viên để xóa!')

            case 5:
                print('Thoát chương trình')

            case _:
                print('Nhập 1-5!!!')