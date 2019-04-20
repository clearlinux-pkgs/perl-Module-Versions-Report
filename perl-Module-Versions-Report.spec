#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Module-Versions-Report
Version  : 1.06
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/J/JE/JESSE/Module-Versions-Report-1.06.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JE/JESSE/Module-Versions-Report-1.06.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmodule-versions-report-perl/libmodule-versions-report-perl_1.06-2.debian.tar.xz
Summary  : report versions of all modules in memory
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
Time-stamp: "2003-06-21 23:18:00 AHDT"
NAME
Module::Versions::Report -- report versions of all modules in memory

%package dev
Summary: dev components for the perl-Module-Versions-Report package.
Group: Development
Provides: perl-Module-Versions-Report-devel = %{version}-%{release}

%description dev
dev components for the perl-Module-Versions-Report package.


%prep
%setup -q -n Module-Versions-Report-1.06
cd ..
%setup -q -T -D -n Module-Versions-Report-1.06 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Module-Versions-Report-1.06/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Module/Versions/Report.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Module::Versions::Report.3
