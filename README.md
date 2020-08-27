# numwrite
Random Number Printer

# How to use: 
1. Download the file 
```
git clone https://github.com/batuhanakca/numwrite.git
```
2. Give the execute permission to the script
```
$ cd numwrite
$ chmod a+x numWriter.py
```
3. Run the command with or without parameters: 
```
./numWriter.py --help
usage: 
              numWriter.py <end> <start>    : Default numbers are 1 to 10
              numWriter.py                  : print numbers from 1 to 10 randomly
              numWriter.py 5                : print numbers from 1 to 5 randomly 
              numWriter.py 15 3             : print numbers from 3 to 15 randomly 
        

positional arguments:
  end         End in this number
  start       Start from this number

optional arguments:
  -h, --help  show this help message and exit
```
# Examples : 
```
[user@hostname]$ ./numWriter.py 
10
1
6
8
3
2
5
7
4
9
[user@hostname]$ ./numWriter.py 12 3
10
6
5
8
9
12
4
11
3
7
[user@hostname]$ ./numWriter.py 9
7
2
9
5
1
3
6
4
8
```
