## Update on 12/30

For myself: I should try to update everyday, just for avoiding forgetting how to use this theme. If forgot, check https://github.com/liuzc/LeaveIt

### I made a repo inside public, so can push to linna-li.github.io.git directly

```md
lilinna:blog/ (master✗) $ git remote -v [13:24:56]
origin https://github.com/linna-li/blog-resource.git (fetch)
origin https://github.com/linna-li/blog-resource.git (push)

lilinna:public/ (master) $ git remote -v [13:25:17]
origin https://github.com/linna-li/linna-li.github.io.git (fetch)
origin https://github.com/linna-li/linna-li.github.io.git (push)
```

### How to make a new blog

- add md file in content/posts
- hugo -t LeaveIt
- git add --all, git commit -m "commit for content", git push
- cd public
- git add --all, git commit -m "commit for public", git push

### How to update locally
- git fetch origin
- git reset --hard origin/master

### Issue

- The year folder in public couldn't be updated
- Theme fold could be removed by mistake
