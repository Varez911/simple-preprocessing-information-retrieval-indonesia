import string
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

"""
PROGRAM PREPROCESSING INFORMATION RETRIEVAL

NAMA: ALIFIAN ALVAREZ F. S.
NRP : 15-2018-021
=========================================================
DOCUMENT TEST:
"Berikut ini adalah salah satu keahlian dari seorang ibu, yaitu adalah memasak. 12344412314123.  Saya tidak tahu apa yang akan saya masukan lagi, tetapi mencoba berbuat kebaikan itu sangatlah keren"
"Proses stemming antara satu bahasa dengan bahasa yang lain tentu berbeda. Contohnya pada teks berbahasa inggris, proses yang diperlukan hanya proses menghilangkan sufiks. Sedangkan pada teks berbahasa Indonesia semua kata imbuhan baik itu sufiks dan prefiks juga dihilangkan."
"Menyicil"
"MEMBELI"
"""

def readFile(namafile):
    text_file = open(namafile, "r")
    lines = text_file.readlines()
    lines2 = []
    for i in lines:
        i = i.replace('\n', '')
        lines2.append(i)
    return lines2

#Inisialisasi Input Dokumen
document = input("Masukan Dokumen: ")
print("=======================================")

#Proses Case Folding
lower_document = document.lower()
print("Dokumen Lowecase: ", lower_document)
print("=======================================")

no_number_document = ''.join([i for i in lower_document if not i.isdigit()])
print("Dokumen with no number: ", no_number_document)
print("=======================================")

punctuation = set(string.punctuation)
no_punctuation_document = ''.join(ch for ch in no_number_document if ch not in punctuation)
print("Dokumen with no punctuation: ", no_punctuation_document)
print("=======================================")

no_whitespace_document = no_punctuation_document.strip();
print("Dokumen with no whitespace: ", no_whitespace_document)
print("=======================================")

#Proses Tokenizing
kata = no_whitespace_document.split()
print("Split: ", kata)
print(len(kata), " word")
print("=======================================")

remove_duplicate_word = list(set(kata))
print("Tokenizing: ", remove_duplicate_word)
print(len(remove_duplicate_word), " word")
print("=======================================")

#Proses Filtering / Stop Removal
stop_removal = readFile('StopWord.txt')
document_without_stopword = [x for x in remove_duplicate_word if x not in stop_removal]
print("Filtering Dokument: ",document_without_stopword)
print("=======================================")

#Proses Stemming Manual
kata_dasar = readFile('kata-dasar.txt')
akhiran = ["i", "an", "kan", "ku", "mu", "nya", "lah", "kah", "tah", "pun"]
awalan = ["di","ke","se","me","be","pe", "te"]
root_word = []
for index, kata in enumerate(document_without_stopword):
    #print("sesi kata ", kata)

    # cek langsung ke kata_dasar
    if kata in kata_dasar:
        #print(kata, " = kata dasar murni")
        root_word.append(kata)
        continue

    # cek akhiran
    for p in akhiran:
        if kata[-len(p):] == p and kata[:-len(p)] in kata_dasar:
            #print(kata, " = ", kata[:-len(p)], " + ", p)
            root_word.append(kata[:-len(p)])
            break

    # cek awalan
    for x in awalan:
        if kata[:len(x)] == x and kata[len(x):] in kata_dasar:
            #print(kata, " = ",  x, " + ", kata[len(x):])
            root_word.append(kata[len(x):])
            break

print("Dokumen with stemming manual: ",root_word)
print("=======================================")

#Proses Stemming Manual
factory = StemmerFactory()
stemmer = factory.create_stemmer()

document_without_stopword = ' '.join(document_without_stopword) #Convert list to string

hasil_stemming_sastrawi = stemmer.stem(document_without_stopword)
print("Dokumen with stemming Sastrawi: ", hasil_stemming_sastrawi)
