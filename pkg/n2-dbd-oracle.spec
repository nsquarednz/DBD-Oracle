Name: %(echo $PACKAGE)
Version: %(echo $VERSION)
# Release is passed through to our script. We concatenate on the dist flag.
# Dist is a magic variable that will populate our version. I.E. EL8.
Release: %(echo $RELEASE)%{?dist}
Summary: Oracle Perl Modules for the Perl DBI database utility.
Group: Development/Languages/Perl
License: Perl
URL: https://github.com/nsquarednz/n2-DBD-Oracle
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%global _binaries_in_noarch_packages_terminate_build 0

#BuildRequires:
# Define some dependencies that we require in order to use this module.
# This module expects the base Oracle instant client modules to be install from:
#   http://yum.oracle.com/repo/OracleLinux/OL8/oracle/instantclient21/x86_64
# The base Perl DBI module.
Requires: oracle-instantclient-basic oracle-instantclient-devel oracle-instantclient-sqlplus perl(DBI)

%description
N-Squared Software fork of 1.8.x of the Perl DBD Oracle module.

%post

#
# All build steps are done by build-packages.sh.
#

%prep

#
# All build steps are done by build-packages.sh.
#

%build

#
# All build steps are done by build-packages.sh.
#

%install

rm -rf %{buildroot}
cp -r %{_builddir} %{buildroot}
find %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)

# Include the core files needed to execute the library code.
/usr/local/lib64/perl5/auto/DBD/Oracle/.packlist
/usr/local/lib64/perl5/auto/DBD/Oracle/dbdimp.h
/usr/local/lib64/perl5/auto/DBD/Oracle/ocitrace.h
/usr/local/lib64/perl5/auto/DBD/Oracle/Oracle.h
/usr/local/lib64/perl5/auto/DBD/Oracle/Oracle.so
/usr/local/lib64/perl5/auto/DBD/Oracle/mk.pm
/usr/local/lib64/perl5/DBD/Oracle.pm
/usr/local/lib64/perl5/DBD/Oracle/Object.pm
/usr/local/lib64/perl5/DBD/Oracle/Troubleshooting.pod
/usr/local/lib64/perl5/DBD/Oracle/Troubleshooting
/usr/local/lib64/perl5/DBD/Oracle/Troubleshooting/Aix.pod
/usr/local/lib64/perl5/DBD/Oracle/Troubleshooting/Linux.pod
/usr/local/lib64/perl5/DBD/Oracle/Troubleshooting/Win64.pod
/usr/local/lib64/perl5/DBD/Oracle/Troubleshooting/Win32.pod
/usr/local/lib64/perl5/DBD/Oracle/Troubleshooting/Sun.pod
/usr/local/lib64/perl5/DBD/Oracle/Troubleshooting/Vms.pod
/usr/local/lib64/perl5/DBD/Oracle/Troubleshooting/Cygwin.pod
/usr/local/lib64/perl5/DBD/Oracle/Troubleshooting/Hpux.pod
/usr/local/lib64/perl5/DBD/Oracle/Troubleshooting/Macos.pod
/usr/local/lib64/perl5/DBD/Oracle/GetInfo.pm
# Bundle the DBD man pages.
/usr/local/share/man/man3/DBD::Oracle::Troubleshooting::Linux.3pm
/usr/local/share/man/man3/DBD::Oracle::Troubleshooting::Cygwin.3pm
/usr/local/share/man/man3/DBD::Oracle::Troubleshooting::Win64.3pm
/usr/local/share/man/man3/DBD::Oracle::Troubleshooting::Sun.3pm
/usr/local/share/man/man3/DBD::Oracle::Troubleshooting.3pm
/usr/local/share/man/man3/DBD::Oracle::Troubleshooting::Win32.3pm
/usr/local/share/man/man3/DBD::Oracle::Troubleshooting::Aix.3pm
/usr/local/share/man/man3/DBD::Oracle::Troubleshooting::Vms.3pm
/usr/local/share/man/man3/DBD::Oracle::Troubleshooting::Hpux.3pm
/usr/local/share/man/man3/DBD::Oracle::Troubleshooting::Macos.3pm
/usr/local/share/man/man3/DBD::Oracle.3pm

%changelog
