Name:		texlive-unfonts-extra
Version:	56291
Release:	2
Summary:	TrueType version of Un-fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/unfonts-extra
License:	gpl2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unfonts-extra.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unfonts-extra.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Un-fonts come from the HLaTeX as type1 fonts in 1998 by
Koaunghi Un, he made type1 fonts to use with Korean TeX
(HLaTeX) in the late 1990's and released it under the GPL
license. They were converted to TrueType with the FontForge
(PfaEdit) by Won-kyu Park in 2003. Extra families (10 fonts):
UnPen, UnPenheulim: script UnTaza: typewriter style UnBom:
decorative UnShinmun UnYetgul: old Korean printing style
UnJamoSora, UnJamoNovel, UnJamoDotum, UnJamoBatang

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/truetype/public/unfonts-extra
%doc %{_texmfdistdir}/doc/fonts/unfonts-extra

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
