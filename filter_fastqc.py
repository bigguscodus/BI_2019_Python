import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--min_length", type=int,
                    help="minimum  length for the  read")
parser.add_argument("--keep_filtered", action='store_true', help="if --keep_filtered return filtered reads in file")
parser.add_argument("--gc_bounds", nargs="+", help="Enter minimum/maximum/nothing/minimum and maximum for GC content")
parser.add_argument("--fastq", required=True, help="Path to fastq file for filtering")
parser.add_argument("--output_base_name", help="Prefix for names of the created files")
args = parser.parse_args()




filter_fastqc()
