with open('logfile.txt') as logfile, open('output.txt', 'w') as output:
    for line in logfile:
        name, in_time, out_time = line.split(',')
        in_time = in_time.replace(':', '.')
        out_time = out_time.replace(':', '.')
        time = abs(float(in_time) - float(out_time))
        if time >= 1:
            print(name, file=output)


#  reference solutions
def get_diff_mins(time2, time1):
    t2 = list(map(int, time2.split(':')))
    t1 = list(map(int, time1.split(':')))
    return (t2[0]*60 + t2[1]) - (t1[0]*60 + t1[1])

with open('logfile.txt', encoding='utf-8') as inputf, open('output.txt', 'w') as outputf:
    for fn in inputf:
        name, time1, time2 = fn.strip().split(', ')
        if get_diff_mins(time2, time1) >= 60:
            print(name, file=outputf)
