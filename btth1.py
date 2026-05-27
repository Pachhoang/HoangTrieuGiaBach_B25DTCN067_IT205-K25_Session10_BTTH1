cart_items = [
         ["P001", "Dien thoai iPhone 15", 1, 25000000],
         ["P002", "Op lung Silicon", 2, 150000]
]
while True:
    print("=========================================")
    print("      SHOPEE CART MANAGEMENT SYSTEM      ")
    print("=========================================")
    print("1. Xem chi tiết giỏ hàng & Tính tổng tiền")
    print("2. Thêm sản phẩm mới / Cộng dồn số lượng ")
    print("3. Cập nhật số lượng của một sản phẩm    ")
    print("4. Xóa sản phẩm khỏi giỏ hàng            ")
    print("5. Thoát chương trình                    ")
    print("=========================================")
    choice = int(input("Mời bạn chọn chức năng (1-5): "))
    
    if choice == 1:
        cart_total = 0
        total_payment = 0
        print("----CHI TIẾT GIỎ HÀNG----")
        print("SST | Mã SP | Tên Sản Phẩm | SL | Đơn Giá | Thành Tiền")
        print("------------------------------------------------------")
        for index, id_order in enumerate(cart_items, start=1):
            product_id = id_order[0]
            product_name = id_order[1]
            quantity = id_order[2]
            price = id_order[3]
            total = price * quantity
            cart_total += quantity
            total_payment += total
            print(f"{index} | {product_id} | {product_name} | {quantity} | {price} | {total}")
            
        print("------------------------------------------------------")
        print(f"Tổng số lượng sản phẩm trong giỏ: {cart_total}")
        print(f"TỔNG TIỀN THANH TOÁN {total_payment:,}đ")
        
    elif choice == 2:
        new_product_id = input("Nhập mã sản phẩm mới: ")
        new_product_name = input("Nhập tên sản phẩm mới: ")
        new_product_quantity = int(input("Nhập số lượng sản phẩm mới: "))
        new_product_price = int(input("Nhập đơn giá sản phẩm mới: "))

        is_found = False
        for item in cart_items:
            if new_product_id == item[0]:
                item[2] += new_product_quantity
                is_found = True
                break 
        if is_found == False:
            cart_items.append([new_product_id, new_product_name, new_product_quantity, new_product_price])
            
    elif choice == 3:
        update_id = input("Nhập mã sản phẩm cần cập nhật số lượng: ").strip()
        
        # Nhập và kiểm tra Số lượng mới
        qty_input = input("Nhập số lượng mới: ").strip()
        if qty_input.startswith('-') and qty_input[1:].isdigit():
            print("Số lượng không được là số âm. Thao tác bị hủy.")
            continue
        elif not qty_input.isdigit():
            print("Số lượng phải là số nguyên. Thao tác bị hủy.")
            continue
            
        new_quantity = int(qty_input)
        if new_quantity == 0:
            print("Số lượng phải lớn hơn 0. Thao tác bị hủy.")
            continue

        is_found = False
        for item in cart_items:
            if item[0] == update_id:
                item[2] = new_quantity
                is_found = True
                print(f"Đã cập nhật số lượng của {update_id} thành {new_quantity}.")
                break
                
        if not is_found:
            print(f"Mã sản phẩm '{update_id}' không tồn tại trong giỏ hàng.")
            
    elif choice == 4:
        delete_id = input("Nhập mã sản phẩm cần xóa: ").strip()
        is_found = False
        for i in range(len(cart_items)):
            if cart_items[i][0] == delete_id:
                deleted_item = cart_items.pop(i) 
                is_found = True
                print(f"Đã xóa sản phẩm '{deleted_item[1]}' khỏi giỏ hàng.")
                break
        if not is_found:
            print(f"Mã sản phẩm '{delete_id}' không tồn tại trong giỏ hàng.")
            
    elif choice == 5:
        print("Thoát khỏi chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")