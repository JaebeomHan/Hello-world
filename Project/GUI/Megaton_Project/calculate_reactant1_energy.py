

def calculate_reactant1_energy(data):

    saved_data = []
    hf_list = []
    for line in data.readlines()[::-1]:
        if 'HF=' in line:
            text = line.split("\\")
            saved_data.extend(text)

            break

    for text in saved_data:
        if 'HF=' in text:
            hf_list.append(text)
            transition_energy = [i.lstrip('HF=') for i in hf_list]
            transition_energy_value = transition_energy[0]

    return transition_energy_value