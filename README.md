# Port_Scanner
A port scanner that is capable of scanning a host or network for open ports. The port scanner allows users to specify a range of ports to scan, or to scan all 65535 ports. It also includes options for scanning for specific types of ports and for scanning multiple hosts at a time.

In implementing the port scanner, I used the Python socket library to create connections to specific ports and check for responses in order to determine if the ports were open or closed. I also implemented algorithms for efficient port scanning and for handling errors and timeouts.

This Python script defines a port_scanner function that takes a host and a port as arguments, and uses the socket library to try to connect to the port. If the connection is successful, the function returns True, otherwise it returns False. The main function uses the argparse library to define command-line arguments for the host, the starting port number, and the ending port number. It then uses a loop to scan the specified range of ports and print the status of each port.

This Python script defines a port_scanner function that takes a host and a port as arguments, and uses the socket library to try to connect to the port. If the connection is successful, the function returns True, otherwise it returns False. The main function uses the argparse library to define command-line arguments for the host, the starting port number, and the ending port number. It then uses a loop to scan the specified range of ports and print the status of each port.

To use this script, you can run it from the command line with the following arguments:<br>
```python port_scanner.py --host <host> --start <start> --end <end>```

Replace <host> with the host you want to scan, <start> with the starting port number, and <end> with the ending port number. For example, to scan all ports on the localhost, you can use the following command:</br>
```python port_scanner.py --host lpu.in --start 1 --end 65535```
  
![screenshot](https://raw.githubusercontent.com/0xd3vil/Port_Scanner/main/Screenshot%202023-01-08%20at%201.15.13%20PM.png)
  
In case you want to contribute, I encourage you to do so. Do you have ideas for cool features? Or have you found any bugs so far? Feel free to open an issue or send a pull request. It's very much appreciated.
  
<div align="center">  
<h3>https://linkedin.com/in/0xd3vil</h3>  
<h3>https://twitter.com/0xd3vil</h3>
  
