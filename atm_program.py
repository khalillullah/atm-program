import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    id = int(input("Masukkan pin Anda: "))
    trial = 0
    warning = 3

    while (id != int(atm.cekPin()) and trial < 4):
        id = int(input("Pin yang Anda masukkan salah. Percobaan sisa " +
                       str(warning) + ".\nSilakan masukkan lagi: "))
        trial += 1
        warning -= 1

    if trial == 4:
        print("Error. Silakan ambil kartu dan coba lagi.")
        exit()

    while True:
        print("\nSelamat datang di ATM Kami..")
        print("\n1 - Cek Saldo \n2 - Debet \n3 - Simpan \n4 - Ganti Pin \n5 - Keluar \n")

        selected = int(input("Pilih menu: "))

        if selected == 1:
            print("\nSaldo Anda sekarang: Rp. " + str(atm.cekBalance()))

        elif selected == 2:
            nominal = int(input("\nMasukkan nominal debet: "))
            verify_withdraw = input(
                "Konfirmasi:\nAnda akan melakukan debet dengan nominal1\nRp. " + str(nominal) + ", y / n ?")

            if verify_withdraw == "y":
                print("\nSaldo awal Anda adalah Rp. " +
                      str(atm.cekBalance()) + " ")
            else:
                break

            if nominal < atm.cekBalance():
                atm.withdrawBalance(nominal)
                print("Transaksi debet telah dilakukan.")
                print("Saldo Anda sekarang Rp. " +
                      str(atm.balance) + " ")
            else:
                print("Maaf, saldo Anda tidak cukup untuk melakukan debet.")
                print("Silakan lakukan pengurangan nominal debet")

        elif selected == 3:
            nominal = int(input("Masukkan nominal saldo: "))
            verify_deposit = input(
                "Konfirmasi: \nAnda akan melakukan deposit dengan nominal berikut " + str(nominal) + ", y / n ? ")

            if verify_deposit == "y":
                atm.depositBalance(nominal)
                print("Saldo Anda sekarang Rp. " + str(atm.balance) + " ")
            else:
                break

        elif selected == 4:
            verify_pin = int(input("Masukkan PIN awal Anda: "))

            while verify_pin != int(atm.cekPin()):
                print("PIN Anda salah. \nSilakan masukkan PIN dengan benar: ")

            new_pin = int(input("Masukkan PIN baru Anda: "))
            print("PIN Anda berhasil diganti.")

            verify_newpin = int(input("Coba masukkan PIN baru: "))

            if verify_newpin == new_pin:
                print("PIN Anda berhasil diganti")
            else:
                print("Maaf, PIN Anda salah")

        elif selected == 5:
            print(
                "Resi akan tercetak setelah Anda keluar. \nSimpan sebagai bukti transaksi Anda.")
            print("No. Record  : ", random.randint(100000, 1000000))
            print("Tanggal     : ", datetime.datetime.now())
            print("Saldo akhir : ", atm.cekBalance())
            print("Terimakasih telah menggunakan ATM Kami.\n")
            exit()

        else:
            print("Menu yang Anda pilih tidak ada.")
