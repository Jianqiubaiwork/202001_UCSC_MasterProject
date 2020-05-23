import argparse
import pandas


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('csv1', type=str)
    parser.add_argument('csv2', type=str)
    parser.add_argument('-o', type=str)

    args = parser.parse_args()

    merge_two_csv(args.csv1, args.csv2, args.o)


def merge_two_csv(csv1_path, csv2_path, out_path):
    csv1 = pandas.read_csv(csv1_path)
    csv2 = pandas.read_csv(csv2_path)
    merged = csv1.merge(csv2, on='id')
    merged.to_csv(out_path, index=False) 

if __name__=='__main__':
    main()