from typing import Optional

START_OF_PACKET_MARKER_LENGTH = 4
START_OF_MESSAGE_MARKER_LENGTH = 14


def parse_input(filename='input.txt') -> str:
    """
    Obtain the datastream buffer from file.

    :param filename: path to the input file.
    :return: the datastream buffer.
    """
    with open(filename, 'r') as fp:
        datastream_buffer = fp.read().strip()

    return datastream_buffer


def find_marker_end(datastream_buffer: str, marker_length: int) -> Optional[int]:
    """
    Identify the first position after a specified number of consecutive characters that are all different.

    :param datastream_buffer: the input datastream.
    :param marker_length: the length of the requested marker.
    :return: the index of the datastream after the marker, or None if not present.
    """
    for i in range(len(datastream_buffer) - marker_length):
        if len(set(datastream_buffer[i:i + marker_length])) == marker_length:
            return i + marker_length
    return None


if __name__ == '__main__':
    datastream_buffer = parse_input()

    packet_marker_index = find_marker_end(datastream_buffer, START_OF_PACKET_MARKER_LENGTH)
    print(f"The start-of-packet marker was found at index {packet_marker_index}.")

    message_marker_index = find_marker_end(datastream_buffer, START_OF_MESSAGE_MARKER_LENGTH)
    print(f"The start-of-message marker was found at index {message_marker_index}.")
