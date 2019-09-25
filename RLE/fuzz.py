from fuzzing.fuzzer import FuzzExecutor

input_files = ['enkoding.txt']

target = ['python & rle.py -e']

def test():
    fuzzer = FuzzExecutor(target,input_files)
    fuzzer.run_test(20)
    return fuzzer.stats

if __name__ == '__main__':
    print(test())
