import os
import sys
import csv
import argparse

"""
Split a source csv (or all CSVs in a folder) into multiple CSVs of a specified batch size,
except the last file (which will contain all remaining records).

Split files follow a zero-index sequential naming convention:

    `{split_file_prefix}_0.csv`
    
"""
current_dir = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", required = True, help="file to be split\n 'filename.csv'\n OR \n'ALL' indicates all .csv files in current folder will be split")
parser.add_argument("-nh", "--noheader", action="store_true", help="if stated, split files will not contain the header row" )
parser.add_argument("-b", "--batch_size", required=True,  type=int, help="desired rows per files")
parser.add_argument("-v", "--verbose", action="store_true", help="prints a completion statement after splitting a CSV.")

args = parser.parse_args()

files = []
if args.file == 'ALL':
    for source_file in os.listdir(current_dir):
        if source_file[-4:] == '.csv':
            files.append(os.path.join(current_dir, source_file))
elif args.file[-4:] == '.csv':
    files.append(os.path.join(current_dir ,args.file))
else:
    print("No .csv file in folder or no .csv file given as argument.")
    parser.print_help()
    sys.exit(0)


batch_size = args.batch_size

for file in files:
    with open(file, 'r') as source:
        reader = csv.reader(source)
        header = next(reader)

        file_idx = 0
        records_exist = True

        while records_exist:

            i = 0
            target_file = f'{file[:-4]}_{file_idx}.csv'

            with open(target_file, 'w',newline='') as target:
                writer = csv.writer(target)

                while i < batch_size:
                    if i == 0 and args.noheader == False:
                        writer.writerow(header)

                    try:
                        writer.writerow(next(reader))
                        i += 1
                    except:
                        records_exist = False
                        break

            if i == 0:
                # we only wrote the header, so delete that file
                os.remove(target_file)

            file_idx += 1
    if args.verbose:
        print('Finished splitting {} into batches of {} records'.format(file,batch_size))

print('Finished splitting {} CSV(s).'.format(len(files)))
