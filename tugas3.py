orang = [
{"nama": "arsene lupin", "nik": 1234, "jenis_kelamin": "male", "tanggal_lahir": "1902-03-23"},
{"nama": "sherlock holmes", "nik": 4321, "jenis_kelamin": "male", "tanggal_lahir": "1876-08-16"},
{"nama": "irene adler", "nik": 6789, "jenis_kelamin": "female", "tanggal_lahir": "1884-10-07"}
]
# menerima input dari user dan menambahkan ke dalam dictionary
for i in range(1):
    nama = input(f"Masukkan nama orang ke-{i+1}: ")
    nik = int(input(f"Masukkan NIK orang ke-{i+1}: "))
    jenis_kelamin = input(f"Masukkan jenis kelamin orang ke-{i+1} (male/female): ")
    tanggal_lahir = input(f"Masukkan tanggal lahir orang ke-{i+1} (format: YYYY-MM-DD): ")
    
    # membuat dictionary untuk setiap orang
    data_orang = {
        'nama': nama,
        'nik': nik,
        'jenis_kelamin': jenis_kelamin,
        'tanggal_lahir': tanggal_lahir
    }
    
    # menambahkan dictionary orang ke dalam list orang
    orang.append(data_orang)

    # menerima input dari user
nama_dicari = input("Masukkan nama yang ingin dicari: ")

# melakukan pencarian berdasarkan nama
for data in orang:
    if data['nama'].lower() == nama_dicari.lower():
        print(f"Data ditemukan:")
        print(f"Nama: {data['nama']}")
        print(f"NIK: {data['nik']}")
        print(f"Jenis kelamin: {data['jenis_kelamin']}")
        print(f"Tanggal lahir: {data['tanggal_lahir']}")
        break
else:
    print("Data tidak ada")
