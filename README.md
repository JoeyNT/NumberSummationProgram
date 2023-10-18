<body>
    <h1>Number Summation Program</h1>
    <p>This Python program reads a file named <code>numbers.txt</code>, processes each line based on the rule specified, and writes the sum of numbers to <code>output.txt</code>.</p>
<h2>Input File (numbers.txt):</h2>
    <pre>
3 10 20 23
4 -7 8 15 12
0
1 17
5 -8 113 -1 6 2
 </pre>
<br> You can access the <code>numbers.txt</code> by clicking the link below:</p>
<a href="https://github.com/JoeyNT/PyFileManager/blob/main/numbers.txt" target="_blank">Download numbers.txt File</a>
<h2>Output File (output.txt):</h2>   
    <pre>
63
28
0
17
112
 </pre>
<br> You can access the <code>output.txt</code> by clicking the link below:</p>
<a href="https://github.com/JoeyNT/PyFileManager/blob/main/output.txt" target="output">Download output.txt File</a>

<h2>Usage:</h2>
    <p>1. Create a file named <code>numbers.txt</code> and populate it with lines following the specified format (as shown above).</p>
    <p>2. Run the program.</p>
    <p>3. The program will process the file, calculate sums, and write the results to <code>output.txt</code>.</p>
    
<h2>Sample Code:</h2>
<pre>
import pickle

numbersfile = open('numbers.txt', 'r')
sumfile = open('output.txt', 'w')
for line in numbersfile:
  numberSum = 0
  number = line.split()
  for n in number[1:]:
    numberSum += int(n)
  sumfile.write(str(numberSum) + "\n")

numbersfile.close()
sumfile.close()
    </pre>
<h2>Author:</h2>
<p>Joey Cuomo (GitHub Username: https://github.com/JoeyNT)</p>

<h2>License:</h2>
<p>This program is open-source and available under the MIT License. Feel free to use and modify it as needed.</p>
    
<h2>Repository:</h2>
<p>Find the source code and contribute to the project on GitHub: <a href="https://github.com/JoeyNT/PyFileManager/blob/main/filehandler.py">GitHub Repository</a></p>
