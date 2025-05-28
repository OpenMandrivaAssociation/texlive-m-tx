Name:		texlive-m-tx
Version:	75301
Release:	1
Summary:	A preprocessor for pmx
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/m-tx
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/m-tx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/m-tx.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-m-tx.bin

%description
M-Tx is a preprocessor to pmx, which is itself a preprocessor
to musixtex, a music typesetting system. The prime motivation
to the development of M-Tx was to provide lyrics for music to
be typeset. In fact, pmx now provides a lyrics interface, but
M-Tx continues in use by those who prefer its language.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/m-tx
%{_texmfdistdir}/scripts/m-tx
%{_texmfdistdir}/tex/generic/m-tx
%{_texmfdistdir}/tex/latex/m-tx
%doc %{_texmfdistdir}/doc/generic/m-tx
%doc %{_mandir}/man1/prepmx.1*
%doc %{_texmfdistdir}/doc/man/man1/prepmx.man1.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/m-tx/m-tx.lua m-tx
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
