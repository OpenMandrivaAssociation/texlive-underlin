# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/underlin
# catalog-date 2007-06-02 10:25:58 +0200
# catalog-license lppl
# catalog-version 1.01
Name:		texlive-underlin
Version:	1.01
Release:	1
Summary:	Underlined running heads
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/underlin
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/underlin.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/underlin.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/underlin.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Defines two pagestyles that provide underlined page heads in
LaTeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/underlin/underlin.sty
%doc %{_texmfdistdir}/doc/latex/underlin/underlin.pdf
#- source
%doc %{_texmfdistdir}/source/latex/underlin/underlin.dtx
%doc %{_texmfdistdir}/source/latex/underlin/underlin.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
