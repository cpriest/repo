## Public Repo
This is my publicly accessible RPM repository, I publish any packages I build here.  Sometimes I include the -release packages from other repos I commonly use for ease of installation.

Use completely at your own risk.

### CentOS Repo Installation

You may install my repository by running this:

```
yum install https://cpriest.github.io/repo/CentOS/noarch/cpriest-repo-release-latest.noarch.rpm
```

### Alpine (edge/3.11) Repository

```
# Add repository to /etc/apk/repositories
echo 'https://cpriest.github.io/repo/alpine/edge' | tee -a /etc/apk/repositories

# Note: if you want this repository to take priority over other repos, you'll need to edit /etc/apk/repositories and change its location, the higher up the higher priority.

# Download and store signing key to /etc/apk/keys
wget -P /etc/apk/keys/ https://cpriest.github.io/repo/alpine/abuild-cpriest.rsa.pub
```
