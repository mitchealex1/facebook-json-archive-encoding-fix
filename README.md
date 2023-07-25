# Fix Your Facebook JSON Archive Data ✨

This is a script to fix data that has been exported from Facebook in the JSON format.

See https://sorashi.github.io/fix-facebook-json-archive-encoding/ for more detail on the issue.

## Using the script

The following command will generate a virtual environment and run the python script. This will read the raw data and create a copy of the data in a specified output location with the encoding fixed.

```
poetry run python src/main.py /path/to/raw/data/ /path/to/output/location
```

You can also optionally specify the [glob pattern](https://docs.python.org/3/library/glob.html) used to select the files with `--file-glob custom_glob_pattern`.
