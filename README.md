# hello-world
My first Github repository
           Your full name to be recorded in any newly created commits. Can be overridden by the GIT_AUTHOR_NAME and GIT_COMMITTER_NAME environment variables. See git-commit-tree(1).

       user.signingKey
           If git-tag(1) or git-commit(1) is not selecting the key you want it to automatically when creating a signed tag or commit, you can override the default selection with this variable. This
           option is passed unchanged to gpg’s --local-user parameter, so you may specify a key using any method that gpg supports.

       versionsort.prereleaseSuffix
           When version sort is used in git-tag(1), prerelease tags (e.g. "1.0-rc1") may appear after the main release "1.0". By specifying the suffix "-rc" in this variable, "1.0-rc1" will appear
           before "1.0".

           This variable can be specified multiple times, once per suffix. The order of suffixes in the config file determines the sorting order (e.g. if "-pre" appears before "-rc" in the config
           file then 1.0-preXX is sorted before 1.0-rcXX). The sorting order between different suffixes is undefined if they are in multiple config files.

       web.browser
           Specify a web browser that may be used by some commands. Currently only git-instaweb(1) and git-help(1) may use it.

GIT
       Part of the git(1) suite

Git 2.7.4                                                                                     11/27/2018                                                                                 GIT-CONFIG(1)
test branch.....
iss53 fixing...
####################
=======
I am changing in b1

