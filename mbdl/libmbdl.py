import os
import pathlib
import progressbar
import output
import util
from util import create_directories, remove_excess_null_chars, size_from_bytes, find_greatest_common_factor, \
    print_tree, pad_filename, size_to_bytes
from const import magic


def unbundle(read_file, args):
    out_path = args.output
    if not os.path.exists(pathlib.Path(out_path).parent.absolute()):
        output.print_fatal("Output directory does not exist")
        exit(1)
    try:
        if len(os.listdir(out_path)) != 0:
            output.print_fatal("Output directory is not empty")
            exit(1)
    except FileNotFoundError:
        pass
    if not os.path.exists(out_path):
        util.try_file_op(lambda: os.mkdir(out_path), "Output directory could not be created (permissions issue?)")
    elif not os.path.isdir(out_path):
        output.print_fatal("Output directory does not exist or is file")
        exit(1)
    if os.path.exists(read_file):
        output.print_info("Unbundling " + read_file)

    def do_unbundle():
        with progressbar.ProgressBar(max_value=os.path.getsize(read_file)) as bar:
            with open(read_file, 'rb') as file_handle:
                opening = file_handle.read(len(magic))

                if opening != magic:
                    output.corrupt()

                next_obj = file_handle.read(1)
                while next_obj != b'':
                    file_handle.seek(-1, os.SEEK_CUR)

                    file_n = file_handle.read(4096)
                    if file_n == b'':
                        output.corrupt()
                    file_n = remove_excess_null_chars(file_n).decode('utf-8')

                    file_s = file_handle.read(8)
                    if file_s == b'':
                        output.corrupt()
                    file_s = size_from_bytes(file_s)

                    file_c = file_handle.read(file_s)
                    if file_c == b'':
                        output.corrupt()

                    path = os.path.normpath(file_n)
                    path = path.split(os.sep)
                    path.insert(0, out_path)

                    create_directories(path)

                    def mv_file():
                        with open(os.path.join(*path), "wb") as out:
                            out.write(file_c)

                    util.try_file_op(mv_file, "Couldn't extract file from archive (permissions issue?)")

                    next_obj = file_handle.read(1)

                    bar.update(file_handle.tell())

    util.try_file_op(do_unbundle,
                     "File not found, or a directory: " + read_file + ". This could be due to a broken link or a permissions "
                                                                      "error.")


def bundle(inputs, args):
    raw_path = [i.replace("~", os.path.expanduser("~")) for i in inputs]
    # "./files ~/Pictures ../PAR_NEW/PAR/venv/lib/python3.10/site-packages/tensorflow/include/external/com_github_grpc_grpc/include/grpcpp/impl/codegen/core_codegen_interface.h"\
    paths = []
    for i in raw_path:
        if os.name == "nt":
            path = pathlib.PureWindowsPath(pathlib.WindowsPath(i).resolve(strict=True)).as_posix()
        else:
            path = pathlib.Path(i).resolve(strict=True).as_posix()

        if path == "/":
            output.print_warn(
                "You are attempting to add the root directory to the bundle (odds are you do not wish to do this)")
            output.yes_no("Continue?", lambda: None, lambda: exit(1))

        paths += [os.path.join(dp, f) for dp, dn, filenames in os.walk(path) for f in filenames] if not os.path.isfile(
            path) else [path]

    gcf = None
    if not args.keep_full_path:
        paths, gcf = find_greatest_common_factor(paths)

    if args.verbose:
        print_tree(paths)
    output.print_info("Bundling " + str(len(paths)) + " files")

    def do_unbundle():
        with open(args.output, 'wb') as file_handle:
            file_handle.write(magic)
            for file in progressbar.progressbar(paths):
                file_handle.write(pad_filename(file))

                def open_file():
                    with open(os.path.join(gcf, file) if gcf is not None else file, 'rb') as content_file:
                        content_file_loaded = content_file.read()
                        file_handle.write(size_to_bytes(content_file.tell()))
                        file_handle.write(content_file_loaded)

                util.try_file_op(open_file,
                                 "Couldn't open " + file + ". This could be due to a broken link or a permissions "
                                                           "error.")

    util.try_file_op(do_unbundle,
                     "Couldn't open " + args.output + ". This could be due to a broken link or a permissions "
                                                      "error.")
