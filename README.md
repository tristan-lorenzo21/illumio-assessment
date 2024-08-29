# Illumio Assessment

Developed a script that parses through a flow log file that maps each row to a tag based on a lookup table

## Assumptions

* The input flow log file is properly formatted (i.e. only version 2 format will be inputted, and no additional spaces/tabs included)
* The lookup table file is properly formatted (i.e. follows the following csv format: dstport,protocol,tag, and no additional spaces/tabs included)

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* Ran on Python version - 3.10.4
* Used the following Python standard libraries
  - unittest
  - os
  - csv
  - textwrap
  
### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders
* If you are using Git and your computer's terminal/command prompt to copy the repository to your local machine, please follow the instructions below
  -  First, open your local machine's terminal/command prompt
  -  Second, change to the directory that you would like to clone the repository to
      ```
      cd /path to your directory/
      ```
  - Third, use the `git clone` command followed by the repository's URL
      ```
      git clone https://github.com/tristan-lorenzo21/illumio-assessment.git
      ```
  - Lastly, once the `git clone` command is executed, navigate into the cloned directory
      ```
      cd illumio-assessment
      ```
### Executing program (Must have completed the `Installing` portion of the README before going to this step)

* ### On Windows
  * First, open your command prompt or Powershell
  * Second, navigate to the `illumio-assessment` directory
    ```
    cd / location of illumio-assessment directory
    ```
  * Third, enter the `python` command followed by the main script: `flow_log_parser.py` into the terminal
    ```
    python flow_log_parser.py
    ```
  * The output file will be located inside the `output_files` folder with the name `output.txt`
     
* ### On Mac
  * First, open your terminal
  * Second, navigate to the `illumio-assessment` directory
    ```
    cd / location of illumio-assessment directory
    ```
  * Third, enter the `python3` command followed by the main script: `flow_log_parser.py` into the terminal (we use the command `python3` because just `python` will lead to a 2.x version of Python)
    ```
    python3 flow_log_parser.py
    ```
  * The output file will be located inside the `output_files` folder with the name `output.txt`
    
### Unit Tests using the `unittest` standard library
* All 9 unit tests passed, and a brief description of what each unit test is testing is included below
1. `test_get_parsed_log`
   * Description: Checks if get_parsed_log correctly parses the flow log and extracts destination ports and protocols.
2. `test_get_lookup_table`
   * Description: Verifies that get_lookup_table reads and converts the CSV file into the expected dictionary.
3. `test_get_tag_counts`
   * Description: Confirms that get_tag_counts accurately counts tags from the parsed log using the lookup table.
4. `test_get_combination_counts`
   * Description: Ensures get_combination_counts counts occurrences of (port, protocol) combinations in the log.
5. `test_invalid_log_file`
    * Description: Tests if get_parsed_log handles files larger than 10 MB correctly.
6. `test_missing_log_file`
    * Description: Checks if get_parsed_log handles missing log files properly.
7. `test_missing_lookup_table_file`
    * Description: Checks if get_lookup_table handles missing lookup table files properly.
8. `test_ascii_check_log`
    * Description: Ensures get_parsed_log detects non-ASCII files.
9. `test_ascii_check_lookup_table`
    * Description: Ensures get_lookup_table detects non-ASCII files.

