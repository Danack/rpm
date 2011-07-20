Name:           memcached
Version:        1.4.5
Release:        1%{?dist}
Summary:        High Performance, Distributed Memory Object Cache

Group:          System Environment/Daemons
License:        BSD
URL:            http://www.danga.com/memcached/
Source0:        http://memcached.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)

BuildRequires:  libevent-devel
BuildRequires:  perl(Test::More)
BuildRequires:  /usr/bin/prove
Requires: initscripts
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig, /sbin/service
Requires(postun): /sbin/service

%description
memcached is a high-performance, distributed memory object caching
system, generic in nature, but intended for use in speeding up dynamic
web applications by alleviating database load.

%prep
%setup -q -n %{name}-%{version}


%build
%configure --enable-replication --enable-64bit

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# remove memcached-debug
rm -f %{buildroot}/%{_bindir}/memcached-debug

# Perl script for monitoring memcached
install -Dp -m0755 scripts/memcached-tool %{buildroot}%{_bindir}/memcached-tool

# Init script
install -Dp -m0755 scripts/memcached.sysv %{buildroot}%{_initrddir}/memcached

# Default configs
mkdir -p %{buildroot}/%{_sysconfdir}/sysconfig
cat <<EOF >%{buildroot}/%{_sysconfdir}/sysconfig/%{name}
PORT="11211"
USER="memcached"
MAXCONN="1024"
CACHESIZE="1024"
OPTIONS=""
EOF

# pid directory
mkdir -p %{buildroot}/%{_localstatedir}/run/memcached

%clean
rm -rf %{buildroot}


%post
getent group memcached >/dev/null || groupadd -r memcached
getent passwd memcached >/dev/null || useradd -r -g memcached -s /bin/bash -c "Memcached Application User" memcached
/sbin/chkconfig --add %{name}
/sbin/chkconfig --level 2345 %{name} on

%preun
if [ "$1" = 0 ] ; then
    /sbin/service %{name} stop > /dev/null 2>&1
    /sbin/chkconfig --del %{name}
fi
exit 0

%postun
if [ "$1" -ge 1 ]; then
    /sbin/service %{name} condrestart > /dev/null 2>&1
fi
exit 0


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README doc/CONTRIBUTORS doc/*.txt
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}

%dir %attr(750,nobody,nobody) %{_localstatedir}/run/memcached
%{_bindir}/memcached-tool
%{_bindir}/memcached
%{_mandir}/man1/memcached.1*
%{_initrddir}/memcached
%{_includedir}/memcached

%changelog
* Wed Jul 13 2011 Mike Willbanks <mike@digitalstruct.com> - 1.4.5-1
- Upgraded memcached to the latest version
