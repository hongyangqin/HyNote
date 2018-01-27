# Download a single folder or directory from a GitHub repo

github 下载单个目录下的文件

Update Sep. 2016: there are a few tools created by the community that
can do this for you:

  - [GitZip](http://kinolien.github.io/gitzip) (Credits to
    [Kino](https://stackoverflow.com/users/2238770/kino) - upvote his
    answer [**right
    here\!**](https://stackoverflow.com/questions/7106012/download-a-single-folder-or-directory-from-a-github-repo/33753575#33753575))

  - [DownGit](https://minhaskamal.github.io/DownGit) (Credits to [Minhas
    Kamal](https://stackoverflow.com/users/4684058/minhas-kamal?tab=profile)
    - upvote his answer [**right
    here\!**](https://stackoverflow.com/questions/7106012/download-a-single-folder-or-directory-from-a-github-repo/38879691#38879691))

-----

Git doesn't support this, but Github does via SVN. If you checkout your
code with subversion, Github will essentially convert the repo from git
to subversion on the backend, then serve up the requested directory.

Here's how you can use this feature to download a specific folder. I'll
use the popular javascript library `lodash` as an example.

1.  **Get the repo URL**. First, copy the URL of the Github repo to your
    clipboard. ![](https://i.stack.imgur.com/7ga2M.png)

2.  **Modify the URL for subversion**. I want to download the folder at
    `/docs` from the `master` branch, so I will append `trunk/docs`.
    Full URL is now `https://github.com/lodash/lodash/trunk/docs`. See
    my note below for a more in-depth explanation of why we must use
    this URL format.

3.  **Download the folder**. Go to the command line and grab the folder
    with SVN. ` svn checkout
    https://github.com/lodash/lodash/trunk/docs`

You might not see any activity immediately because Github takes up to 30
seconds to convert larger repositories, so be patient.

> *Full URL format explanation:*
> 
>   - If you're interested in `master` branch, use `trunk` instead. So
>     the full path is `trunk/foldername`
>   - If you're interested in `foo` branch, use `branches/foo` instead.
>     The full path looks like `branches/foo/foldername`
>   - Protip: You can use `svn ls` to see available tags and branches
>     before downloading if you wish

That's all\! Github [supports more subversion
features](https://help.github.com/articles/support-for-subversion-clients/)
as well, including support for committing and pushing changes.
