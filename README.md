# photo-store
python script to filter and store photo from my computer

Configutation at ./config.json :
- file_type :
    - filter_out : is a  list of file extensions in lowercase, which you don't want to copy to a new directory
- path :
    - input_dir : is a root of an input directory structure to be started with
    - output_dir : is a root of an output directory structure to be started with
    - log_file : is a name of log file
- dir :
    - filter_in : is a regexp of folder name which you want to do inside in ./input_dir (if empty, it gets all folder)
