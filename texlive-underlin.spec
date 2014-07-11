# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/underlin
# catalog-date 2007-06-02 10:25:58 +0200
# catalog-license lppl
# catalog-version 1.01
Name:		texlive-underlin
Version:	1.01
Release:	8
Summary:	Underlined running heads
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/underlin
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/underlin.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/underlin.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/underlin.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.01-2
+ Revision: 757283
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.01-1
+ Revision: 719846
- texlive-underlin
- texlive-underlin
- texlive-underlin

