import ctypes
import numpy as np
import pathlib

# Load the shared library
libtmscore = ctypes.CDLL(pathlib.Path(__file__).parent.resolve().joinpath('libtmscore.so'))

libtmscore.TMscore.argtypes = [ctypes.c_int, np.ctypeslib.ndpointer(dtype = np.int32), np.ctypeslib.ndpointer(dtype = np.float64), ctypes.POINTER(ctypes.c_char_p)]
libtmscore.TMscore.restype = ctypes.c_int

libtmscore.TMscore_buffer.argtypes = [ctypes.c_int, np.ctypeslib.ndpointer(dtype = np.int32), np.ctypeslib.ndpointer(dtype = np.float64), ctypes.POINTER(ctypes.c_char_p), ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
libtmscore.TMscore_buffer.restype = ctypes.c_int



def compute_tm_score(argc, argv):
    # Convert the list of strings to an array of C-style strings (char *)
    argv_ctypes = (ctypes.c_char_p * (argc + 1))()
    argv_ctypes[0] = ctypes.c_char_p("TMscore".encode('utf-8'))
    for i, arg in enumerate(argv):
        argv_ctypes[i + 1] = ctypes.c_char_p(arg.encode('utf-8'))

    length = np.array([0, 0], dtype = np.int32)
    res = np.array([0, 0], dtype = np.float64)
    ret_status = libtmscore.TMscore(argc + 1, length, res, argv_ctypes)

    # assert ret_status == 0
    return length, res


def compute_tm_score_buffer(struct_1, struct_2):
    argc = 3
    argv_ctypes = (ctypes.c_char_p * argc)()
    argv_ctypes[0] = ctypes.c_char_p("TMscore".encode('utf-8'))
    argv_ctypes[1] = ctypes.c_char_p("struct1".encode('utf-8'))
    argv_ctypes[2] = ctypes.c_char_p("struct2".encode('utf-8'))

    length = np.array([0, 0], dtype = np.int32)
    res = np.array([0, 0], dtype = np.float64)

    buffer1 = ctypes.c_char_p(struct_1.encode('utf-8'))
    buffer1_len = len(struct_1)
    buffer2 = ctypes.c_char_p(struct_2.encode('utf-8'))
    buffer2_len = len(struct_2)
    ret_status = libtmscore.TMscore_buffer(argc, length, res, argv_ctypes, buffer1, buffer1_len, buffer2, buffer2_len)

    # assert ret_status == 0
    return length, res


def TMscore(struct_1, struct_2):
    if struct_1.endswith(".pdb") and struct_2.endswith(".pdb"):
        return compute_tm_score(2, [struct_1, struct_2])
    else:
        return compute_tm_score_buffer(struct_1, struct_2)



if __name__ == "__main__":
    import subprocess

    path_1 = "sample1.pdb"
    path_2 = "sample2.pdb"
    buffer1 = ''
    with open(path_1, "r") as fr:
        for line in fr:
            buffer1 += line
    
    buffer2 = ''
    with open(path_2, "r") as fr:
        for line in fr:
            buffer2 += line

    print(subprocess.check_output(['./TMscore', path_1, path_2]).decode("utf-8"))
    print(TMscore(buffer1, buffer2))
    print(TMscore(path_1, path_2))
