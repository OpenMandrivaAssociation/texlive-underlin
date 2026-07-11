%global tl_name underlin
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.01
Release:	%{tl_revision}.1
Summary:	Underlined running heads
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/underlin
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/underlin.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/underlin.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/underlin.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Defines two pagestyles that provide underlined page heads in LaTeX.

