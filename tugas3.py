arsene_lupin = {
    'nama': 'Arsene Lupin',
    'nik': 1234,
    'jenis_kelamin': 'male',
    'tanggal_lahir': '1902-03-23'
}

sherlock_holmes = {
    'nama': 'Sherlock Holmes',
    'nik': 4321,
    'jenis_kelamin': 'male',
    'tanggal_lahir': '1876-08-16'
}

irene_adler = {
    'nama': 'Irene Adler',
    'nik': 6789,
    'jenis_kelamin': 'female',
    'tanggal_lahir': '1884-10-07'
}

# membuat dictionary kosong
orang = []

# menerima input dari user dan menambahkan ke dalam dictionary
for i in range(3):
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

print(orang)