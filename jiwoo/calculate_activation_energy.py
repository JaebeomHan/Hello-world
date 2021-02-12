
def calculate_reactant1_energy(file):
    with open(file,'r',encoding='UTF8') as f :
        saved_data = []
        hf_list = []
        for line in f.readlines()[::-1]:
<<<<<<< HEAD
                if 'HF=' in line :

                    text = line.split("\\")
                    saved_data.extend(text)

                    break
=======
            if 'HF=' in line :

                text = line.split("\\")
                saved_data.extend(text)

                break
>>>>>>> f7c77dfeeb2bf75198fa3dd3b50059d66c014f4f

        for text in saved_data:
            if 'HF=' in text:
                hf_list.append(text)
                energy = [i.lstrip('HF=') for i in hf_list]


    return energy

<<<<<<< HEAD
print(calculate_reactant1_energy('gv5_w10.txt'))
reactant1_energy = (calculate_reactant1_energy('gv5_w10.txt'))


print(reactant1_energy)


=======
>>>>>>> f7c77dfeeb2bf75198fa3dd3b50059d66c014f4f
def calculate_reactant2_energy(file):
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

    return energy

<<<<<<< HEAD
print(calculate_reactant2_energy('wmethane.txt'))
reactant2_energy = (calculate_reactant2_energy('wmethane.txt'))
print(reactant2_energy)


=======
>>>>>>> f7c77dfeeb2bf75198fa3dd3b50059d66c014f4f
def calculate_ts_energy(file):
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

    return energy

<<<<<<< HEAD
print(calculate_ts_energy('gv5_wts10-1.txt'))
ts_energy = (calculate_ts_energy('gv5_wts10-1.txt'))

activation_energy_hatree = float(ts_energy[0])-(float(reactant1_energy[0])+float(reactant2_energy[0]))
print(activation_energy_hatree)
=======
if __name__ == '__main__':

    print(calculate_reactant1_energy('gv5_w10.txt'))
    reactant1_energy = (calculate_reactant1_energy('gv5_w10.txt'))

    print(reactant1_energy)

    print(calculate_reactant2_energy('wmethane.txt'))
    reactant2_energy = (calculate_reactant2_energy('wmethane.txt'))
    print(reactant2_energy)

    print(calculate_ts_energy('gv5_wts10-1.txt'))
    ts_energy = (calculate_ts_energy('gv5_wts10-1.txt'))

    activation_energy_hatree = float(ts_energy[0])-(float(reactant1_energy[0])+float(reactant2_energy[0]))
    print(activation_energy_hatree)
>>>>>>> f7c77dfeeb2bf75198fa3dd3b50059d66c014f4f
