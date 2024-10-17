Name:		texlive-underlin
Version:	15878
Release:	2
Summary:	Underlined running heads
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/underlin
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/underlin.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/underlin.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/underlin.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines two pagestyles that provide underlined page heads in
LaTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/underlin/underlin.sty
%doc %{_texmfdistdir}/doc/latex/underlin/underlin.pdf
#- source
%doc %{_texmfdistdir}/source/latex/underlin/underlin.dtx
%doc %{_texmfdistdir}/source/latex/underlin/underlin.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
