I don't know what the UCB folks need, so here's a sketch or two...

One script here creates a database with a teeny amount of sample data:
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

