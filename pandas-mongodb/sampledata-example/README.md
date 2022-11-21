# Load Dataset into MongoDB instance

## Data
`./mongo-service/data` is downloaded from this link:
[Data](https://github.com/SouthbankSoftware/dbkoda-data)

## Load data into MongoDB Instance --> mongo-init.sh
Mongo init script is used to load data from dump
- Move into data directory: `cd /data/db` 
- Dump data: `mongodump -u root -p my_password --db SampleCollections --collection <collection> --authenticationDatabase admin`
- Restore data: `mongorestore -u root -p my_password --nsInclude="SampleCollections.samples_pokemon" --authenticationDatabase admin`
- `1119998 document(s) restored successfully. 0 document(s) failed to restore.`
