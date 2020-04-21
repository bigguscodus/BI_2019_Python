import os
def _read_fastq(path):
    if os.path.exists(path) == False or path is None:
        raise FileExistsError("Fastq file doesn't exist")
    with open(path, "r") as file:
        data = file.readlines()
        data = [line.strip() for line in data]
        data_by_read = [data[index:index + 4] for index in
                        range(0, len(data), 4)]  # make sublists from list. One sublist - one read
        return data_by_read


def _phread_encoding():
    prhred_symbols = [chr(value) for value in range(33, 74)]
    real_scores = [value for value in range(0, 41)]
    prhred_scores_dict = dict(zip(prhred_symbols, real_scores))
    return prhred_scores_dict


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


def _recode_quality(quality: list):
    rule = _phread_encoding()
    recoded_quality = list()
    for value in quality:
        recoded_quality.append(rule[value])
    return recoded_quality


def _measure_mean_quality(quality: list):
    recoded_quality = _recode_quality(quality)
    mean = sum(recoded_quality) / len(recoded_quality)
    return mean


def _raiseValueError(value, argument):
    try:
        value = int(value)
    except ValueError:
        raise ValueError(f"{argument} argument must be interger")
    return value


def _headcrop(read, n):
    if n is None:
        return read
    n = _raiseValueError(n, "headcrop")
    read[1] = read[1][n:]
    read[3] = read[3][n:]
    return read


def _crop(read, n):
    if n is None:
        return read
    n = _raiseValueError(n, "crop")
    read[1] = read[1][:n]
    read[3] = read[3][:n]
    return read


def _leading(read, threshhold):
    if threshhold is None:
        return read
    threshhold = _raiseValueError(threshhold, "leading")
    recoded_quality = _recode_quality(read[3])
    breaker = 0
    for value in recoded_quality:
        if value < threshhold:
            breaker += 1
        else:
            break
    read[1] = read[1][breaker:]
    read[3] = read[3][breaker:]
    return read


def _trailing(read, threshhold):
    if threshhold is None:
        return read
    threshhold = _raiseValueError(threshhold, "trailing")
    read[1] = read[1][::-1]
    read[3] = read[3][::-1]
    read = _leading(read, int(threshhold))
    read[1] = read[1][::-1]
    read[3] = read[3][::-1]
    return read
