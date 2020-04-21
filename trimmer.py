import argparse
import secondary_functions as sf
parser = argparse.ArgumentParser()
parser.add_argument("--min_length", type=int,
                    help="minimum  length for the  read")
parser.add_argument("--keep_filtered", action='store_true', help="if --keep_filtered return filtered reads in file")
parser.add_argument("--gc_bounds", nargs="+", help="Enter minimum/maximum/nothing/minimum and maximum for GC content")
parser.add_argument("--fastq", required=True, help="Path to fastq file for filtering")
parser.add_argument("--output_base_name", help="Prefix for names of the created files")
parser.add_argument("--crop")
parser.add_argument("--headcrop")
parser.add_argument("--leading")
parser.add_argument("--trailing")
args = parser.parse_args()
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def filter_fastqc(file=args.fastq,
                  min_length=args.min_length,
                  gc_content_bounds=args.gc_bounds,
                  crop=args.crop,
                  headcrop=args.headcrop,
                  leading=args.leading,
                  trailing=args.trailing):
    data_by_read = sf._read_fastq(file)
    total_len_reads = len(data_by_read)
    if gc_content_bounds is not None:
        gc_content_bounds = [int(bound) for bound in gc_content_bounds]
        if len(gc_content_bounds) == 1 and 0 <= gc_content_bounds[0] <= 100:
            gc_content_bounds.append(100)
        elif len(gc_content_bounds) == 2 and 0 <= gc_content_bounds[0] <= 100 and 0 <= gc_content_bounds[1] <= 100:
            pass
        else:
            raise Exception("Check gc_bounds parameter input")
    if gc_content_bounds is None:
        gc_content_bounds = [0, 100]
    passed_reads = []
    failed_reads = []
    for read in data_by_read:
        if sf._check_length(read=read, threshhold=min_length) and sf._check_gc_content(read, minimum=gc_content_bounds[0],
                                                                                 maximum=gc_content_bounds[1]):
            passed_reads.append(read)
        else:
            if args.keep_filtered:
                failed_reads.append(read)
    print(f"{bcolors.FAIL}{total_len_reads-len(passed_reads)} reads dropped by length and gc content filter{bcolors.ENDC}")
    for read in passed_reads:
        read = sf._crop(read, crop)
        read = sf._headcrop(read, headcrop)
        read = sf._leading(read, leading)
        read = sf._trailing(read, trailing)
    if args.output_base_name is not None:
        output_name = args.output_base_name
    else:
        output_name = "fastq"
    if args.keep_filtered:
        with open(output_name + "_failed.fastq", "w") as failed:
            for read in failed_reads:
                for line in read:
                    failed.write(line + "\n")
    with open(output_name + "_passed.fastq", "w") as passed:
        for read in passed_reads:
            for line in read:
                passed.write(line + "\n")


if __name__ == "__main__":
    filter_fastqc()
