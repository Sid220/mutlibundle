# Multibundle

![Build](https://github.com/Sid220/mutlibundle/actions/workflows/build.yml/badge.svg)

Mutltibundle saves many files together into a single tape or disk archive, and can restore individual files from the
archive. It is a novel alternative to GNU tar, and aims to be incredibly portable.

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

## Format

The Mutlibundle file format consists of three components

1. Magic number
2. Header
3. Data

### Magic Number

Every multibundle file begins with the magic number `$₹₫₦€¥` encoded in UTF-8. This is used to identify the file as a
multibundle file. Newer versions of multibundle can add to this magic number to provide additional information about the
file.

#### Versions

| Version | Magic Number | Description     |
|---------|--------------|-----------------|
| 1       | `$₹₫₦€¥`     | Initial version |

### Header

Every file in a multibundle contains a header. The header contains the following information

| Length | Description | Type Description                                                       |
|--------|-------------|------------------------------------------------------------------------|
| 4096   | File name   | UTF-8 Encoded String, with NULL characters replacing the excess length |
| 8      | File size   | Big-endian unsigned long long                                          |

### Data
After the header, the file data is stored. The length of the data is specified in the header.

### Repeat
The header and data are then repeated for every file in the multibundle.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details