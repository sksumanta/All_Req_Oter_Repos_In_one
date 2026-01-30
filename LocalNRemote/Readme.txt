
$ cd Local_N_Remot/
$ ls
$ git init
		Initialized empty Git repository in E:/Local_N_Remot/.git/
$ mkdir myProject
$ cd myProject/
$ vi projectFile
$ git status
		On branch master
		No commits yet
		Untracked files:
		(use "git add <file>..." to include in what will be committed)
				./
		nothing added to commit but untracked files present (use "git add" to track)
$ cd ..
$ ls  -lrt
		total 0
		drwxr-xr-x 1 Sumanta 197121 0 Aug 17 08:31 myProject/
$ git add .
$ git commit -m "added a project"
		[master (root-commit) 5b4ab14] added a project
		1 file changed, 1 insertion(+)
		create mode 100644 myProject/projectFile
$ git log
		commit 5b4ab142a3049611d07a9b2e8b7686f73b2b731f (HEAD -> master)
		Author: unknown <sumanta.sahoo98@gmail.com>
		Date:   Sat Aug 17 08:37:00 2019 +0530
		
			added a project
$ git remote -v
$ git remote add origin https://github.com/XXXXXXXXXX/XXXXXXXX.git
$ git push -u origin master

		Enumerating objects: 4, done.
		Counting objects: 100% (4/4), done.
		Delta compression using up to 4 threads
		Compressing objects: 100% (2/2), done.
		Writing objects: 100% (4/4), 322 bytes | 35.00 KiB/s, done.
		Total 4 (delta 0), reused 0 (delta 0)
		To https://github.com/sksumanta/LocalNRemote.git
		* [new branch]      master -> master
		Branch 'master' set up to track remote branch 'master' from 'origin'.

