
def fileopen(file):
    with open(file,'r',encoding='UTF8') as f :
        saved_data = []
        hf_list = []
        for line in f.readlines()[::-1]:
                if 'HF=' in line :

                    text = line.split("\\")
                    saved_data.extend(text)

                    break

        for text in saved_data:
            if 'HF=' in text:
                hf_list.append(text)
                energy = [i.lstrip('HF=') for i in hf_list]


    return saved_data , energy

print(fileopen('Project/project_data/gv5_w10.txt'))




