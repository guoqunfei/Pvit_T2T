

input_file =  'unlink_info_200bp2.gff'
output_file = 'CpG_island_link.gff'

def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x:x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1] + 1:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    return merged

intervals = []
chromosome = None

with open(input_file, 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith('##'):
            continue
        parts = line.split('\t')
        if len(parts) == 9 and parts[2] == 'CpG_island':
            chrom = parts[0]
            start = int(parts[3])
            end = int(parts[4])
            id_field = parts[8]
            id = id_field.split('=')[1]

            if chromosome is None:
                chromosome = chrom 
            if chrom == chromosome:
                intervals.append((start, end))
            else:
                merged_intervals = merge_intervals(intervals)
                with open(output_file, 'a') as out_f:
                    for i, interval in enumerate(merged_intervals):
                        out_f.write(f"{chromosome}\t.\tCpG_island\t{interval[0]}\t{interval[1]}\t.\t.\t.\tID=CpG_island_{chromosome}_{interval[0]}_{interval[1]}\n")
                chromosome = chrom
                intervals = [(start, end)] 

if intervals:
    merged_intervals = merge_intervals(intervals)
    with open(output_file, 'a') as out_f:
        for i, interval in enumerate(merged_intervals):
            out_f.write(f"{chromosome}\t.\tCpG_island\t{interval[0]}\t{interval[1]}\t.\t.\t.\tID=CpG_island_{chromosome}_{interval[0]}_{interval[1]}\n")
            
