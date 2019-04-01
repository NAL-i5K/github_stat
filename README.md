# github_stat

Download repos list of a GitHub organization using [Github API](https://developer.github.com/v3/repos/#list-organization-repositories)
```
# save it as a file named 'repos' and put in the github_stat/ directory.
curl https://api.github.com/orgs/NAL-i5K/repos?per_page=500 > repos
```


Usage: 
```
python stat_github.py <startdate> <enddate> 
ex: python stat_github.py 2017-10-1 2018-9-30
```

Output format: (file name: repos.stat)
```
repo1, <number of commit, number of file changed, number of insertion, number of deletion> 
repo2, ...
repo3, ...
```
