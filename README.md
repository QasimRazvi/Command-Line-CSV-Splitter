# Command-Line-CSV-Splitter
Splits CSVs into rows of a desired batch size from the command line. Generated files will be output in form <em>SourceFilename_0/1/2/3.csv</em> etc. The final csv file generated will contain all remaining rows.

# Usage
<p>
Add CSV files to be split to the same directory folder as CSV_splitter.py, then navigate to that location in the command line. From here run the command:
<b>python3 CSV_splitter.py [arguments] </b></p>

<p><strong><em>optional arguments:</em></strong></p>
<ul>
<li>-h, --help show this help message and exit</li>
<li>-f FILE, --file FILE file to be split 'filename.csv' OR 'ALL' indicates all .csv files in current folder will be split</li>
<li>-nh, --noheader if stated, split files will not contain the header row. if not stated, default will retain header.</li>
<li>-b BATCH_SIZE, --batch_size BATCH_SIZE (desired rows per files)</li>
<li>-v, --verbose prints a completion statement after splitting a CSV.</li>
</ul>
<p><strong><em>For example:</em></strong></p>
<p>python3 CSV_splitter.py -f ALL -b 10000</p>
<p>This will find all '.csv' files in the current folder and split each file into new files with 10000 rows per file.&nbsp;</p>



