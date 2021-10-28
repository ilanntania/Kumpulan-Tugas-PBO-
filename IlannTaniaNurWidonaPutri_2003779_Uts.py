# Nama : Ilann Tania Nur Widona Putri
# NIM : 2003779
# Kelas : SIK A 20

user_id = 0
loop = "n"
#isi/info user
user =  [
            {   
                "id":"7879",
                "no_rekening":"123322455",
                "username":"test",
                "pin":"0977",
               
            },
            {   
                "id":"0977",
                "no_rekening":"436678998",
                "username":"test2",
                "pin":"8766",
               
            }
        ]
#menyimpan status apakah user berhasil login atau tidak
status_login = False
#menyimpan kondisi apakah kita masih menggunakan ATM atau tidak
pakai_atm = "y"
 
 #Fungsi login buat tahap masuk pertama
def cek_login(p):
    for us in user:
        if us['pin'] == p:
            return us
    return False       
     
def cek_user(id):
    for i in range(len(user)):
        if user[i]['id'] == str(id):
            return int(i)
    return -1
 
def cek_rekening(no):
    for i in range(len(user)):
        if str(user[i]['no_rekening']) == str(no):
            return int(i)
    return -1
 
#Pewarisan/Proses

#Pewarisan menu utama 
class Menu():
    def __init__(self, info, tambah, ambil,keluar,logout):
        self.info = info
        self.tambah= tambah
        self.ambil = ambil
        self.keluar = keluar
        self.logout = logout
    #Proses dan output dari menu utama
    def cek_menu (self):
        print('====================================================')
        print('                 ATM LEEBIT')
        print('====================================================')
        print('====================================================')
        print(' 1. ', self.info, '\n 2. ',self.tambah, '\n 3. ',self.ambil , '\n 4. ',self.keluar , '\n 5. ',self.logout)
        print('*=*=*=**=*=*=**=*=*=**=*=*=**=*=*=**=*=*=**=*=*=**=*=')

#Pewarisan menu Kedua
class Menu2():
    def __init__(self, Umum, Tabungan):
        self.Umum = Umum
        self.Tabungan= Tabungan
#Proses dan output dari menu utama
    def cek_menu2 (self):
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print(' 1. ', self.Umum, '\n 2. ',self.Tabungan)
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++')

#Pewarisan saldo umum
class Saldo_umum():
    def __init__ (self,rek,salu):
        self.rekeninh=rek
        self.saldou=salu

    #Proses dan Output cek saldo 
    def cek_saldou(self):
        print('====================================================')
        print('                  Informasi Saldo ')
        print('                     Umum ')
        print('====================================================')
        print('Berikut adalah nominal saldo anda : ')
        print ("saldo : Rp. ", self.saldou)
        print('---------------------------')

    #Proses dan Output tambah Saldo   
    def tambahu(self):
        print('====================================================')
        print('                  Tambah Saldo')
        print('                     Umum ')
        print('====================================================')
        print('Silahkan masukan nominal uang yang ingin anda tambahkan ')
        tambahu_uang=int(input("Nominal Uang : "))
        hasilu=self.saldou+tambahu_uang
        self.saldou = hasilu
        print('*=*=*=**=*=*=**=*=*=**=*=*=**=*=*')
        print('   PROSES BERHASIL !!')
        print('---------------------------')
        print("Jumlah Penambahan Saldo Anda  : Rp. ", tambahu_uang) 
        print(" Sisa Saldo Anda              : Rp. ",hasilu)
        print('---------------------------')

    #Proses dan Output ambil saldo   
    def ambilu(self):
        print('====================================================')
        print('                  Ambil Saldo')
        print('                     Umum ')
        print('====================================================')
        print('Silahkan masukan nominal uang yang ingin anda ambil ')
        ambilu_uang=int(input("Nominal Uang : "))
        hasilu=self.saldou-ambilu_uang
        self.saldou = hasilu
        print('*=*=*=**=*=*=**=*=*=**=*=*=**=*=*')
        print('   PROSES BERHASIL !!')
        print('---------------------------')
        print ("Jumlah Penarikan Saldo Anda  : Rp. ", ambilu_uang)
        print(" Sisa Saldo Anda              : Rp. ", hasilu)
