import argparse
import libmbdl
import const

# Construct the argument parser and parse the arguments
arg_desc = '''\
        Mutltibundle saves many files together into a single tape or disk archive, and can
restore individual files from the archive. It is a novel alternative to GNU tar.
        '''
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                 description=arg_desc)

parser.add_argument("-v", "--verbose", help="Verbose", action="store_true", default=False, dest="verbose",
                    required=False)
action = parser.add_subparsers(help='Action to perform', dest='action', required=True)
bundle = action.add_parser('bundle', help='Bundle files together')
bundle.add_argument("input", nargs="*", help="Input file or directory")
bundle.add_argument("-o", "--output", help="Output file, otherwise mbdl.mbdl", default="mbdl.mbdl", dest="output")
bundle.add_argument("-k", "--keep-full-path", help="Keep full path", dest="keep_full_path", action="store_true",
                    required=False, default=False)
unbundle = action.add_parser('unbundle', help='Unbundle files')
unbundle.add_argument("input", help="Input file or directory")
unbundle.add_argument("output", nargs='?', help="Output directory, otherwise CWD", default=".")

args = parser.parse_args()
if args.action in const.commands["bundle"]:
    if not args.input:
        parser.error("You must specify at least one input file or directory")
    libmbdl.bundle(args.input, args)
elif args.action in const.commands["unbundle"]:
    libmbdl.unbundle(args.input, args)
