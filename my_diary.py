from datetime import datetime
entries = []
def write_entry():
    now = datetime.now()
    date_time = now.strftime("%d-%m-%Y %H:%M:%S")
    entry = input("write a diary: ")
    diary_entry =f"{date_time}|{entry}"
    entries.append(diary_entry)
    with open("diary,txt","a")as file:
        file.write(diary_entry +"\n")
    print("entry saved!")
def read_entry():
    try:
        with open("diary.txt","r")as file:
            print("\n MY DIARY\n")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("your diary is empty")
while True:
    print("\n==== my presonal dairy====")
    print("1.write today entry")
    print("2.read my diary")
    print("3.exit")
    choice =input("choose.")
    if choice =="1":
        write_entry()
    elif choice =="2":
        read_entry()
    elif choice =="3":
        print("see you tommorow")
        break
    else:
        print("invalid choice.")