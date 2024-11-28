import argparse
from pelna_na_grub_funkcje import convert_to_grub
from zadanie_1_funkcje import structure_load

def main(input_file,output_file):
    structure = structure_load(input_file)
    convert_to_grub(args.output, structure)
    print(f"Plik zostal zapisany jako {output_file} w katalogu Struktury")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Przemiana z struktury pelnej na gruboziarnista")
    parser.add_argument('--input', type=str, required=True, help='Plik Wejsciowy.')
    parser.add_argument('--output', type=str, required=True, help='plik wyjsciowy.')
    args = parser.parse_args()
    main(args.input,args.output)

