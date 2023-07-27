# Multibundle
![Build](https://github.com/Sid220/mutlibundle/actions/workflows/build.yml/badge.svg)

Mutltibundle saves many files together into a single tape or disk archive, and can restore individual files from the archive. It is a novel alternative to GNU tar, and aims to be incredibly portable.

## Usage
### Overview
```
mbdl [-h] [-v] {bundle,unbundle} ...
positional arguments:
  {bundle,unbundle}  Action to perform
    bundle           Bundle files together
    unbundle         Unbundle files

options:
  -h, --help         show this help message and exit
  -v, --verbose      Verbose (default: False)
```
### Bundling
Ex: `mbdl bundle -o myarchive.mbdl /home/user/Documents /home/user/Pictures`
```
mbdl bundle [-h] [-o OUTPUT] [-k] [input ...]

positional arguments:
  input                 Input file or directory

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file, otherwise mbdl.mbdl
  -k, --keep-full-path  Keep full path
```
### Unbundling
Ex: `mbdl unbundle myarchive.mbdl /home/user/restore`
```
mbdl unbundle [-h] input [output]

positional arguments:
  input       Input file or directory
  output      Output directory, otherwise CWD

options:
  -h, --help  show this help message and exit
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details