import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--min_length", type=int,
                    help="minimum  length for the  read")
parser.add_argument("--keep_filtered", action='store_true', help="if --keep_filtered return filtered reads in file")
parser.add_argument("--gc_bounds", nargs="+", help="Enter minimum/maximum/nothing/minimum and maximum for GC content")
parser.add_argument("--fastq", required=True, help="Path to fastq file for filtering")
parser.add_argument("--output_base_name", help="Prefix for names of the created files")
args = parser.parse_args()

def _check_gc_content(read: list, minimum: int, maximum: int):
    """Filter by GC content. Including soft masking fastqc"""
    gc_percent = 100 * (read[1].count("G") + read[1].count("g") + read[1].count("C") + read[1].count("c")) / len(
        read[1])
    if minimum < gc_percent < maximum:
        return True
    return False


def _check_length(read: list, threshhold: int):
    if len(read[1]) > threshhold:
        return True
    return False

filter_fastqc()
