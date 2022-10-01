from data import score_board

dataQ = ([0, "Yasuho Hirose", 19, 9.9], 
        [1, "Ashley Graham", 18, 8.5],
        [2, "Allan Bilfaqih", 20, 6.9],
        [3, "Elden John", 24, 10.0],
        [4, "Denji Dennis", 16, 2.0])

selected_data = 0

print("""
===========================
======= Score Board =======
===========================
""")

while True:

    sb = score_board(dataQ,
        dataQ[selected_data][1],
        dataQ[selected_data][2],
        dataQ[selected_data][3])

    sb.choices()
    inpChoice = input("\n[=] Select Menu : ")

    if(inpChoice == "1"):
        sb.showTable(selected_data)

    elif(inpChoice == "2"):
        inpSelect = input("\n[=] Select Data : ")
        lened = len(dataQ) - 1

        if(inpSelect.isdigit()):
            if(int(inpSelect)> lened):
                print(f"[!] There's no #{inpSelect}! Data #0 selected instead.\n")
                selected_data = 0
            else:
                selected_data = int(inpSelect)
                print(f"\n[i] Selected data : {selected_data}\n")
        elif(inpSelect == ""):
            print("[!] No data is selected! Data #0 selected instead.\n")
            selected_data = 0
        else:
            print("[!] String is not allowed! Data #0 selected instead.\n")
            selected_data = 0

    elif(inpChoice == "3"):
        sb.showSelected(selected_data)

    elif(inpChoice == "4"):
        sb.editAttr1(selected_data)

    elif(inpChoice == "5"):
        sb.editAttr2(selected_data)

    elif(inpChoice == "6"):
        sb.editAttr3(selected_data)

    elif(inpChoice == "0"):
        print("""
===========================
======== Good Bye! ========
===========================
""")
        exit()

    else:
        print("[!] Invalid option!\n")