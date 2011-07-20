Summary: nginx [engine x] is a HTTP and reverse proxy server, as well as a mail proxy server.
Name: nginx
Version: 1.0.4
Release: 1
License: BSD
Group: System Environment/Daemons
URL: http://www.nginx.org
Packager: Mike Willbanks <mike@digitalstruct.com>

Source: http://nginx.org/download/nginx-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
nginx [engine x] is a HTTP and reverse proxy server, as well as a mail proxy server written by Igor Sysoev.

%prep
%setup -q

./configure --prefix=/usr/local/nginx --with-http_ssl_module --without-mail_pop3_module --without-mail_imap_module --without-mail_smtp_module --with-http_stub_status_module
%build
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install  DESTDIR="%{buildroot}" AM_INSTALL_PROGRAM_FLAGS=""

%clean
%{__rm} -rf %{buildroot}

%files
/usr/local/nginx/*

%pre

%post
ln -s /var/log/nginx /usr/local/nginx/logs
ln -s /etc/nginx /usr/local/nginx/conf

%changelog
* Wed Jul 13 2011 Mike Willbanks <mike@digitalstruct.com> - 1.0.4-1
- initial package
