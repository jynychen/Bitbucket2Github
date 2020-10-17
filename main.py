from github import Github
import sys

def sourceimport(import_name, import_url):
    buser = ""
    bpwd  = ""
    gtoken  = ""
    g = Github(gtoken)
    org = g.get_organization("")

    repoprefix = "Bitbucket-"
    reponame = repoprefix + import_name
    print(reponame)

    try:
        org.create_repo(reponame, private=True)
    except:
        pass

    return org.get_repo(reponame).create_source_import(
        "git",
        import_url,
        buser,
        bpwd,
    )


tmp = sys.argv[1]
si = sourceimport(
    tmp,
    "uil"+tmp+".git"
)
print(si.html_url)