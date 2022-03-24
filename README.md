# EC530-PROJECT4-MULTIPROCESSING
## Part One: Multiprocess
In Multiprocess.py, I wrote a program to test how many process my comupter can handle simultaneously.
To do so, I write a time-costing method and build multiprocess upon this method, reord time cost to complete all these processes.
The result is, when I run process less than 14, it always take about 2 seconds. However, if I run 15 processes, it will take about 4 seconds to complete.
In this case, the result shows that my computer can at most handle 14 processes at one time.
![16process](https://user-images.githubusercontent.com/78243340/159817404-a370591b-e51b-4008-84ed-27bd38df3273.JPG)
14 processes
![24process](https://user-images.githubusercontent.com/78243340/159817406-0bb3dea1-4c98-4913-b7ac-1a48fc4f581f.JPG)
15 processes
## Part Two: Text-converse
In Main.py.I wrote a program to converse .wav file to text, this method makes use of text-recogniziton api. 
Also, I make use of pool and Queue api to build multiprocess. Check if my computer can handle these tasks simultaneously.
![queue](https://user-images.githubusercontent.com/78243340/159817725-662f2e14-2e68-4f51-b704-ea8e5a69655e.JPG)
The the content of .wav file is "one,two,three", I downloaded it from the internet, and the result is 123. It shows that my computer can handle all the processes successfully. 
