# literate-waddle
This program moves files from one location to another, appends a number to the beginning of each file moved, and also writes a master list of all the files moved with the final number displayed in the master_list.txt filename.
If the program fails for any reason, it checks for the master_list.txt file in the destination, and if it exists, grabs the last number from the filename and restarts numbering from there.

Uses json for source, destination, and filetypes
Uses python3.7

### Use
1. Download `filewalker.py` to local machine
2. CD into the folder where the file was downloaded
3. Create a JSON file with the following structure

        {
            "source": "full/path/to/source/directory",
            "destination": "where/you/would/like/the/files/moved",
            "filetypes": [".list", ".of", ".file", ".types"]
        }
        
4. Run `python3.7 filewalker.py yourfileinfo.json`

***Note: the json file argument either needs to be in the same directory as filewalker.py or the full path must be given to its location***
