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

## Usage

### Creating default instance
1. Using default `/usr/local/bin` directory for binary files and `mega.rc` file in current working directory.
```
from megatools import Mega
m = Mega()
```
2. Passing binary directory path and `mega.rc` location.
```
from megatools import Mega
m = Mega(megaPath='/usr/local/bin/', configPath='/Users/jay/mega.rc')
```
