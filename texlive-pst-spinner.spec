%global tl_name pst-spinner
%global tl_revision 66115

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.02
Release:	%{tl_revision}.1
Summary:	Drawing a fidget spinner
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-spinner
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-spinner.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-spinner.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package aims to propose a model of the fidget spinner gadget. It
exists under different forms with 2, 3 poles and even more. We chose the
most popular model: the triple Fidget Spinner. You can run the PSTricks
related documents with XeLaTeX.

