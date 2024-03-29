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
#### Show total available, used, or free space in the cloud. Default unit is in megabytes (MB).
```
m.df('/Root')
```
To display used or free space in gigabytes,
```
m.df('/Root', 'g')
```
#### List directories.
```
m.ls('/Root/Games')
```
#### Upload a file.
```
m.put('/Users/jay/Desktop/test.pdf', '/Root')
```
#### Remove a file or directory.
```
m.rm('/Root/Games')
```
#### Make a directory.
```
m.md('/Root/Codes')
```
#### Upload contents of a folder to the remote server. The remote directory should have been created using the `.md` method.
```
m.copy('/Users/jay/Desktop/Codes', '/Root/Codes')
```
#### Download contents of a remote folder to a local folder.
```
m.copy('/Users/jay/Desktop/Codes', '/Root/Codes', download=True)
```
#### Download a remote file.
```
m.get('/Root/Documents/test.pdf')
```
#### Get file download link.
```
m.url('/Root/Documents/test.pdf')
```
#### Download file using the mega link.
```
m.dl('https://mega.nz/#!2eoEhAaS!olmfrMsNeyLiifXu6D6ps9CD7ePYSYGCSjEYAoiQl4')
```
