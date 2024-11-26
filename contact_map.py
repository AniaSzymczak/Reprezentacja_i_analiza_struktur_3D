from zadanie_1_funkcje import structure_load, read_CA, visualization_contact_map

struktura = structure_load("4ywo")
tablica_ca = read_CA(struktura)
visualization_contact_map(tablica_ca)