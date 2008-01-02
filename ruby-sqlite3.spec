%define rname sqlite3
%define name  ruby-%{rname}
%define oname %{rname}-ruby

%define version 1.2.1
%define release %mkrel 1

Summary: Ruby interface for the SQLite3 database engine
Name: %name
Version: %version
Release: %release
License: BSD-like
Group: Development/Ruby
URL: http://rubyforge.org/projects/sqlite-ruby/
Source0: %{oname}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: ruby-devel sqlite3-devel ruby-flexmock swig
Provides: %{oname}

%description
Ruby interface for the SQLite database engine.

%prep
%setup -q -n %{oname}-%{version}
perl -pi -e 's/555/755/' setup.rb

%build
ruby setup.rb config
ruby setup.rb setup

%check
# Needs flexmock < 0.1.0
#ruby -Ilib test/tests.rb

%clean
rm -rf %buildroot

%install
rm -rf %buildroot
ruby setup.rb install --prefix=%buildroot

%files
%defattr(-,root,root)
%{ruby_sitelibdir}/%{rname}*
%{ruby_sitearchdir}/%{rname}*
%doc ChangeLog LICENSE README api/ doc/

