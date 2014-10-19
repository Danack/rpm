Name:           php
Version:        5.3.6
Release:        1%{?dist}
Summary:        PHP is a widely-used general-purpose scripting language.

Group:          Development/Languages
License:        PHP License v3.01
URL:            http://www.php.net
Source0:        http://www.php.net/distributions/php-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Obsoletes:      php
BuildRequires:  enchant-devel curl-devel pcre-devel libmcrypt-devel MySQL-devel
BuildRequires:  giflib-devel libjpeg-devel freetype-devel libpng-devel
BuildRequires:  libmcrypt-devel libtidy-devel zlib-devel sqlite-devel
BuildRequires:  gettext-devel intltool fcgi-devel

%description
PHP is a widely-used general-purpose scripting language that is especially
suited for Web development and can be embedded into HTML.

%prep
%setup -q -n %{name}-%{version}
%build
EXTENSION_DIR=%{_libdir}/php/modules; export EXTENSION_DIR
%configure --with-layout=GNU --with-libdir=lib64 --with-enchant \
--enable-fpm --with-gd --enable-intl --enable-mbstring --enable-pcntl \
--enable-soap --enable-sockets --enable-sqlite-utf8 --enable-zip --with-zlib \
--with-curl --with-jpeg-dir --with-png-dir --with-zlib-dir --with-gettext \
--with-mcrypt --with-mysql=mysqlnd --with-mysqli=mysqlnd --with-pdo-mysql=mysqlnd \
--with-pdo-sqlite --with-tidy --with-pear=%{_datadir}/php/pear --disable-debug

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_initrddir}
install -Dp -m0755 sapi/fpm/init.d.php-fpm %{buildroot}%{_initrddir}/php-fpm
%{__make} install INSTALL_ROOT="%{buildroot}"

%post
%/sbin/chkconfig --add php-fpm
%/sbin/chkconfig --level 2345 php-fpm on

%preun
if [ "$1" = 0 ] ; then
    /sbin/service php-fpm stop > /dev/null 2>&1
    /sbin/chkconfig --del php-fpm
fi
exit 0

%postun
if [ "$1" -ge 1 ]; then
    /sbin/service php-fpm condrestart > /dev/null 2>&1
fi
exit 0

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_sbindir}/*
%{_includedir}/*
%{_libdir}/*
%{_mandir}/man1/php*
%{_sysconfdir}/*
%{_datadir}/*
%{_initrddir}/*
%exclude /.channels
%exclude /.depdb
%exclude /.depdblock
%exclude /.filemap
%exclude /.lock

%changelog
* Tue Feb 23 2011 Mike Willbanks <mike@_________.com> - 5.3.5-1
- Initial Package
