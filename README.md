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

## How to

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

### Usage
1. Show total available, used, or free space in the cloud. Default unit is in megabytes (MB).
```
m.df('/Root')
```
To display used or free space in gigabytes,
```
m.df('/Root', 'g')
```
2. List directories
```
m.ls('/Root/Games')
```
3. Upload a file
```
m.put('/Users/jay/Desktop/test.pdf', '/Root')
```
4. Remove a file or directory
```
m.rm('/Root/Games')
```
5. Make a directory
```
m.md('/Root/Codes')
```
6. Upload contents of a folder to the remote server. The remote directory should have been created using the `.md` method.
```
m.copy('/Users/jay/Desktop/Codes', '/Root/Codes')
```
7. Download contents of a remote folder to a local folder.
```
m.copy('/Users/jay/Desktop/Codes', '/Root/Codes', download=True)
```
8. Download a remote file.
```
m.get('/Root/Documents/test.pdf')
```
9. Get file download link
```
m.url('/Root/Documents/test.pdf')
```
10. Download file using the mega link
```
m.dl('https://mega.nz/\#\!2eoEhAaS\!olmfrMsNeyLiifXu6D6ps9CD7ePYSYGCSjEYAoiQl4')
```
