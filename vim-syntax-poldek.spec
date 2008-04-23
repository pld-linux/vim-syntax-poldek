Summary:	Vim syntax: poldek
Name:		vim-syntax-poldek
Version:	1.1
Release:	1
License:	Charityware
Group:		Applications/Editors/Vim
Source0:	poldek.vim
Source1:	vim-ftdetect-poldek.vim
# for _vimdatadir existence
Requires:	vim >= 4:6.3.058-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles
%define		syntax		poldek

%description
This plugin provides syntax highlighting for poldek config files.

%prep
%setup -qcT
rev=$(awk '/^".*Revision:/{print $5}' %{SOURCE0})
if [ "$rev" != "%{version}" ]; then
	: Update version $rev, and retry
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,ftdetect}
install %{SOURCE0} $RPM_BUILD_ROOT%{_vimdatadir}/syntax/%{syntax}.vim
install %{SOURCE1} $RPM_BUILD_ROOT%{_vimdatadir}/ftdetect/%{syntax}.vim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/%{syntax}.vim
%{_vimdatadir}/ftdetect/%{syntax}.vim