#Pewarisan saldo tabungan
class Saldo_tabungan():
    def __init__ (self,rek,salt):
        self.rekeninh=rek
        self.saldot=salt

    #Proses dan Output cek saldo 
    def cek_saldot(self):
        print('====================================================')
        print('                  Informasi Saldo ')
        print('                     Tabungan ')
        print('====================================================')
        print('Berikut adalah nominal saldo anda : ')
        print ("saldo : Rp. ", self.saldot)
        print('---------------------------')

    #Proses dan Output tambah Saldo   
    def tambaht(self):
        print('====================================================')
        print('                   Tambah Saldo')
        print('                     Tabungan ')
        print('====================================================')
        print('Silahkan masukan nominal uang yang ingin anda tambahkan ')
        tambaht_uang=int(input("Nominal Uang : "))
        hasilt=self.saldot+tambaht_uang
        self.saldot = hasilt
        print('*=*=*=**=*=*=**=*=*=**=*=*=**=*=*')
        print('   PROSES BERHASIL !!')
        print('---------------------------')
        print("Jumlah Penambahan Saldo Anda  : Rp. ", tambaht_uang) 
        print(" Sisa Saldo Anda              : Rp. ",hasilt)
        print('---------------------------')

    #Proses dan Output ambil saldo   
    def ambilt(self):
        print('====================================================')
        print('                  Ambil Saldo')
        print('                    Tabungan ')
        print('====================================================')
        print('Silahkan masukan nominal uang yang ingin anda ambil ')
        ambilt_uang=int(input("Nominal Uang : "))
        hasilt=self.saldot-ambilt_uang
        self.saldot = hasilt
        print('*=*=*=**=*=*=**=*=*=**=*=*=**=*=*')
        print('   PROSES BERHASIL !!')
        print('---------------------------')
        print ("Jumlah Penarikan Saldo Anda  : Rp. ", ambilt_uang)
        print(" Sisa Saldo Anda              : Rp. ", hasilt)
 
#Output Menu Utama
Menubar = Menu('Informasi Saldo', 'Tambah Saldo ', 'Ambil Saldo ', 'Keluar' , 'logout' )


#Output Rekening Umum
IlannTann_rek=Saldo_umum("170411100014", 100000)
#Output Rekening Tabungan
IlannTann_rek=Saldo_tabungan("170411100014", 100000)
#Output Menu Kedua
Menubar2 = Menu2('Umum', 'Tabungan ') 
while pakai_atm == "y":
    while status_login == False:
        print("SELAMAT DATANG DI ATM UPI SERANG")
        print("Silahkan masukan pin anda")
        pin = input("Masukan PIN : ")
     
        cl = cek_login(pin)
        if cl != False:
            print("selamat data "+cl['username'])
            user_id = cl['id']
            status_login = True
            loop = "y"
        else:
            print("")
            print("Ops PIN anda salah")
            print("")
            print("")
     
    while loop == "y" and status_login == True:
        u = user[cek_user(user_id)]
        Menubar.cek_menu ()
        a = int(input("Silahkan pilih menu : "))
        if a == 1:
           #Output Informasi Saldo Umum dan Tabungan
            Ilanntann_rek.cek_saldou()
            Ilanntann_rek.cek_saldot()
            loop = "n"
        elif a == 2:
            #menu kedua
            print('Silahkan Pilih Salah satu Jenis Saldo Anda')
            Menubar2.cek_menu2 ()
            mza = int(input('Masukan Pilihan Anda : ')) 
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
            if mza == 1:
                #Output Tambah Saldo Utama
                Ilanntann_rek.tambahu()
                loop = "n"

            elif mza == 2:
                #Output Tambah Saldo Tabungan
                Ilanntann_rek.tambaht()
                loop="n"

            else: print('Maaf Anda Memilih nomer yang salah ')
            loop="n"
                 
        elif a == 3:
             #menu kedua
            print('Silahkan Pilih Salah satu Jenis Saldo Anda')
            Menubar2.cek_menu2 ()
            mza = int(input('Masukan Pilihan Anda : ')) 
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
            if mza == 1:
                #Output Tambah Saldo Utama
                Ilanntann_rek.ambilu()
                loop = "n"

            elif mza == 2:
                #Output Tambah Saldo Tabungan
                Ilanntann_rek.ambilt()
                loop = "n"

            else: print('Maaf Anda Memilih nomer yang salah ')
            loop = "n"

        elif a == 4:
            status_login = False
             
        elif a == 5:
            status_login = False
            loop = "n"
            pakai_atm = "n"
        else:
            print("pilihan tidak tersedia")
        if status_login == True:
             
            input("kembali Ke menu (Enter) ")
            print("")
            loop = "y"
 
    