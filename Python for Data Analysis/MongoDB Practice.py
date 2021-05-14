from re import I
import pymongo as p

dbServer = 'mongodb://localhost:27017'
myMongo = p.MongoClient(dbServer)

dbs = myMongo.list_database_names()
print(dbs)

dbkampus = myMongo['Kampus']

# dbkampus.command("createUser", "", pwd="anditopsecret", roles=["dbAdmin"])
# dbkampus.command("createUser", "budi", pwd="buditopsecret", roles=["readWrite"])

# user = dbkampus.command('usersInfo') 


Col1 = dbkampus['Dosen']

Col2 = dbkampus['Mahasiswa']

# datadosen = [{'nama' : "Caca",
# 'usia' :28,
#     'asal' :"Jakarta",
#     'bidang' :"Fisika Astrologi",
#     'titel' :"S2",
#     'status' :"Honorer",
#     'nip' :123,
#     'matkul' :["Metrologi","Kosmologi","Kalkulus"]},

#     {'nama' :"Dedi",
#     'usia' :29,
#     'asal' :"Yogyakarta",
#     'bidang' :"Fisika Terapan",
#     'titel' :"S3",
#     'status' :"PNS",
#     'nip' :456,
#     'matkul' :["Instrumentasi","Elektronika","Fisika Dasar"]},

#     {'nama' :"Euis",
#     'usia' :30,
#     'asal' :"Bandung",
#     'bidang' :"Fisika Teoretik",
#     'titel' :"S1",
#     'status' :"Honorer",
#     'nip' :789,
#     'matkul' :["Fisika Dasar","Fisika Modern","Kalkulus"]}]

# datamahasiswa = [{'nama' :"Faza",
#     'usia' :19,
#     'asal' :"Aceh",
#     'prodi' :"Fisika",
#     'angkatan' :2017,
#     'nim' :123},

#     {'nama' :"Gilang",
#     'usia' :20,
#     'asal' :"Semarang",
#     'prodi' :"Fisika",
#     'angkatan' :2017,
#     'nim' :456},

#     {'nama' :"Hanafi",
#     'usia' :20,
#     'asal' :"Makassar",
#     'prodi' :"Fisika",
#     'angkatan' :2017,
#     'nim' : 789},

#     {'nama' :"Dini",
#     'usia' :20,
#     'asal' :"Bekasi",
#     'prodi' :"Fisika",
#     'angkatan' :2017,
#     'nim' :'004'}]

# Col1.insert_many(datadosen)
# Col2.insert_many(datamahasiswa)
# print(dbs)

    # # print("Data Submitted")

    # # print(dbs)

# for i in Col1.find():
#     print(i)

# for i in Col2.find():
#     print(i)


print("========= hapus faza ===========")
hapusfaza = {'nama' : "Faza"}
Col2.delete_one(hapusfaza)

for i in Col2.find():
    print(i)

datadosendodi = {'nama' : "Dodi",
'usia' :27,
    'asal' :"Surabaya",
    'bidang' :"Computer Science",
    'titel' :"S2",
    'status' :"PNS",
    'nip' :998,
    'matkul' :["Data Analysis","AI","NLP"]}


print("========= tambah dodi ===========")
# Col1.insert_one(datadosendodi)
for i in Col1.find():
    print(i)

print("=====update hanafi======")
# datahanafi = {"nama" : "Hanafi"} ## Kondisi Data yg akan diupdate
# new_val_hanafi = {"$set" : {"nama" : "Ahmad Hanafi"}} ## Value-Baru yg akan digunakan untuk Update
# new_val_usiahanafi = {"$set" : {"usia" : 22}}
# Col2.update_one(datahanafi, new_val_hanafi)
# Col2.update_one(datahanafi, new_val_usiahanafi)

print("=====update kota asal======")
# datakota = {}
# new_val_kota = {"$rename" : {"asal" : "Kota_asal"}}
# Col2.update_many(datakota, new_val_kota)

for i in Col2.find():
    print(i)


#buat reset awal hapus collection dulu
# Col1.drop()
# Col2.drop()