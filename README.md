# MEGA-Tools Python

## MacOS
1. Install megatools using Homebrew
  ``` 
  brew install megatools 
  ``` 
2. Create a `mega.rc` file in your home directory or in the current working directory. The contents of the file in shown below
```
  [Login]
  Username = your@email
  Password = yourpassword

  [Network]
  # 1MiB/s
  SpeedLimit = 1024
  # Use over TOR or any socks5 proxy
  Proxy = socks5://127.0.0.1:9050
  ParallelTransfers = 2
```
