import argparse
from grub_na_pelna_funkcje import convert_to_full


def main(input_file,output_file):
    convert_to_full(input_file, output_file)
    print(f"Plik zostal zapisany jako {output_file} w katalogu Struktury")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Przemiana z struktury gruboziarnistej na pelnoatomowa")
    parser.add_argument('--input', type=str, required=True, help='Plik Wejsciowy.')
    parser.add_argument('--output', type=str, required=True, help='Plik Wyjsciowy.')
    args = parser.parse_args()
    main(args.input,args.output)