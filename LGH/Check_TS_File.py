
def Check_TS_File(file) :
    with open(file, 'r', encoding = 'UTF*') as f :
        saved_data = []
        for line in f.readlines() :
            if 'Frequencies' in line :
                text = line.split(" ")
                saved_data.append(text)

    save_only_frequencies = sum(saved_data, [])
    while '' in save_only_frequencies :
        save_only_frequencies.remove('')
    while '--' in save_only_frequencies :
        save_only_frequencies.remove('--')
    while 'Frequencies' in save_only_frequencies :
        save_only_frequencies.remove('Frequencies')

    frequencies_list = list(map(float, save_only_frequencies))
    check_freq_list = [x for x in frequencies_list if x < 0]
    if len(check_freq_list) == 1 :
        print("good")
    else :
        print("not good")
print(Check_TS_File('gv5_wts10-1.txt'))









