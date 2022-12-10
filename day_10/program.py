from computer.cpu import CPU
from computer.operations import NoOp, AddX, Program


def read_program(filename: str = "input.txt") -> Program:
    """Read the input file as a program with operations."""
    with open(filename, 'r') as fp:
        ops = [line.strip() for line in fp.readlines() if line]

    # Build list of Operations
    return [NoOp(op) if op == "noop" else AddX(op.split(' ')[0], int(op.split(' ')[1])) for op in ops]


if __name__ == '__main__':
    cpu = CPU()
    program: Program = read_program()

    cpu.run(program)
    print(f"\nSummed signal strength for the requested cycles: {cpu.signal_strength_sum}")
