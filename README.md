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
    
### Test Cases

