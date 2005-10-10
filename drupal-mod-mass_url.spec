%define		modname mass_url
Summary:	Drupal Mass URL Module
Name:		drupal-mod-%{modname}
Version:	0.1.cvs
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/mass_url-cvs.tar.gz
# Source0-md5:	078b154e6674e6d583ccfa76f4883c88
URL:		http://drupal.org/node/13215
Requires:	drupal >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_drupaldir	%{_datadir}/drupal
%define		_moddir		%{_drupaldir}/modules

%description
A module that allows for easy mass url aliasing, not requiring the use
of path.module for many types of common URLs.

Currently this module only supports user page and user blog URLs.

When installed, a user's account page is accessible via
<http://example.com/user/username>, and a user's blog is accessible
via <http://example.com/blog/username>. 

As of now, only view functions are available (no edit for account
pages), and user names must be entered exactly as they are formatted
(including spaces). I hope to implement some kind of fuzzy filtering
soon, but that's a big task...

%prep
%setup -q -n %{modname}
rm -f LICENSE.txt # GPL v2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_moddir}

install *.module $RPM_BUILD_ROOT%{_moddir}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc *.txt
%{_moddir}/*.module
