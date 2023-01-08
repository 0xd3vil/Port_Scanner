import argparse
import socket

def port_scanner(host, port):
  # create a socket object
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  # set a timeout of 1 second for the socket
  s.settimeout(1)
  
  # try to connect to the port
  try:
    s.connect((host, port))
    return True
  except:
    return False

def main():
  # create an argument parser
  parser = argparse.ArgumentParser(description="Python port scanner")
  
  # add arguments for the host and the port range
  parser.add_argument("--host", type=str, required=True, help="the host to scan")
  parser.add_argument("--start", type=int, required=True, help="the starting port number")
  parser.add_argument("--end", type=int, required=True, help="the ending port number")
  
  # parse the arguments
  args = parser.parse_args()
  
  # scan the ports
  for port in range(args.start, args.end+1):
    if port_scanner(args.host, port):
      print(f"Port {port} is open")
    else:
      print(f"Port {port} is closed")

if __name__ == "__main__":
  main()
