staff_list = []
next_id = 101

while True:
    print('''
=======================================
    QUẢN LÝ NHÂN SỰ - STAFF MANAGER
=======================================
    1. Thêm nhân viên mới
    2. Danh sách nhân viên
    3. Tìm kiếm nhân viên (theo ma)
    4. Xóa nhân viên khỏi hệ thống
    5. Thóat chương trình
=======================================''')
    choice = input("Nhập lựa chọn của bạn: ")
    if not choice.isdigit():
        print("Vui lòng nhập từ 1 đến 5!")
        continue
    match choice:
        case "1":
            name = input("Nhập tên nhân viên: ").strip()
            while name == "":
                print("-> Tên nhân viên không được để trống!!!")
                name = input("Nhập lại tên nhân viên: ").strip()
            salary = input("Nhập mức lương: ")
            while True:
                if salary == "":
                    print("Lương không được để trống!")
                    salary = input("Nhập lại mức lương: ")
                    continue
                salary = float(salary)
                if salary <= 0:
                    print("-> Lương phải lớn hơn 0!!!")
                    salary = input("Nhập lại mức lương: ")
                    continue
                break
            staff = {
                "id": next_id,
                "name": name,
                "salary": salary
            }
            staff_list.append(staff)
            print(f"Thêm nhân viên thành công! ID: {next_id}")
            next_id += 1
        case "2":
            if len(staff_list) == 0:
                print("Chưa có dữ liệu nhân sự!")
            else:
                print("-" * 60)
                print(f"| {'ID':<5} | {'Tên Nhân Viên':<25} | {'Lương':<15} |")
                print("-" * 60)
                for item in staff_list:
                    print(
                        f"| {item['id']:<5} "
                        f"| {item['name']:<25} "
                        f"| {item['salary']:<15,.2f} |"
                    )
                print("-" * 60)
        case "3":
            search_id = input("Nhập ID cần tìm: ")
            if not search_id.isdigit():
                print("ID phải là số!")
                continue
            search_id = int(search_id)
            found = False
            for item in staff_list:
                if item["id"] == search_id:
                    print("Thông tin nhân viên:")
                    print(item)
                    found = True
                    break
            if found == False:
                print(f"Không tìm thấy nhân viên có ID {search_id}!")
        case "4":
            delete_id = input("Nhập ID cần xóa: ")
            if not delete_id.isdigit():
                print("ID phải là số!")
                continue
            delete_id = int(delete_id)
            found = False
            for item in staff_list:
                if item["id"] == delete_id:
                    staff_list.remove(item)
                    print(f"Đã xóa nhân viên ID {delete_id} thành công!")
                    found = True
                    break
            if found == False:
                print("Không tìm thấy nhân viên để xóa!")
        case "5":
            print("=> Bạn đã thoát chương trình!!!")
            break
        case _:
            print("-> Vui lòng nhập từ 1 đến 5!!!")