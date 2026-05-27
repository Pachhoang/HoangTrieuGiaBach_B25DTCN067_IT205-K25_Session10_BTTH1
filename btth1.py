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
        total_qty = 0
        total_price = 0

        print("---- CHI TIẾT GIỎ HÀNG ----")
        print("STT | Mã SP | Tên Sản Phẩm | SL | Đơn Giá | Thành Tiền")
        print("-------------------------------------------------------")

        for index, item in enumerate(cart_items, start=1):
            product_id = item[0]
            product_name = item[1]
            quantity = item[2]
            unit_price = item[3]

            item_total = quantity * unit_price

            total_qty += quantity
            total_price += item_total

            print(
                f"{index} | {product_id} | {product_name} | "
                f"{quantity} | {unit_price} | {item_total}"
            )

        print("-------------------------------------------------------")
        print(f"Tổng số lượng sản phẩm trong giỏ: {total_qty}")
        print(f"TỔNG TIỀN THANH TOÁN: {total_price:,}đ")

    elif choice == 2:
        product_id = input("Nhập mã sản phẩm mới: ").strip()
        product_name = input("Nhập tên sản phẩm mới: ").strip()
        quantity = int(input("Nhập số lượng sản phẩm mới: "))
        unit_price = int(input("Nhập đơn giá sản phẩm mới: "))

        found = False

        for item in cart_items:
            if item[0] == product_id:
                item[2] += quantity
                found = True
                break

        if not found:
            cart_items.append([
                product_id,
                product_name,
                quantity,
                unit_price
            ])
    elif choice == 3:
        update_id = input(
            "Nhập mã sản phẩm cần cập nhật số lượng: "
        ).strip()

        qty_input = input("Nhập số lượng mới: ").strip()

        if qty_input.startswith('-') and qty_input[1:].isdigit():
            print("Số lượng không được là số âm. Thao tác bị hủy.")
            continue

        elif not qty_input.isdigit():
            print("Số lượng phải là số nguyên. Thao tác bị hủy.")
            continue

        new_qty = int(qty_input)

        if new_qty == 0:
            print("Số lượng phải lớn hơn 0. Thao tác bị hủy.")
            continue

        found = False

        for item in cart_items:
            if item[0] == update_id:
                item[2] = new_qty
                found = True

                print(
                    f"Đã cập nhật số lượng của "
                    f"{update_id} thành {new_qty}."
                )
                break

        if not found:
            print(
                f"Mã sản phẩm '{update_id}' "
                f"không tồn tại trong giỏ hàng."
            )

    elif choice == 4:
        delete_id = input("Nhập mã sản phẩm cần xóa: ").strip()

        found = False

        for index in range(len(cart_items)):
            if cart_items[index][0] == delete_id:
                removed_item = cart_items.pop(index)

                found = True

                print(
                    f"Đã xóa sản phẩm "
                    f"'{removed_item[1]}' khỏi giỏ hàng."
                )
                break

        if not found:
            print(
                f"Mã sản phẩm '{delete_id}' "
                f"không tồn tại trong giỏ hàng."
            )

    elif choice == 5:
        print("Thoát khỏi chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")