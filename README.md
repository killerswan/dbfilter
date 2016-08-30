First steps
===

For SQLite exploration, one script here creates a database with a teeny amount of sample data:
```bash
rm *.sqlite3
python dbcreate.py
```

And another script searches a couple columns of a table,
then prints matches into a CSV file:
```bash
rm *.csv
python dbfilter.py

cat output.csv
```

😺
UCMR3 Data
===

Now to filter the data from [this UCMR3 publication](https://www.epa.gov/dwucmr/occurrence-data-unregulated-contaminant-monitoring-rule#3), after extracting the ZIP file so that this file exists: `ucmr-3-occurrence-data/UCMR3_All.txt`...

```bash
python ucmr_filter.py
```

This creates a file named `filtered-ucmr3-data.csv` which has a subset of the data, still in this tab-delimited Excel-readable file format.

