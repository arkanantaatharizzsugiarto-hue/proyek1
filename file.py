# 1. Membaca dan menampilkan isi file saat ini
try:
    with open('quotes.txt', "r", encoding="UTF-8") as file:
        print("--- Isi File Saat Ini ---")
        for line in file:
            print(line.strip())
        print("-------------------------\n")

except FileNotFoundError:
    print("File 'quotes.txt' belum ada. File baru akan dibuat jika kamu menambah quote.\n")


# 2. Loop untuk menambah quote
while True:
    answer = input("Ingin menambah quote baru? (yes/no): ").strip().lower()

    if answer == "yes":
        quote = input("Masukkan quote: ")
        author = input("Masukkan nama author: ")

        with open("quotes.txt", "a", encoding="UTF-8") as file:
            file.write(quote + "\n")
            file.write("(" + author + ")\n\n")

        print("Quote berhasil ditambahkan!\n")

    elif answer == "no":
        print("\nProgram selesai mengisi.")
        break

    else:
        print("Masukkan 'yes' atau 'no'.\n")


# 3. Menampilkan isi file terbaru
print("\n--- Isi File Terbaru ---")

try:
    with open('quotes.txt', "r", encoding="UTF-8") as file:
        for line in file:
            print(line.strip())

    print("------------------------")

except FileNotFoundError:
    print("File kosong.")
    #RAHAAAAAAAAAA