#!/usr/bin/python
from __future__ import print_function
import json
from sys import argv
import os
import subprocess


def _read_git_log(repo_name):
    file_name = "stat.txt"
    result = [repo_name, ]
    cc, fc, ic, dc = (0, 0, 0, 0)
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
#            cc, fc, ic, dc = (0, 0, 0, 0)
            try:
                l = line.split(",")
                cc += 1
                for e in l:
                    if "changed" in e:
                        fc += int(e.split(" ")[0])
                    elif "insertion" in e:
                        ic += int(e.split("insertion")[0])
                    elif "deletion" in e:
                        dc += int(e.split("deletion")[0])
            except ValueError:
                print("line from stat.txt is not properly formatted:\n",line)
        for i in [str(cc), str(fc), str(ic), str(dc)]:
            result.append(i)

    return result


if __name__ == '__main__':
    startdate = argv[1] #2017-1-31
    enddate = argv[2] #2018-1-31
    t_result = []
    data = json.load(open('repos'))
    for d in data:
        if not d['fork']:  # not forked from other
            repo_name = d['full_name'].split('/')[-1]
            if os.path.exists(repo_name):
                os.chdir(repo_name)
                subprocess.call(["git", "pull", 'origin', 'master'])
                os.chdir('../')
            else:
                subprocess.call(["git", "clone", 'https://github.com/' + d['full_name']])
            os.chdir(repo_name)
            if not os.path.exists('stat.sh'):
                subprocess.call(["ln", '-s', '../stat.sh'])
            subprocess.call(["./stat.sh", startdate, enddate])
            result = _read_git_log(repo_name)
            t_result.append(result)
            os.chdir('../')
    with open('repo.stat', 'w') as output_file:
        for r in t_result:
            output_file.write(','.join(r) + '\n')
    print('Report generated')
