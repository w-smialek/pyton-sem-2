###
### Załadowanie danych
###

with open('p059_cipher.txt', 'r') as f:
    message = f.read()

message = [int(i) for i in message.split(",")]

with open('words.txt', 'r') as w:
    words = w.read().splitlines()

all_words = []
for i in words:
    all_words.append(i.split(";")[1])
    all_words.append(i.split(";")[1].capitalize())

weights = []
for i in words:
    weights += 2 * [float(i.split(";")[3])]

del words

# print(weights)
# print(all_words_int)
# print(message)

###
### Generator kluczy
###

keys = []
for i in range(26 ** 3):
    a = i // 26 ** 2
    b = (i - a * 26 ** 2) // 26
    c = (i - a * 26 ** 2 - b * 26)
    keys.append([a + 97, b + 97, c + 97])

# print(keys[-100:])

###
### Odszyfrowywanie
###

best_englishness = [0., 0]
for key_no in range(len(keys)):
    englishness = 0.
    decyfred_int = [chr(message[i] ^ keys[key_no][i % 3]) for i in range(len(message))]
    decyfred_string = ''.join(decyfred_int)
    for word_no in range(len(all_words)):
        englishness = englishness + decyfred_string.count(all_words[word_no]) * weights[word_no]
    if englishness > best_englishness[0]:
        best_englishness = [englishness, key_no]
    ### Gdyby liczenie było bardzo wolne, można wyznaczyć "englishness" przypadkowego tekstu i dać warunek z wartością nieco niższą, tak,
    ### że program zakończy się gdy tylko znajdzie rozsądny tekst, czyli średnio dwa razy szybciej, niż gdyby iterował przez całość
    # if englishness > 50:
    #     break

decyfred_int = [chr(message[i] ^ keys[best_englishness[1]][i % 3]) for i in range(len(message))]
decyfred_string = ''.join(decyfred_int)

checksum = 0
for c in decyfred_string:
    checksum += ord(c)

print(best_englishness)
print(decyfred_string)
print(checksum)