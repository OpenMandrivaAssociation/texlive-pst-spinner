Name:		texlive-pst-spinner
Version:	61719
Release:	2
Summary:	Drawing a fidget spinner
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pst-spinner
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-spinner.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-spinner.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package aims to propose a model of the fidget spinner
gadget. It exists under different forms with 2, 3 poles and
even more. We chose the most popular model: the triple Fidget
Spinner. You can run the PSTricks related documents with
XeLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pst-spinner
%{_texmfdistdir}/tex/generic/pst-spinner
%{_texmfdistdir}/dvips/pst-spinner
%doc %{_texmfdistdir}/doc/generic/pst-spinner

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
