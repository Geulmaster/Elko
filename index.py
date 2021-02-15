import argparse

class Parser:

    def __init__(self):
        self.args = self.run_arguments()


    def run_arguments(self):
        parser = argparse.ArgumentParser(description="Load test your app")
        #group = parser.add_mutually_exclusive_group()
        parser.add_argument("read", nargs='?', help='Read command, should get index')
        parser.add_argument("write", nargs='?', help="Write command, should get index")
        args = parser.parse_args()
        return args


def runner():
    if arguments.run == "run":
        print("ran")
    if arguments.type == "type":
        print("type")


if __name__ == '__main__':
    parser = Parser()
    arguments = parser.run_arguments()
    runner()
    