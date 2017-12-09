### install
```
  $ mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
  $ rpmbuild -bb SPECS/zap.spec
```

```vim /etc/default/java
export JAVA_HOME=/usr/java/default
export JAVA_OPTS=" -Xmx1024m -Xms1024M"
```

