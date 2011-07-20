%define _prefix /usr/local
%define _sysconfdir /usr/local/etc
%define _localstatedir /usr/local/var
%define _mandir /usr/local/share/man
%define _infodir /usr/local/share/info

Summary: VIM 7.3
Name: vim73
Version: 1
Release: 1
License: BSD
Group: Applications/Editors
BuildRequires: gcc-c++ ncurses-devel
Requires: ncurses
URL: http://www.vim.org

Packager: Mike Willbanks <mike@digitalstruct.com>

Source: ftp://ftp.vim.org/pub/vim/unix/vim-7.3.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Vim is an advanced text editor that seeks to provide the power of the de-facto Unix editor 'Vi', with a more complete feature set.

%prep
%setup -q -n vim73

%build
./configure --build=x86_64-redhat-linux-gnu --host=x86_64-redhat-linux-gnu --target=x86_64-redhat-linux-gnu --prefix=/usr/local --with-features=huge --disable-selinux --disable-darwin --enable-multibyte
%{__make} %{_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install  DESTDIR="%{buildroot}" AM_INSTALL_PROGRAM_FLAGS=""

%clean
%{__rm} -rf %{buildroot}

%post
echo 'alias vi=/usr/local/bin/vim
alias vim=/usr/local/bin/vim' > /etc/profile.d/vim.sh
chmod +x /etc/profile.d/vim.sh
source /etc/profile.d/vim.sh

%files
%{_datadir}/*
%{_bindir}/*

%changelog
* Fri Feb  4 2011 Mike Willbanks <mike@digitalstruct.com> - 7.3-1
- Initial vim build
