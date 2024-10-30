def main_menu():
    print("--- 人事資料管理系統 ---")
    print("1. 新增資料")
    print("2. 查詢資料")
    print("3. 修改資料")
    print("4. 刪除資料")
    print("5. 顯示所有資料")
    print("6. 退出系統")
    print("------------------------")


def display_records(records):
    if not records:
        print("目前沒有任何資料")
    else:
        print("\n部門\t	姓名\t	年齡\t	手機")
        print("----------------------------------------")
        for record in records:
            print(f"{record['部門']}		{record['姓名']}		{record['年齡']}		{record['手機']}")
    print()


def main():
    records = []
    while True:
        main_menu()
        choice = input("請選擇功能: ")

        if choice == '1':
            while True:
                部門 = input("請輸入部門: ")
                姓名 = input("請輸入姓名: ")
                年齡 = input("請輸入年齡: ")
                手機 = input("請輸入手機號碼: ")
                record = {'部門': 部門, '姓名': 姓名, '年齡': 年齡, '手機': 手機}
                records.append(record)
                是否繼續 = input("是否繼續新增資料? (y/n): ")
                if 是否繼續.lower() != 'y':
                    break

        elif choice == '2':
            姓名 = input("請輸入要查詢的姓名: ")
            found_records = list(filter(lambda record: record['姓名'] == 姓名, records))
            if not found_records:
                print("查無此人。")
            else:
                print("\n--- 查詢結果 ---")
                display_records(found_records)

        elif choice == '3':
            姓名 = input("請輸入要修改的姓名: ")
            found_records = list(filter(lambda record: record['姓名'] == 姓名, records))
            if not found_records:
                print("查無此人。")
            else:
                record = found_records[0]
                print("\n當前資料:")
                display_records([record])
                print("1. 修改部門")
                print("2. 修改姓名")
                print("3. 修改年齡")
                print("4. 修改手機")
                field_choice = input("請選擇要修改的欄位: ")
                if field_choice == '1':
                    record['部門'] = input("請輸入新的部門: ")
                elif field_choice == '2':
                    record['姓名'] = input("請輸入新的姓名: ")
                elif field_choice == '3':
                    record['年齡'] = input("請輸入新的年齡: ")
                elif field_choice == '4':
                    record['手機'] = input("請輸入新的手機號碼: ")
                print("\n--- 更新後的資料 ---")
                display_records([record])

        elif choice == '4':
            姓名 = input("請輸入要刪除的姓名: ")
            found_records = list(filter(lambda record: record['姓名'] == 姓名, records))
            if not found_records:
                print("查無此人。")
            else:
                record = found_records[0]
                confirm = input(f"確定要刪除 {record['姓名']} 的資料嗎? (y/n): ")
                if confirm.lower() == 'y':
                    records.remove(record)
                    print(f"{record['姓名']} 的資料已刪除。")
                print("\n--- 剩餘的所有資料 ---")
                display_records(records)

        elif choice == '5':
            print("\n--- 所有資料 ---")
            display_records(records)

        elif choice == '6':
            print("系統已退出。")
            break

        else:
            print("無效選擇，請重新選擇。")

if __name__ == "__main__":
    main()
