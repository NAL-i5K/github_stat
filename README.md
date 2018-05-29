# github_stat

Download repos list of a GitHub organization using [Github API](https://developer.github.com/v3/repos/#list-organization-repositories)
```
# save it as a file named 'repos' and put in the github_stat/ directory.
curl https://api.github.com/orgs/NAL-i5K/repos > repos
```


Usage: 
```
python stat_github.py <year> 
ex: python stat_github.py 2017
```

Output format: (file name: repos.stat)
```
repo1, <number of commit, number of file changed, number of insertion, number of deletion> X 12 (Jan, ... , Dec)
repo2, ...
repo3, ...
```
